# GitHub Copilot Workshop — Agent Mode & Agent Skills

**Duration:** 20 minutes
**Audience:** Developers familiar with GitHub Copilot chat / inline completions
**Goal:** Leave knowing the difference between Ask, Plan, and Agent mode, how to drive Agent mode effectively, and how to package reusable workflows as **Skills**, **Instructions**, and **Prompts**.

---

## Agenda (20 min)

| Time | Section | What happens |
|------|---------|--------------|
| 0:00–2:00 | **Framing** | Modes overview: Ask vs Plan vs Agent. When to reach for which. |
| 2:00–6:00 | **Demo 1 — Agent mode** | Use Agent mode to fix a bug + add a test in `demo/` end-to-end. |
| 6:00–9:00 | **Demo 2 — Plan mode** | Use Plan mode to scope a larger change before any code is written. |
| 9:00–11:00 | **Customization layers** | `copilot-instructions.md`, `*.instructions.md`, `*.prompt.md`, Skills. |
| 11:00–16:00 | **Demo 3 — Skills in action** | Trigger the `pydantic-endpoint` skill to scaffold a compliant FastAPI endpoint. |
| 16:00–18:00 | **Hands-on** | Attendees follow the [attendee guide](attendee-guide.md). |
| 18:00–20:00 | **Q&A + takeaways** | Cheat sheet handout. |

---

## 1. Modes in 60 seconds

- **Ask** — Read-only Q&A about your code. No file edits.
- **Plan** — Read-only *planning*. GitHub Copilot investigates the codebase and produces a concrete, file-by-file plan you can review before any edits happen.
- **Agent** — GitHub Copilot picks the files, runs tools (search, terminal, tests), and iterates until the task is done. You approve actions.

> Rule of thumb: **Ask** to learn, **Plan** to scope, **Agent** to do.

## 2. What makes Agent mode powerful

1. **Tool use** — searches the workspace, reads/edits files, runs the terminal, checks errors.
2. **Iteration loop** — runs tests, sees failures, fixes, re-runs.
3. **Customization** — instructions and skills steer behavior repeatably.

## 3. Customization cheat sheet

| File | Scope | When applied | Use for |
|------|-------|--------------|---------|
| `.github/copilot-instructions.md` | Whole repo | Every request | Standards, security rules, stack conventions |
| `*.instructions.md` (with `applyTo`) | Glob-matched files | When matching files are in context | Per-language / per-folder rules |
| `*.prompt.md` | On-demand | User runs `/prompt-name` | Reusable canned tasks (e.g. "scaffold endpoint") |
| `SKILL.md` (in a skill folder) | On-demand, semantic | Agent loads when description matches | Multi-step expert workflows |

### Skills vs Prompts (the most-asked question)
- **Prompt** = parameterized macro. Runs when *you* invoke it.
- **Skill** = packaged expertise the **agent** decides to load when the task description matches `SKILL.md`'s `description`. Better for "always do X this way."

## 4. Live demo paths

- Demo 1 (Agent fixes bug): [demo/buggy_math.py](demo/buggy_math.py)
- Demo 2 (Plan scopes a change): same `demo/` folder — see [facilitator.md](facilitator.md)
- Demo 3 (Skill scaffolds endpoint): [.github/skills/pydantic-endpoint/SKILL.md](../.github/skills/pydantic-endpoint/SKILL.md)
- Repo standards in effect: [.github/copilot-instructions.md](../.github/copilot-instructions.md)
- Reusable prompt: [.github/prompts/add-endpoint.prompt.md](../.github/prompts/add-endpoint.prompt.md)
- Attendee hands-on guide: [attendee-guide.md](attendee-guide.md)

## 5. Facilitator script

See [facilitator.md](facilitator.md) for line-by-line talk track and the exact prompts to paste.

## 6. Takeaways

1. Agent mode = autonomous loop with tools. Approve, don't micromanage.
2. Push standards into `copilot-instructions.md` once — every request inherits them.
3. Package repeated multi-step workflows as **Skills**; package one-shot canned tasks as **Prompts**.
4. Keep instruction files **short and specific**. They go into every prompt's context.
