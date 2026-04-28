# Attendee Guide — Copilot Workshop

Follow these three short steps. Total time: ~5 minutes.

## Before you start
- Open this repo in VS Code.
- Open the Copilot Chat panel (Ctrl/Cmd+Alt+I).
- Find the **mode picker** at the bottom of the chat input. You should see **Ask**, **Plan**, and **Agent**.

---

## Step 1 — Ask mode (understand)

Switch to **Ask** mode. Paste:

```
What standards does this repo enforce on Copilot, and where are they defined?
```

You should see Copilot summarize [.github/copilot-instructions.md](../.github/copilot-instructions.md) and reference the python instructions and the `pydantic-endpoint` skill. No files are edited.

---

## Step 2 — Plan mode (scope before doing)

Switch to **Plan** mode. Paste:

```
Plan how to add a /health endpoint to this repo that returns
{"status": "ok"}, with a pytest test. Do not write code yet.
```

You should get a numbered plan listing the files it would create or change. Skim it.

> No diffs appeared. That's the point of Plan mode.

---

## Step 3 — Agent mode (do it, with a skill)

Switch to **Agent** mode. Paste:

```
Add a /health endpoint with a pytest test, following our standards.
```

Watch for:
1. The agent loads the **`pydantic-endpoint`** skill (you'll see it referenced in the chat).
2. It creates a router file, request/response models, the handler, and a test under `tests/`.
3. It runs the tests in the terminal. Approve the run.
4. If a test fails, it iterates until green.

When it finishes, open the diff and check:
- Pydantic v2 models with field constraints (`max_length`, etc.)
- An OpenAPI `summary` and `description` on the route.
- A test that covers the happy path **and** a 422 validation failure.
- No `print` statements anywhere.

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| No mode picker visible | Update the Copilot Chat extension. |
| Plan mode tries to edit | You're in Agent mode \u2014 check the picker. |
| Skill didn't load | Reword your prompt to mention "endpoint" or "route" explicitly. |
| Test run not offered | Tell it: "run the tests in the terminal." |
| Output doesn't match standards | Open [.github/copilot-instructions.md](../.github/copilot-instructions.md) and confirm it's not empty. |

---

## What to take home

- **Ask** \u2192 learn. **Plan** \u2192 scope. **Agent** \u2192 do.
- The repo's standards live in [.github/copilot-instructions.md](../.github/copilot-instructions.md) and apply to **every** request.
- The [.github/skills/pydantic-endpoint/SKILL.md](../.github/skills/pydantic-endpoint/SKILL.md) skill loads automatically because its `description` matches "add an endpoint" tasks.
- See [cheatsheet.md](cheatsheet.md) for the one-page summary.
