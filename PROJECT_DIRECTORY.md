# OpenHands 项目目录详解

> **OpenHands** 是一个 AI 驱动的自动化软件开发平台（AI Software Engineer）。包含 Python 后端 (`openhands/`) 和 React 前端 (`frontend/`)，以及企业版模块 (`enterprise/`)。
git add .
git commit -m "feat: 更新"
git push origin main

---

## 一、根目录文件

| 文件 | 说明 |
|------|------|
| `.dockerignore` | Docker 构建时忽略的文件列表 |
| `.editorconfig` | 跨编辑器代码风格配置（缩进、换行等） |
| `.gitattributes` | Git 属性配置（文件类型与换行处理） |
| `.gitignore` | Git 忽略规则（含 Python/Node/Docker/IDE 等常见忽略项） |
| `.nvmrc` | Node.js 版本管理，指定项目使用的 Node 版本 |
| `AGENTS.md` | AI Agent 操作指南——当用 Claude/其他 Agent 操作此项目时的行为规范与流程说明 |
| `CITATION.cff` | 学术引用信息文件（CFF 格式） |
| `CNAME` | GitHub Pages 自定义域名配置 |
| `CODE_OF_CONDUCT.md` | 社区行为准则 |
| `COMMUNITY.md` | 社区介绍与加入方式（Slack、贡献指南等） |
| `CONTRIBUTING.md` | 贡献指南——如何提交 PR、代码风格要求 |
| `CREDITS.md` | 项目致谢与依赖声明 |
| `Development.md` | 开发环境搭建与运行说明（后端、前端、Docker 等详细步骤） |
| `ISSUE_TRIAGE.md` | Issue 分类处理流程 |
| `LICENSE` | MIT 许可证 |
| `MANIFEST.in` | Python 包分发包含/排除文件清单 |
| `Makefile` | 构建自动化脚本——包含 build/run/test/lint/install-pre-commit-hooks 等目标 |
| `README.md` | 项目主文档——介绍 OpenHands 的 SDK/CLI/GUI 三种使用方式 |
| `build.sh` | 简化的构建入口脚本 |
| `config.template.toml` | 配置文件模板——包含 LLM、沙箱、服务器、安全等全部配置项及注释 |
| `docker-compose.yml` | Docker Compose 编排——用于本地启动完整应用（app + db） |
| `poetry.lock` | Python 依赖锁定文件（Poetry 生成） |
| `pydoc-markdown.yml` | pydoc-markdown 文档生成配置 |
| `pyproject.toml` | Python 项目元数据与依赖声明——含 FastAPI、Anthropic SDK、boto3 等核心依赖 |
| `pytest.ini` | pytest 测试框架配置 |
| `uv.lock` | UV 包管理器的依赖锁定文件 |

---

## 二、`openhands/` — Python 后端核心

### 2.1 顶层文件

| 文件 | 说明 |
|------|------|
| `openhands/__init__.py` | 包初始化 |
| `openhands/version.py` | 版本号定义 |

### 2.2 `openhands/server/` — 服务器入口与配置

| 文件 | 说明 |
|------|------|
| `__init__.py` | 包初始化 |
| `__main__.py` | 服务器作为 `python -m openhands.server` 的入口 |
| `app.py` | FastAPI 应用初始化——创建 app 实例、注册中间件和路由 |
| `listen.py` | 服务器监听启动逻辑——支持 HTTP/HTTPS/Unix Socket |
| `middleware.py` | 自定义中间件（CORS、请求日志等） |
| `shared.py` | 服务间共享工具与常量 |
| `static.py` | 静态文件服务——用于托管前端构建产物（SPA） |
| `types.py` | 服务器层类型定义 |
| `config/server_config.py` | 服务器配置定义——端口、主机、CORS 等 |

### 2.3 `openhands/app_server/` — 应用服务器（REST API 层）

这是 API 的核心实现，包含所有业务路由和服务：

#### 2.3.1 核心入口

| 文件 | 说明 |
|------|------|
| `__init__.py` | 包初始化 |
| `app.py` | FastAPI 应用工厂——组装路由、服务注入、生命周期管理 |
| `config.py` | 应用配置（环境变量读取、配置模型） |
| `constants.py` | 应用级常量 |
| `conversation_paths.py` | 会话文件路径工具 |
| `errors.py` | 自定义异常类 |
| `middleware.py` | API 中间件（认证、数据库会话注入等） |
| `shared.py` | 共享工具 |
| `static.py` | 静态文件服务 |
| `types.py` | 类型定义 |
| `v1_router.py` | V1 API 总路由——聚合所有子路由 |
| `version.py` | 应用版本 |

#### 2.3.2 `app_conversation/` — 会话管理

| 文件 | 说明 |
|------|------|
| `app_conversation_info_service.py` | 会话信息服务接口 |
| `app_conversation_models.py` | 会话数据模型 |
| `app_conversation_router.py` | 会话 CRUD API 路由 |
| `app_conversation_service.py` | 会话核心业务逻辑 |
| `app_conversation_service_base.py` | 会话服务抽象基类 |
| `app_conversation_start_task_service.py` | 创建新会话任务的服务 |
| `hook_loader.py` | 会话 Hook 加载器 |
| `live_status_app_conversation_service.py` | 会话实时状态服务 |
| `skill_loader.py` | 技能（Skills）加载器 |
| `sql_app_conversation_info_service.py` | 基于 SQL 的会话信息存储实现 |
| `sql_app_conversation_start_task_service.py` | 基于 SQL 的会话启动任务存储 |

#### 2.3.3 `app_lifespan/` — 应用生命周期与数据库迁移

