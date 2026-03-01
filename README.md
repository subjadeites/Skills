# OpenClaw Skills

## Language

- **English (Default)** — you are here
- **中文** — see [README_CN.md](README_CN.md)

## What is a skill

A *skill* is a focused, task-oriented guide that tells the assistant:

- **What it is for** (core goal/value)
- **When to use it** (applicable scenarios)
- **How to invoke it** (trigger/entrypoint and expected inputs)

### How to use skills (as a user)

- **When to call**: when you want a specific workflow, quality bar, or operating mode (e.g., “relay this dev session to chat”, “do a UI/UX audit”, “optimize Next.js performance”).
- **How to trigger**: explicitly name the skill in your request *or* use the skill’s documented invocation command (some skills define a command-like entrypoint).
- **What to provide**: concrete inputs and constraints (repo/workdir, target files, acceptance criteria, and any “must/ must-not” requirements). Missing inputs mean the assistant has to ask more questions.

### Skill catalog

| Skill | Core goal / value | When to use | How to invoke |
|------|--------------------|-------------|---------------|
| `codeflow` | Make coding agent work **observable** by live-streaming tool calls, file writes, commands, and results to Discord/Telegram. | You want transparent, real-time relay of an agent-driven dev/review session (no “black box”). | Invoke `/codeflow` to activate the session-scoped contract, then run coding/review tasks under that mode. See `codeflow/SKILL.md`. |

### Where to look next

- Each skill’s source of truth is its own `SKILL.md`.
- If a skill has required setup, the `SKILL.md` should link to it directly.

## License

See `LICENSE`.
