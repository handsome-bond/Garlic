import asyncio
# 【修改点】路径更新为 PROJECT_DIRECTORY.md 中标注的真实路径
from openhands.app_server.sandbox.sandbox_service import SandboxService

async def main():
    print("🧅 成功导入沙盒模块！正在初始化 Garlic Docker 沙盒...")

    try:
        # 注意：不同版本的 OpenHands 初始化参数可能略有不同
        # 如果这里报错，我们再根据它的报错微调参数
        sandbox = SandboxService.create(
            sandbox_type="docker",
            sandbox_config={}
        )

        await sandbox.start()
        print("✅ 沙盒启动成功！正在执行测试代码...")

        # 1. 测试一段正确的代码
        action_correct = "python3 -c \"print('Hello from Garlic Sandbox!')\""
        print(f"\n👉 执行: {action_correct}")
        result_correct = await sandbox.execute_command(action_correct)
        print(f"输出 (stdout): {result_correct.output}")

        # 2. 测试一段报错的代码
        action_error = "python3 -c \"print(1/0)\""
        print(f"\n👉 执行: {action_error}")
        result_error = await sandbox.execute_command(action_error)
        print(f"错误输出 (stderr): {result_error.output}")

        # 清理沙盒
        await sandbox.close()
        print("\n🧹 沙盒已清理关闭。")

    except Exception as e:
        print(f"❌ 运行过程中出现错误: {e}")

if __name__ == "__main__":
    asyncio.run(main())