| 文件 | 说明 |
|------|------|
| `app_lifespan_service.py` | 应用启动/关闭生命周期服务接口 |
| `oss_app_lifespan_service.py` | 开源版生命周期实现 |
| `alembic/env.py` | Alembic 数据库迁移环境配置 |
| `alembic/versions/001.py ~ 009.py` | 数据库迁移脚本（9 个版本） |

#### 2.3.4 `config_api/` — 配置 API

| 文件 | 说明 |
|------|------|
| `config_models.py` | 配置数据模型 |
| `config_router.py` | 配置查询 API 路由 |
| `default_llm_model_service.py` | 默认 LLM 模型配置服务 |
| `llm_model_service.py` | LLM 模型服务接口 |

#### 2.3.5 `event/` — 事件系统

| 文件 | 说明 |
|------|------|
| `event_router.py` | 事件 API 路由（SSE 流式事件推送） |
| `event_service.py` | 事件服务接口 |
| `event_service_base.py` | 事件服务抽象基类 |
| `event_store.py` | 事件存储——保存 Agent 执行产生的各类事件 |
| `aws_event_service.py` | AWS 事件服务实现（基于 AWS 基础设施） |
| `filesystem_event_service.py` | 基于文件系统的事件存储 |
| `google_cloud_event_service.py` | 基于 Google Cloud 的事件存储 |

#### 2.3.6 `event_callback/` — 事件回调

| 文件 | 说明 |
|------|------|
| `event_callback_models.py` | 回调数据模型 |
| `event_callback_result_models.py` | 回调结果数据模型 |
| `event_callback_service.py` | 回调服务接口 |
| `set_title_callback_processor.py` | 自动设置会话标题的回调处理器 |
| `sql_event_callback_service.py` | 基于 SQL 的回调存储 |
| `util.py` | 回调工具函数 |
| `webhook_router.py` | Webhook 回调路由 |

#### 2.3.7 `file_store/` — 文件存储

| 文件 | 说明 |
|------|------|
| `files.py` | 文件存储抽象接口 |
| `google_cloud.py` | Google Cloud Storage 实现 |
| `local.py` | 本地文件系统存储实现 |
| `memory.py` | 内存存储实现（测试用） |
| `s3.py` | AWS S3 存储实现 |

#### 2.3.8 `git/` — Git 操作

| 文件 | 说明 |
|------|------|
| `git_models.py` | Git 操作数据模型 |
| `git_router.py` | Git 操作 API 路由（分支、PR、提交等） |

#### 2.3.9 `integrations/` — 第三方代码托管平台集成

**GitHub:**
| 文件 | 说明 |
|------|------|
| `github/github_service.py` | GitHub 集成服务主逻辑 |
| `github/queries.py` | GitHub GraphQL 查询模板 |
| `github/service/base.py` | GitHub 服务基类 |
| `github/service/branches_prs.py` | GitHub 分支与 PR 操作 |
| `github/service/features.py` | GitHub 特性操作 |
| `github/service/prs.py` | GitHub PR 操作 |
| `github/service/repos.py` | GitHub 仓库操作 |
| `github/service/resolver.py` | GitHub 仓库 URL 解析 |

**GitLab:**
| 文件 | 说明 |
|------|------|
| `gitlab/constants.py` | GitLab 常量 |
| `gitlab/gitlab_service.py` | GitLab 服务主入口 |
| `gitlab/service/base.py` | GitLab 服务基类 |
| `gitlab/service/branches.py` | GitLab 分支操作 |
| `gitlab/service/features.py` | GitLab 特性操作 |
| `gitlab/service/prs.py` | GitLab MR 操作 |
| `gitlab/service/repos.py` | GitLab 仓库操作 |
| `gitlab/service/resolver.py` | GitLab URL 解析 |

**Bitbucket / Bitbucket Data Center / Azure DevOps / Forgejo:**
- 与上述结构类似，各自包含 `service/base.py`、`service/branches.py`、`service/prs.py`、`service/repos.py`、`service/resolver.py` 等

**基础设施:**
| 文件 | 说明 |
|------|------|
| `protocols/http_client.py` | HTTP 客户端协议定义 |
| `provider.py` | 集成提供商注册 |
| `service_types.py` | 服务类型枚举 |
| `utils.py` | 集成工具函数 |

#### 2.3.10 `mcp/` — MCP（Model Context Protocol）

| 文件 | 说明 |
|------|------|
| `mcp_router.py` | MCP 协议路由——支持工具/资源/提示的协议实现 |

#### 2.3.11 `pending_messages/` — 待处理消息

| 文件 | 说明 |
|------|------|
| `pending_message_models.py` | 待处理消息数据模型 |
| `pending_message_router.py` | 待处理消息 API 路由 |
| `pending_message_service.py` | 待处理消息服务——管理 Agent 的待发送消息 |

#### 2.3.12 `sandbox/` — 沙箱环境

| 文件 | 说明 |
|------|------|
| `sandbox_models.py` | 沙箱数据模型 |
| `sandbox_router.py` | 沙箱 API 路由 |
| `sandbox_service.py` | 沙箱服务接口 |
| `docker_sandbox_service.py` | Docker 容器沙箱实现 |
| `docker_sandbox_spec_service.py` | Docker 沙箱规格（镜像、资源配置） |
| `preset_sandbox_spec_service.py` | 预设沙箱规格 |
| `process_sandbox_service.py` | 本地进程沙箱实现（非 Docker） |
| `process_sandbox_spec_service.py` | 本地进程沙箱规格 |
| `remote_sandbox_service.py` | 远程沙箱服务——通过 API 调用远程沙箱 |
| `remote_sandbox_spec_service.py` | 远程沙箱规格 |
| `sandbox_spec_models.py` | 沙箱规格数据模型 |
| `sandbox_spec_router.py` | 沙箱规格 API 路由 |
| `sandbox_spec_service.py` | 沙箱规格服务接口 |
| `session_auth.py` | 沙箱会话认证 |

