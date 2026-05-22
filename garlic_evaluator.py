import base64
from datasets import load_dataset
import docker  # 直接使用底层的 docker 引擎

def main():
    print("🧅 [步骤 1] 正在加载 HumanEval 数据集...")
    dataset = load_dataset("openai_humaneval", split="test")

    task = dataset[0]
    prompt = task["prompt"]
    test_cases = task["test"]
    entry_point = task["entry_point"]

    print(f"🎯 [步骤 2] 正在构建测试用例，当前题目: {entry_point}")

    # ==========================================
    # 🤖 伪造的大模型错误代码
    # ==========================================
    mock_llm_code = "    return False\n"

    # 拼装代码
    full_test_code = f"""
{prompt}{mock_llm_code}

{test_cases}

try:
    check({entry_point})
    print("GARLIC_ALL_TESTS_PASSED")
except AssertionError:
    print("GARLIC_ASSERTION_ERROR")
    import sys
    sys.exit(1)
except Exception as e:
    print(f"GARLIC_RUNTIME_ERROR: {{e}}")
    import sys
    sys.exit(1)
"""

    print("🚀 [步骤 3] 正在启动【纯净版 RL Docker 沙盒】...")

    # 直接与你电脑上的 Docker Desktop 通信
    client = docker.from_env()

    # Base64 编码，防止代码里的单双引号破坏 Linux 终端命令
    encoded_code = base64.b64encode(full_test_code.encode('utf-8')).decode('utf-8')

    # 组合 Linux 命令：解码代码并运行 (注意这里的 python3 -u)
    command = f'sh -c "echo {encoded_code} | base64 -d > eval_task.py && python3 -u eval_task.py"'

    logs = ""
    exit_code = 0

    try:
        print("🏃 [步骤 4] 沙盒正在独立运行代码 (无网络, 限制内存)...")
        # 核心！一步到位启动容器、执行、拿结果、并自动销毁
        output = client.containers.run(
            image="python:3.10-slim",  # 极其纯净轻量的 Python 镜像
            command=command,
            remove=True,               # 运行完【立刻销毁】容器，保持电脑干干净净
            network_disabled=True,     # 【断网运行】绝对安全，防止模型写恶意下载代码
            mem_limit="512m"           # 【限制内存】防止模型写出死循环撑爆你的内存
        )
        logs = output.decode('utf-8')
    except docker.errors.ContainerError as e:
        # Docker 的 ContainerError 把所有输出都合并到了 e.stderr 属性中
        logs = e.stderr.decode('utf-8') if getattr(e, 'stderr', None) else ""
        exit_code = e.exit_status
    except Exception as e:
        logs = str(e)
        exit_code = -1

    print("\n" + "="*50)
    print("📊 [判卷报告]")
    print(f"退出状态码 (Exit Code): {exit_code}")
    print(f"沙盒输出 (Logs): \n{logs.strip()}")
    print("-" * 50)

    # 🌟 提取强化学习的 Reward (奖励信号)
    if "GARLIC_ALL_TESTS_PASSED" in logs:
        print("✅ 最终判定: 测试通过 -> 给予模型 Reward = +1.0")
    elif "GARLIC_ASSERTION_ERROR" in logs:
        print("❌ 最终判定: 逻辑错误 (断言失败) -> 给予模型 Reward = -1.0")
    else:
        print("⚠️ 最终判定: 语法错误或运行崩溃 -> 给予模型 Reward = -1.0")
    print("="*50 + "\n")

    print("🧹 沙盒考场已物理蒸发 (容器自动回收)。")

if __name__ == "__main__":
    main()
