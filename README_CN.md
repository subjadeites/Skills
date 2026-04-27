# Skills（中文）

## 语言

- **中文** — 你正在阅读
- **English** — 参见 [README.md](README.md)

本仓库同时收录 OpenClaw skill 和 coding Agent skill。每个 skill 都应标明目标宿主类型，让使用者知道它是依赖 OpenClaw 运行时能力，还是可以被 coding agent 直接读取和执行。

## 什么是 skills

一个 *skill（技能）* 是一份“面向任务”的指引，它会明确告诉助手：

- **做什么**（核心目标/价值）
- **何时用**（适用场景）
- **怎么用**（如何触发/入口，以及需要提供哪些输入）

### 如何使用 skills（对使用者）

- **何时调用（invoke）**：当你需要一个明确的工作流、质量标准或运行模式（例如“把开发会话转播到聊天里”“做 UI/UX 审查”“优化 Next.js 性能”）。
- **如何触发（trigger）**：在需求里直接点名 skill，或使用该 skill 文档里定义的“命令式入口”（有些 skill 会规定类似命令的触发方式）。
- **需要提供什么**：尽量给出可执行的输入与约束（repo/workdir、目标文件、验收标准、必须/禁止项）。输入缺失只会导致更多反问。

### Skill 类型

| 类型 | 含义 | 何时使用 |
|------|------|----------|
| OpenClaw skill | 依赖 OpenClaw 运行时能力的 skill，例如命令注册、inline buttons、session keys 或 OpenClaw plugins。 | 该 skill 缺少 OpenClaw 宿主能力就无法提供完整工作流。 |
| Coding Agent skill | 面向 coding agent（例如 Codex 或 Claude Code）的可移植 skill，可直接从 `SKILL.md` 加载，不假设 OpenClaw 专属运行时。 | 该 skill 描述编码工作流、工具包装、review 模式或开发实践。 |

### Coding Agent skills

| Skill | 核心目标/价值 | 适用场景 | 使用方式 |
|------|----------------|----------|----------|
| `engineering-refactor` | 通过聚焦清理和重构，让现有代码库接近可交付的成熟工程质量。 | 你需要 coding agent 检查项目约定、移除低价值代码、简化实现，并运行可用校验。 | 在需求中点名 `engineering-refactor`，并提供目标仓库、范围和验收标准。详见 `engineering-refactor/SKILL.md`。 |

### OpenClaw skills

| Skill | 核心目标/价值 | 适用场景 | 使用方式 |
|------|----------------|----------|----------|
| `codeflow` | 让 coding agent 的工作 **可观测**：把工具调用、文件写入、命令与结果实时转播到 Discord/Telegram。 | 你需要一个透明、可追踪的 OpenClaw 编码/审查会话（避免“黑盒”）。 | 通过 `/codeflow` 激活 OpenClaw 会话级工作约束。详见 `codeflow/SKILL.md`。 |

搜索 ClawHub 请直接使用内置的 `openclaw skills search` CLI 命令。

### 下一步看哪里

- 每个 skill 的权威文档都在它自己的 `SKILL.md`。
- 如果某个 skill 需要额外配置，`SKILL.md` 一般会提供直接链接/指引。

## 许可证

见 `LICENSE`。