#### 2.3.13 `secrets/` — 密钥管理

| 文件 | 说明 |
|------|------|
| `secrets_models.py` | 密钥数据模型 |
| `secrets_router.py` | 密钥 CRUD API 路由 |
| `secrets_store.py` | 密钥存储接口 |
| `file_secrets_store.py` | 基于文件的密钥存储实现 |

#### 2.3.14 `server_config/` — 服务器配置

| 文件 | 说明 |
|------|------|
| `server_config.py` | 服务器全局配置服务 |

#### 2.3.15 `services/` — 基础服务

| 文件 | 说明 |
|------|------|
| `db_session_injector.py` | 数据库会话依赖注入 |
| `httpx_client_injector.py` | HTTP 客户端依赖注入 |
| `injector.py` | 通用依赖注入框架 |
| `jwt_service.py` | JWT 令牌服务——生成/验证访问令牌 |

#### 2.3.16 `settings/` — 用户设置

| 文件 | 说明 |
|------|------|
| `settings_models.py` | 设置数据模型（LLM 密钥、Agent 配置等） |
| `settings_router.py` | 设置 CRUD API 路由 |
| `settings_store.py` | 设置存储接口 |
| `file_settings_store.py` | 基于文件的设置存储 |
| `llm_profiles.py` | LLM 配置文件管理 |

#### 2.3.17 `status/` — 系统状态

| 文件 | 说明 |
|------|------|
| `status_router.py` | 健康检查与状态 API 路由 |
| `system_stats.py` | 系统资源统计（CPU、内存、磁盘） |

#### 2.3.18 `user/` — 用户管理

| 文件 | 说明 |
|------|------|
| `user_models.py` | 用户数据模型 |
| `user_router.py` | 用户 API 路由 |
| `user_context.py` | 用户上下文服务 |
| `auth_user_context.py` | 认证用户上下文 |
| `specifiy_user_context.py` | 特定用户上下文 |
| `skills_router.py` | 用户技能 API 路由 |

#### 2.3.19 `user_auth/` — 用户认证

| 文件 | 说明 |
|------|------|
| `user_auth.py` | 用户认证接口 |
| `default_user_auth.py` | 默认认证实现 |

#### 2.3.20 `utils/` — 工具函数集

| 文件 | 说明 |
|------|------|
| `async_utils.py` | 异步工具（异步重试、超时等） |
| `chunk_localizer.py` | 代码块定位工具——处理大文件的代码片段 |
| `dependencies.py` | 依赖检查与安装工具 |
| `docker_utils.py` | Docker 操作工具函数 |
| `encryption_key.py` | 加密密钥生成与管理 |
| `environment.py` | 环境变量解析与验证 |
| `git.py` | Git 操作工具函数 |
| `http_session.py` | HTTP 会话管理 |
| `import_utils.py` | 动态导入工具 |
| `jsonpatch_compat.py` | JSON Patch 兼容性处理 |
| `llm.py` | LLM 调用工具函数 |
| `llm_metadata.py` | LLM 元数据管理 |
| `logger.py` | 日志配置工具 |
| `models.py` | 通用数据模型 |
| `paging_utils.py` | 分页工具 |
| `search_utils.py` | 搜索工具函数 |
| `shutdown_listener.py` | 优雅关闭监听器 |
| `sql_utils.py` | SQL 工具函数 |

#### 2.3.21 `web_client/` — Web 客户端配置

| 文件 | 说明 |
|------|------|
| `web_client_models.py` | Web 客户端配置模型 |
| `web_client_router.py` | Web 客户端配置 API 路由 |
| `web_client_config_injector.py` | Web 客户端配置注入接口 |
| `default_web_client_config_injector.py` | 默认 Web 客户端配置注入 |
| `web_client_deployment_mode.py` | 部署模式（OSS/SAAS） |

---

## 三、`frontend/` — React 前端

### 3.1 `frontend/src/api/` — API 服务层

每个子目录包含对应后端 API 的 TypeScript 客户端（React Query hooks + API 调用）：

| 目录/文件 | 说明 |
|------|------|
| `auth-service/` | 认证 API（登录、注册、令牌刷新） |
| `billing-service/` | 计费 API（套餐、使用量） |
| `config-service/` | 配置 API（服务器配置查询） |
| `conversation-service/` | 会话 API（会话 CRUD、消息发送） |
| `email-service/` | 邮件 API |
| `event-service/` | 事件 API（SSE 流式事件消费） |
| `git-service/` | Git 操作 API |
| `integration-service/` | 第三方集成 API |
| `onboarding-service/` | 新手引导 API |
| `option-service/` | 选项/枚举 API |
| `organization-service/` | 组织/团队 API |
| `pending-message-service/` | 待发送消息 API |
| `sandbox-service/` | 沙箱 API |
| `settings-service/` | 用户设置 API |
| `suggestions-service/` | 建议/自动补全 API |
| `user-service/` | 用户 API |

### 3.2 `frontend/src/components/` — UI 组件

#### 3.2.1 `components/features/` — 功能组件

