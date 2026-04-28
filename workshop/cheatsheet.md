# Cheat Sheet — Agent Mode & Skills

## Modes
| Mode | Edits files? | Runs tools? | Use when |
|------|-------------|-------------|----------|
| Ask | No | No | Understanding code |
| Plan | No | Yes (read-only: search, read) | Scoping a multi-file or risky change before edits |
| Agent | Yes | Yes (search, terminal, tests) | Making changes, fixing bugs, scaffolding |

**Pattern:** Plan → review the plan → switch to Agent and say *"execute the plan above"*.

## Driving Agent mode well
- Give it a **goal**, not steps. ("Fix the bug and add a test" > "Open file X, change line 12...")
- Mention success criteria. ("Make sure tests pass.")
- Let it run the terminal — that's where the magic is.
- Approve tools once with "always allow" for safe ones (search, read).
- Stop early if it goes off-track; tighten the prompt or instructions.

## Customization layers (pick the right one)
- Repo-wide rule → `.github/copilot-instructions.md`
- Per-language rule → `.github/instructions/<name>.instructions.md` with `applyTo:`
- One-shot reusable task → `.github/prompts/<name>.prompt.md` (run via `/<name>`)
- Multi-step domain expertise → `.github/skills/<name>/SKILL.md` (auto-loaded by agent)

## Skill description = the trigger
The agent loads a skill when the user's task matches its `description`.
Write descriptions like a search query, not a title.

Bad: `description: "Endpoint helper"`
Good: `description: "Use when adding/scaffolding a new FastAPI endpoint or route. Ensures Pydantic v2 validation, structured logging, OpenAPI docs, and a pytest test."`
