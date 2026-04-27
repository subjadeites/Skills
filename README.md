# Skills

## Language

- **English (Default)** — you are here
- **中文** — see [README_CN.md](README_CN.md)

This repository collects skills for both OpenClaw and coding agents. Each skill must declare its intended host type so users know whether it depends on OpenClaw runtime features or can be used directly by a coding agent.

## What is a skill

A *skill* is a focused, task-oriented guide that tells the assistant:

- **What it is for** (core goal/value)
- **When to use it** (applicable scenarios)
- **How to invoke it** (trigger/entrypoint and expected inputs)

### How to use skills (as a user)

- **When to call**: when you want a specific workflow, quality bar, or operating mode (e.g., “relay this dev session to chat”, “do a UI/UX audit”, “optimize Next.js performance”).
- **How to trigger**: explicitly name the skill in your request *or* use the skill’s documented invocation command (some skills define a command-like entrypoint).
- **What to provide**: concrete inputs and constraints (repo/workdir, target files, acceptance criteria, and any “must/ must-not” requirements). Missing inputs mean the assistant has to ask more questions.

### Skill types

| Type | Meaning | Use this type when |
|------|---------|--------------------|
| OpenClaw skill | A skill that depends on OpenClaw runtime features, such as command registration, inline buttons, session keys, or OpenClaw plugins. | The skill cannot provide its full workflow without OpenClaw-specific host support. |
| Coding Agent skill | A portable skill for coding agents, such as Codex or Claude Code, that can be loaded from its `SKILL.md` without OpenClaw-specific runtime assumptions. | The skill describes a coding workflow, tool wrapper, review mode, or development practice for a coding agent. |

### Coding Agent skills

| Skill | Core goal / value | When to use | How to invoke |
|------|--------------------|-------------|---------------|
| `engineering-refactor` | Bring an existing codebase closer to delivery-grade engineering quality through focused cleanup and refactoring. | You want a coding agent to inspect project conventions, remove low-value code, simplify implementation, and run available validation. | Name `engineering-refactor` in your request and provide the target repo, scope, and acceptance criteria. See `engineering-refactor/SKILL.md`. |

### OpenClaw skills

| Skill | Core goal / value | When to use | How to invoke |
|------|--------------------|-------------|---------------|
| `codeflow` | Make coding agent work **observable** by live-streaming tool calls, file writes, commands, and results to Discord/Telegram. | You want transparent, real-time relay of an OpenClaw-driven coding or review session (no “black box”). | Invoke `/codeflow` to activate the OpenClaw session-scoped contract. See `codeflow/SKILL.md`. |

Use the built-in `openclaw skills search` CLI command for ClawHub discovery.

### Where to look next

- Each skill’s source of truth is its own `SKILL.md`.
- If a skill has required setup, the `SKILL.md` should link to it directly.

## License

See `LICENSE`.