| 文件/目录 | 说明 |
|------|------|
| `alerts/alert-banner.tsx` | 顶部告警横幅组件 |
| `analytics/analytics-consent-form-modal.tsx` | 分析同意弹窗 |
| `auth/login-content.tsx` | 登录表单内容 |
| `auth/login-cta.tsx` | 登录引导按钮 |
| `browser/browser.tsx` | 内嵌浏览器组件 |
| `browser/browser-snapshot.tsx` | 浏览器截图快照 |
| `browser/empty-browser-message.tsx` | 浏览器空状态提示 |
| `chat/` | **聊天核心组件群**： |
| `chat/chat-interface.tsx` | 聊天主界面——消息列表 + 输入框 + 状态栏 |
| `chat/chat-message.tsx` | 单条聊天消息渲染 |
| `chat/chat-action-tooltip.tsx` | 操作提示框 |
| `chat/chat-add-file-button.tsx` | 添加文件按钮 |
| `chat/chat-send-button.tsx` | 发送按钮 |
| `chat/chat-stop-button.tsx` | 停止 Agent 按钮 |
| `chat/chat-play-button.tsx` | 启动/恢复 Agent 按钮 |
| `chat/chat-status-indicator.tsx` | Agent 运行状态指示器 |
| `chat/chat-suggestions.tsx` | 智能建议面板 |
| `chat/chat-messages-skeleton.tsx` | 消息加载骨架屏 |
| `chat/change-agent-button.tsx` | 切换 Agent 类型按钮 |
| `chat/change-agent-context-menu.tsx` | Agent 切换上下文菜单 |
| `chat/custom-chat-input.tsx` | 自定义聊天输入框 |
| `chat/btw-messages.tsx` | "中间"消息（Agent 内部思考） |
| `chat/archived-banner.tsx` | 已归档会话横幅 |
| `chat/drag-over.tsx` | 文件拖放覆盖层 |
| `chat/error-message.tsx` | 错误消息组件 |
| `chat/error-message-banner.tsx` | 错误消息横幅 |
| `chat/event-message.tsx` | 事件消息渲染——根据事件类型分发 |
| `chat/generic-event-message.tsx` | 通用事件消息 |
| `chat/expandable-message.tsx` | 可展开/折叠消息 |
| `chat/confirmation-mode-enabled.tsx` | 确认模式提示 |
| `chat/event-message-components/` | 事件消息子组件（错误/完成/MCP/Hook/拒绝/任务跟踪等） |
| `chat/event-content-helpers/get-event-content.tsx` | 事件内容提取辅助函数 |
| `chat/components/` | 聊天子组件（输入框行/输入框容器/斜杠命令菜单/隐藏文件输入等） |
| `chat/git-control-bar-*.tsx` | Git 控制栏（分支/PR/Pull/Push 按钮） |

#### 3.2.2 `components/providers/` — Context Provider

| 文件 | 说明 |
|------|------|
| 各类 Provider | React Context 提供者（主题、认证、配置等全局状态注入） |

#### 3.2.3 `components/shared/` — 共享组件

| 文件 | 说明 |
|------|------|
| 通用共享组件 | 跨页面复用的图标、按钮、布局等 |

#### 3.2.4 `components/ui/` 和 `components/v1/` — UI 基础组件

| 文件 | 说明 |
|------|------|
| UI 基础组件 | 通用的 Input/Button/Modal/Dropdown 等基础 UI 元素 |

### 3.3 `frontend/src/hooks/` — React Hooks

| 目录/文件 | 说明 |
|------|------|
| `chat/` | 聊天相关 Hooks（消息发送、SSE 事件订阅） |
| `mutation/` | React Query Mutation Hooks 封装 |
| `query/` | React Query Query Hooks 封装 |
| `organizations/` | 组织相关 Hooks |

### 3.4 `frontend/src/stores/` — 状态管理

| 文件 | 说明 |
|------|------|
| 状态 Store | 全局状态管理（用户信息、UI 状态、Agent 运行状态等） |

### 3.5 `frontend/src/routes/` — 路由/页面

| 文件 | 说明 |
|------|------|
| 路由配置 | React Router 路由定义——页面映射与导航守卫 |

### 3.6 其他前端目录

| 目录 | 说明 |
|------|------|
| `src/assets/` | 静态资源（图片、Logo） |
| `src/assets/branding/` | 品牌资源（Logo 变体、图标） |
| `src/constants/` | 常量定义 |
| `src/context/` + `src/contexts/` | React Context 定义 |
| `src/i18n/` | 国际化（多语言翻译文件） |
| `src/icons/` | SVG 图标组件 |
| `src/mocks/` | API Mock 数据（开发/测试用） |
| `src/services/` | 业务服务层——封装 API 调用外的业务逻辑 |
| `src/types/` + `src/types/core/` + `src/types/v1/` | TypeScript 类型定义 |
| `src/ui/` + `src/ui/dropdown/` | UI 工具组件 |
| `src/utils/` | 工具函数（日期、字符串、验证等） |
| `src/utils/org/` | 组织相关工具 |
| `src/utils/suggestions/` | 智能建议工具 |
| `src/wrapper/` | 包装组件 |

---

## 四、`enterprise/` — 企业版（SaaS）模块

### 4.1 入口与核心

| 文件 | 说明 |
|------|------|
| `__init__.py` | 企业版包初始化 |
| `saas_server.py` | SaaS 服务器入口——企业版完整服务器启动 |
| `run_maintenance_tasks.py` | 后台维护任务执行器（定时清理、同步等） |

### 4.2 `enterprise/analytics/` — SaaS 分析

| 文件 | 说明 |
|------|------|
| `saas_user_provider.py` | SaaS 用户身份提供者——用于分析追踪的用户标识 |

