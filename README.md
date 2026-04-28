# Quick Copilot Hackday

A self-contained **20-minute GitHub Copilot workshop** focused on **Agent mode**, **Plan mode**, and **Agent Skills**, plus the customization files (`copilot-instructions.md`, `*.instructions.md`, `*.prompt.md`, `SKILL.md`) that steer Copilot toward your team's standards.

The repo doubles as a working example: the customization files in [.github/](.github/) are real and active when you open this folder in VS Code with the Copilot Chat extension.

## What's in here

| Path | Purpose |
|---|---|
| [workshop/README.md](workshop/README.md) | Workshop agenda, learning objectives, mental model |
| [workshop/facilitator.md](workshop/facilitator.md) | Minute-by-minute talk track and exact prompts to paste during demos |
| [workshop/attendee-guide.md](workshop/attendee-guide.md) | 3-step hands-on guide attendees follow on their own laptops |
| [workshop/cheatsheet.md](workshop/cheatsheet.md) | One-page mode + customization cheat sheet |
| [workshop/demo/buggy_math.py](workshop/demo/buggy_math.py) | Intentionally broken file used in the live Agent-mode demo |
| [.github/copilot-instructions.md](.github/copilot-instructions.md) | Repo-wide standards Copilot inherits on every request |
| [.github/instructions/python.instructions.md](.github/instructions/python.instructions.md) | Python-specific rules, scoped via `applyTo` |
| [.github/prompts/add-endpoint.prompt.md](.github/prompts/add-endpoint.prompt.md) | Reusable `/add-endpoint` prompt (user-invoked macro) |
| [.github/skills/pydantic-endpoint/SKILL.md](.github/skills/pydantic-endpoint/SKILL.md) | Skill the agent auto-loads when scaffolding endpoints |

## How to run the workshop

1. Open this repo in VS Code with GitHub Copilot Chat installed.
2. Facilitator: follow [workshop/facilitator.md](workshop/facilitator.md).
3. Attendees: follow [workshop/attendee-guide.md](workshop/attendee-guide.md).

## Mental model in one line

> **Instructions** are always-on rules. **Prompts** are macros *you* invoke. **Skills** are expert workflows the *agent* invokes when your task matches.

## Requirements

- VS Code with the GitHub Copilot and GitHub Copilot Chat extensions.
- Copilot Chat must show the **Ask / Plan / Agent** mode picker.
- For the demo to actually run tests, Python 3.12+ and `pytest` available on `PATH`.