### 4.3 `enterprise/enterprise_local/` — 本地企业配置

| 文件 | 说明 |
|------|------|
| `convert_to_env.py` | 将企业配置转换为环境变量 |

### 4.4 `enterprise/integrations/` — 企业版集成

**GitHub 集成：**
| 文件 | 说明 |
|------|------|
| `github/github_manager.py` | GitHub App 安装管理——Webhook 处理、OAuth 流程 |
| `github/github_service.py` | GitHub 服务核心逻辑 |
| `github/github_types.py` | GitHub 类型定义 |
| `github/github_v1_callback_processor.py` | V1 API GitHub 回调处理器 |
| `github/github_view.py` | GitHub API 视图/端点 |
| `github/data_collector.py` | GitHub 数据收集（用于分析） |
| `github/queries.py` | GitHub GraphQL 查询 |

**GitLab 集成：**
| 文件 | 说明 |
|------|------|
| `gitlab/gitlab_manager.py` | GitLab Webhook 管理与事件处理 |
| `gitlab/gitlab_service.py` | GitLab 服务核心 |
| `gitlab/gitlab_v1_callback_processor.py` | GitLab 回调处理器 |
| `gitlab/gitlab_view.py` | GitLab API 端点 |
| `gitlab/webhook_installation.py` | GitLab Webhook 安装工具 |

**Bitbucket / Bitbucket Data Center 集成：**
- 与 GitHub/GitLab 结构类似，含 `*_manager.py`、`*_service.py`、`*_v1_callback_processor.py`、`*_view.py`

**Jira 集成：**
| 文件 | 说明 |
|------|------|
| `jira/jira_manager.py` | Jira 工作区管理与 OAuth |
| `jira/jira_payload.py` | Jira Webhook 负载解析 |
| `jira/jira_types.py` | Jira 类型定义 |
| `jira/jira_v1_callback_processor.py` | Jira 回调处理器 |
| `jira/jira_view.py` | Jira API 端点 |

**Jira Data Center 集成：** 同上结构，针对 Jira DC

**Slack 集成：**
| 文件 | 说明 |
|------|------|
| `slack/slack_manager.py` | Slack Bot 管理——OAuth、事件订阅 |
| `slack/slack_types.py` | Slack 类型定义 |
| `slack/slack_v1_callback_processor.py` | Slack 回调处理器 |
| `slack/slack_view.py` | Slack API 端点 |
| `slack/slack_errors.py` | Slack 自定义错误 |

**集成基础设施：**
| 文件 | 说明 |
|------|------|
| `manager.py` | 集成管理器接口 |
| `models.py` | 集成通用数据模型 |
| `resolver_context.py` | 集成 URL 解析上下文 |
| `resolver_org_router.py` | 组织级集成路由 |
| `store_repo_utils.py` | 仓库存储工具 |
| `stripe_service.py` | Stripe 支付服务集成 |
| `types.py` | 集成类型定义 |
| `utils.py` | 集成工具函数 |
| `v1_utils.py` | V1 API 集成工具 |

### 4.5 `enterprise/server/` — 企业版服务器

#### 4.5.1 认证模块 `auth/`

| 文件 | 说明 |
|------|------|
| `auth_error.py` | 认证错误类 |
| `authorization.py` | 授权中间件——权限验证 |
| `constants.py` | 认证常量 |
| `email_validation.py` | 邮件验证服务 |
| `github_utils.py` | GitHub OAuth 工具 |
| `gitlab_sync.py` | GitLab 用户同步 |
| `keycloak_manager.py` | Keycloak 身份管理集成 |
| `org_context.py` | 组织上下文中间件 |
| `recaptcha_service.py` | reCAPTCHA 验证服务 |
| `saas_user_auth.py` | SaaS 用户认证实现 |
| `sheets_client.py` | Google Sheets 客户端 |
| `token_manager.py` | 令牌管理（JWT 生成/验证/刷新） |
| `user/default_user_authorizer.py` | 默认用户授权器 |
| `user/user_authorizer.py` | 用户授权器接口 |

#### 4.5.2 路由 `routes/`

| 文件 | 说明 |
|------|------|
| `api_keys.py` | API 密钥管理路由 |
| `auth.py` | 认证路由（登录/注册/刷新） |
| `billing.py` | 计费路由 |
| `bitbucket_dc_proxy.py` | Bitbucket DC 代理路由 |
| `email.py` | 邮件路由 |
| `github_proxy.py` | GitHub 代理路由 |
| `integration/bitbucket.py` | Bitbucket 集成路由 |
| `integration/bitbucket_dc.py` | Bitbucket DC 集成路由 |
| `integration/github.py` | GitHub 集成路由 |
| `integration/gitlab.py` | GitLab 集成路由 |
| `integration/jira.py` | Jira 集成路由 |
| `integration/jira_dc.py` | Jira DC 集成路由 |
| `integration/slack.py` | Slack 集成路由 |
| `oauth_device.py` | OAuth 设备码流 |
| `onboarding.py` | 新手引导路由 |
| `orgs.py` | 组织 CRUD 路由 |
| `org_models.py` | 组织数据模型 |
| `org_invitations.py` | 组织邀请路由 |
| `org_invitation_models.py` | 邀请数据模型 |
| `readiness.py` | 就绪检查/健康检查 |
| `service.py` | 服务发现路由 |
| `user_app_settings.py` | 用户应用设置路由 |
| `user_app_settings_models.py` | 用户设置模型 |
| `users_v1.py` | 用户管理 V1 路由 |

#### 4.5.3 `services/` — 企业版服务

| 文件 | 说明 |
|------|------|
| `automation_event_service.py` | 自动化事件服务——定时任务/触发器 |
| `email_service.py` | 邮件发送服务（通知/邀请/告警） |
| `org_app_settings_service.py` | 组织应用设置服务 |
| `org_invitation_service.py` | 组织邀请服务——生成/验证/接受邀请 |
| `org_member_financial_service.py` | 组织成员财务服务 |
| `org_member_service.py` | 组织成员管理服务 |
| `user_app_settings_service.py` | 用户应用设置服务 |

#### 4.5.4 `sharing/` — 会话分享

| 文件 | 说明 |
|------|------|
| `shared_conversation_info_service.py` | 分享会话信息服务 |
| `shared_conversation_models.py` | 分享会话模型 |
| `shared_conversation_router.py` | 分享会话 API 路由 |
| `shared_event_router.py` | 分享事件 API 路由 |
| `shared_event_service.py` | 分享事件服务 |
| `aws_shared_event_service.py` | AWS 事件分享实现 |
| `filesystem_shared_event_service.py` | 文件系统事件分享实现 |
| `google_cloud_shared_event_service.py` | Google Cloud 事件分享实现 |
| `sql_shared_conversation_info_service.py` | SQL 分享会话存储 |

#### 4.5.5 `verified_models/` — 已验证模型

| 文件 | 说明 |
|------|------|
| `verified_model_models.py` | 已验证 LLM 模型列表 |
| `verified_model_router.py` | 已验证模型 API 路由 |
| `verified_model_service.py` | 已验证模型服务 |

#### 4.5.6 其他企业服务器文件

| 文件 | 说明 |
|------|------|
| `config.py` | 企业版配置 |
| `constants.py` | 企业版常量 |
| `email_validation.py` | 邮件验证 |
| `logger.py` | 企业版日志配置 |
| `middleware.py` | 企业版中间件（租户隔离、限流等） |
| `models/user_models.py` | 企业版用户模型 |
| `rate_limit.py` | API 限流 |
| `utils/` | 工具函数（会话工具、限流工具、URL 工具、注入器等） |

### 4.6 `enterprise/storage/` — 企业版数据持久层

包含 100+ 个文件，每个数据表对应一组模型+存储文件：

| 类别 | 代表性文件 | 说明 |
|------|------|------|
| **用户与认证** | `user.py`, `user_store.py`, `api_key.py`, `api_key_store.py`, `auth_token_store.py`, `auth_tokens.py`, `device_code.py`, `device_code_store.py`, `offline_token_store.py`, `stored_offline_token.py`, `user_authorization.py`, `user_authorization_store.py` | 用户管理、API 密钥、认证令牌、设备码、离线令牌 |
| **设置** | `user_settings.py`, `user_app_settings_store.py`, `saas_settings_store.py`, `saas_secrets_store.py`, `stored_custom_secrets.py` | 用户/SaaS 设置与密钥存储 |
| **组织** | `org.py`, `org_store.py`, `org_member.py`, `org_member_store.py`, `org_service.py`, `org_invitation.py`, `org_invitation_store.py`, `org_app_settings_store.py`, `org_git_claim.py`, `org_git_claim_store.py`, `role.py`, `role_store.py` | 组织/团队管理、成员、角色、邀请 |
| **会话** | `stored_conversation_metadata.py`, `stored_conversation_metadata_saas.py`, `conversation_work.py`, `feedback.py`, `openhands_pr.py`, `openhands_pr_store.py` | 会话元数据、工作记录、反馈、PR 记录 |
| **集成** | `github_app_installation.py`, `gitlab_webhook.py`, `gitlab_webhook_store.py`, `bitbucket_webhook.py`, `bitbucket_webhook_store.py`, `bitbucket_dc_webhook.py`, `bitbucket_dc_webhook_store.py`, `jira_*.py`, `linear_*.py`, `slack_*.py`, `slack_conversation.py`, `slack_team.py`, `slack_user.py` | 各平台集成配置与状态存储 |
| **计费** | `billing_session.py`, `billing_session_type.py`, `stripe_customer.py`, `subscription_access.py`, `subscription_access_status.py` | Stripe 计费、订阅管理 |
| **仓库** | `stored_repository.py`, `repository_store.py`, `user_repo_map.py`, `user_repo_map_store.py` | 用户仓库映射 |
| **其他** | `database.py`（数据库连接）, `encrypt_utils.py`（加密工具）, `redis.py`（Redis 缓存）, `lite_llm_manager.py`（LLM 管理）, `resend_synced_user.py`, `resend_synced_user_store.py`（邮件同步）, `telemetry_identity.py`, `telemetry_metrics.py`（遥测） | 数据库连接、加密、缓存、LLM 管理、遥测 |

### 4.7 `enterprise/migrations/` — 数据库迁移

109 个 Alembic 迁移版本（`versions/001.py` ~ `versions/109.py`），涵盖：
- 用户/组织/会话表的创建与演进
- 设置表扩展
- 各平台集成表（GitHub/GitLab/Bitbucket/Jira/Slack）
- Stripe 计费表
- MCP 配置、Agent 配置、技能配置等

### 4.8 `enterprise/sync/` — 同步任务

| 文件 | 说明 |
|------|------|
| `clean_proactive_convo_table.py` | 清理主动会话表 |
| `enrich_user_interaction_data.py` | 丰富用户交互数据 |
| `install_gitlab_webhooks.py` | 批量安装 GitLab Webhooks |
| `resend_keycloak.py` | Keycloak 用户同步（通过 Resend 发送邮件） |

### 4.9 `enterprise/tests/` — 企业版测试（约 200+ 测试文件）

覆盖所有企业版功能模块的单元测试，组织结构与源码对应：
- `unit/server/auth/` — 认证测试
- `unit/server/routes/` — 路由测试
- `unit/server/services/` — 服务测试
- `unit/storage/` — 数据存储测试
- `unit/integrations/` — 各平台集成测试
- `unit/sync/` — 同步任务测试

### 4.10 `enterprise/utils/` — 企业版工具

| 文件 | 说明 |
|------|------|
| `identity.py` | 用户身份识别与匿名化工具 |

---

## 五、`openhands-ui/` — 独立 UI 组件库

这是 OpenHands 的设计系统/组件库，独立于主前端应用：

| 目录 | 说明 |
|------|------|
| `components/accordion/` | 手风琴（折叠面板）组件——含 Header/Item/Panel 子组件与 Storybook 故事 |
| `components/button/` | 按钮组件——多种变体、样式与 Storybook |
| `components/checkbox/` | 复选框组件 |
| `components/chip/` | 标签/芯片组件——含工具函数 |
| `components/dialog/` | 对话框/模态框组件 |
| `components/divider/` | 分割线组件 |
| `components/icon/` | 图标组件——统一图标渲染 |
| `components/input/` | 输入框组件 |
| `components/interactive-chip/` | 可交互芯片组件（含 CSS） |
| `components/radio-group/` | 单选按钮组——含 RadioOption 子组件 |
| `components/scrollable/` | 可滚动容器组件 |
| `components/select/` | 下拉选择组件——基于 react-select，含 DropdownIndicator/Option/Placeholder/SingleValue 子组件 |
| `components/spinner/` | 加载旋转器组件 |
| `components/tabs/` | 标签页组件——含 TabItem/TabScroller 及溢出/滚动 Hooks |
| `components/toast/` | Toast 通知组件——含 ToastManager 管理器 |
| `components/toggle/` | 开关切换组件 |
| `components/tooltip/` | 工具提示组件 |
| `components/typography/` | 排版组件——BaseTypography/Typography 及故事 |
| `shared/hooks/` | 共享 Hooks（use-array） |
| `shared/utils/` | 共享工具（cn 类名合并/clone-icon/invariant 断言） |
| `shared/types.ts` | 共享类型定义 |
| `.storybook/` | Storybook 配置（组件文档与可视化开发） |
| `index.ts` | 组件库导出入口 |
| `index.css` | 全局样式 |
| `tokens.css` | 设计 Token（颜色、间距、字体等 CSS 变量） |

---

## 六、`tests/` — 后端测试

```
tests/
├── __init__.py
└── unit/
    ├── __init__.py
    ├── test_analytics_context.py       # 分析上下文测试
    ├── test_analytics_service.py       # 分析服务测试
    ├── test_analytics_user_base.py     # 分析用户基础测试
    ├── test_azure_devops.py            # Azure DevOps 集成测试
    └── test_forgejo_service.py         # Forgejo 代码托管测试
```

---

## 七、`containers/` — Docker 容器配置

| 文件 | 说明 |
|------|------|
| `README.md` | 容器构建说明 |
| `app/Dockerfile` | 生产应用镜像——打包 Python 后端 + 前端构建产物 |
| `app/entrypoint.sh` | 容器入口脚本——数据库迁移 + 启动服务器 |
| `dev/Dockerfile` | 开发环境镜像——含开发工具和热重载 |
| `dev/README.md` | 开发容器说明 |
| `dev/compose.yml` | 开发环境 Docker Compose 编排 |
| `dev/dev.sh` | 开发环境快速启动脚本 |

---

## 八、`scripts/` — 辅助脚本

| 文件 | 说明 |
|------|------|
| `dump_config_schema.py` | 导出配置 JSON Schema——用于配置验证与文档生成 |
| `update_openapi.py` | 更新 OpenAPI/Swagger 规范文档 |

---

## 九、`skills/` — Agent 技能定义

每个 `.md` 文件定义一种 Agent 技能（Skill），告诉 Agent 如何完成特定任务：

| 文件 | 说明 |
|------|------|
| `add_agent.md` | 添加自定义 Agent 的技能 |
| `add_repo_inst.md` | 添加仓库集成指令 |
| `address_pr_comments.md` | 处理 PR 评审意见 |
| `agent-builder.md` | Agent 构建器——指导如何创建新 Agent |
| `agent_memory.md` | Agent 记忆管理 |
| `azure_devops.md` | Azure DevOps 平台集成技能 |
| `bitbucket.md` | Bitbucket 平台操作技能 |
| `bitbucket_data_center.md` | Bitbucket Data Center 操作技能 |
| `code-review.md` | 代码审查技能 |
| `codereview-roasted.md` | 代码审查（幽默风格） |
| `default-tools.md` | 默认工具集配置 |
| `docker.md` | Docker 操作技能 |
| `fix-py-line-too-long.md` | 修复 Python 代码行过长问题 |
| `fix_test.md` | 修复测试用例技能 |
| `flarglebargle.md` | 测试/演示用技能 |
| `github.md` | GitHub 平台操作技能 |
| `gitlab.md` | GitLab 平台操作技能 |
| `kubernetes.md` | Kubernetes 操作技能 |
| `npm.md` | NPM 包管理技能 |
| `onboarding.md` | 新手引导技能 |
| `pdflatex.md` | LaTeX PDF 编译技能 |
| `security.md` | 安全检查技能 |
| `ssh.md` | SSH 连接与操作技能 |
| `swift-linux.md` | Swift on Linux 开发技能 |
| `update_pr_description.md` | 更新 PR 描述技能 |
| `update_test.md` | 更新测试用例技能 |

---

## 十、`.github/` — GitHub 配置

### 10.1 Issue 模板
| 文件 | 说明 |
|------|------|
| `ISSUE_TEMPLATE/bug_template.yml` | Bug 报告表单模板 |
| `ISSUE_TEMPLATE/config.yml` | Issue 配置（禁止空白 Issue） |
| `ISSUE_TEMPLATE/feature_request.yml` | 功能请求表单模板 |

### 10.2 Actions
| 文件 | 说明 |
|------|------|
| `actions/docker-image-tags/action.yml` | Docker 镜像标签生成 Action |
| `actions/docker-merge-manifest/action.yml` | Docker 多架构清单合并 Action |

### 10.3 CI/CD Workflows
| 文件 | 说明 |
|------|------|
| `workflows/_build-image.yml` | 可复用的 Docker 镜像构建 Workflow |
| `workflows/check-package-versions.yml` | 检查包版本一致性 |
| `workflows/check-version-consistency.yml` | 检查版本号一致性 |
| `workflows/enterprise-check-migrations.yml` | 企业版迁移检查 |
| `workflows/fe-e2e-tests.yml` | 前端 E2E 测试 |
| `workflows/fe-unit-tests.yml` | 前端单元测试 |
| `workflows/ghcr-build.yml` | GitHub Container Registry 构建推送 |
| `workflows/lint-fix.yml` | 代码格式化自动修复 |
| `workflows/lint.yml` | 代码规范检查（Python/JS） |
| `workflows/npm-publish-ui.yml` | 发布 openhands-ui 到 npm |
| `workflows/pr-artifacts.yml` | PR 构建产物生成 |
| `workflows/pr-readiness-confirm.yml` | PR 就绪确认 |
| `workflows/pr-review-by-openhands.yml` | OpenHands 自动 PR 审查 |
| `workflows/pr-review-evaluation.yml` | PR 审查评估 |
| `workflows/py-tests.yml` | Python 后端测试 |
| `workflows/pypi-release.yml` | PyPI 发布 |
| `workflows/stale.yml` | 自动关闭过期 Issue/PR |
| `workflows/tag-image.yml` | 发布时打标签并构建镜像 |
| `workflows/ui-build.yml` | UI 构建验证 |
| `workflows/welcome-good-first-issue.yml` | 新人欢迎——推荐 good first issue |

### 10.4 其他
| 文件 | 说明 |
|------|------|
| `dependabot.yml` | Dependabot 依赖自动更新配置 |
| `pull_request_template.md` | PR 描述模板 |
| `scripts/find_prs_between_commits.py` | 查找两个提交之间的 PR |
| `scripts/update_pr_description.sh` | 更新 PR 描述 Shell 脚本 |

---

## 十一、`.openhands/` — OpenHands 自我配置

| 文件 | 说明 |
|------|------|
| `microagents/documentation.md` | 项目文档微 Agent——帮助 Agent 理解项目文档 |
| `microagents/glossary.md` | 术语表——项目专有名词定义 |
| `pre-commit.sh` | 预提交 Hook 脚本 |
| `setup.sh` | 项目初始化设置脚本 |

---

## 十二、其他配置目录

| 目录/文件 | 说明 |
|------|------|
| `.devcontainer/` | VS Code Dev Container 配置——提供一致的容器化开发环境 |
| `.vscode/` | VS Code 编辑器配置——推荐扩展、调试配置、设置 |
| `dev_config/` | 开发环境配置文件（Python pre-commit 配置等） |
| `kind/` | Kubernetes Kind（Kubernetes in Docker）集群配置——用于本地 K8s 测试 |

---

## 项目架构概览

```
                      ┌──────────────────────────┐
                      │     Frontend (React)      │
                      │  frontend/ + openhands-ui/ │
                      └────────────┬─────────────┘
                                   │ REST API / SSE
                      ┌────────────▼─────────────┐
                      │    App Server (FastAPI)    │
                      │   openhands/app_server/    │
                      │   ┌─────────────────────┐ │
                      │   │  Routes / Services   │ │
                      │   │  Auth / Events /     │ │
                      │   │  Sandbox / Settings  │ │
                      │   └─────────────────────┘ │
                      └────────────┬─────────────┘
                                   │
          ┌────────────────────────┼────────────────────────┐
          │                        │                        │
┌─────────▼──────────┐  ┌─────────▼──────────┐  ┌─────────▼──────────┐
│  Enterprise (SaaS)  │  │   Agent Runtime    │  │   Integrations     │
│  enterprise/        │  │   (SDK Engine)     │  │   GitHub/GitLab/   │
│  - Multi-tenant     │  │   - LLM calls      │  │   Bitbucket/Jira/  │
│  - Billing/Stripe   │  │   - Sandbox exec   │  │   Slack/Azure      │
│  - Org management   │  │   - Tool use       │  │                    │
│  - OAuth/SSO        │  │                    │  │                    │
└────────────────────┘  └────────────────────┘  └────────────────────┘
```

- **后端核心** (`openhands/`): FastAPI 应用，提供 REST API + SSE 事件流
- **前端** (`frontend/`): React SPA，通过 API 与后端交互
- **UI 组件库** (`openhands-ui/`): 独立设计系统，发布到 npm
- **企业版** (`enterprise/`): SaaS 多租户功能——计费、组织管理、高级集成
- **技能** (`skills/`): Agent 行为指南，定义如何完成各类编程任务
