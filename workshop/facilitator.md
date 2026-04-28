# Facilitator Script — 20 min

> Times are cumulative. Keep transitions tight; demos are the value.

## 0:00 — Open (30s)
> "By the end of this 20 minutes you'll know when to use Ask, Plan, and Agent mode, how to keep Agent on the rails with instructions, and how to package reusable expertise as Skills."

## 0:30 — Modes whiteboard (90s)
Draw three boxes: **Ask | Plan | Agent**.
- Ask = read-only Q&A.
- Plan = read-only *planning* — produces a file-by-file plan, no edits.
- Agent = chooses files, edits them, runs tools, iterates.

Key line:
> "Plan thinks. Agent does. Ask explains. Use Plan before Agent on anything you couldn't undo with `git checkout`."

---

## 2:00 — DEMO 1: Agent fixes a bug + writes a test (4 min)

**Setup (already on screen):** [workshop/demo/buggy_math.py](demo/buggy_math.py) open. Terminal visible.

1. Switch chat to **Agent** mode. Show the picker.
2. Paste this prompt verbatim:

```
The function average() in workshop/demo/buggy_math.py has a bug.
Find it, fix it, and add a pytest test in workshop/demo/test_buggy_math.py
covering the bug plus an empty-list edge case. Run the tests and make
sure they pass.
```

3. **Narrate the loop as it runs:**
   - "It's reading the file." (file read tool)
   - "Notice it didn't ask me which file — semantic search found it."
   - "It's running pytest in the terminal — I have to approve."
   - "Test failed → it's iterating. This is the agent loop."

4. When green, point at the diff and say:
> "I never typed a line of code. I approved tool calls."

**Talking points to drop in:**
- Approve scope: "always allow in this workspace" for safe tools.
- Stop button if it goes off track.
- Checkpoints / undo.

---

## 6:00 — DEMO 2: Plan mode scopes a change (3 min)

**Setup:** still in `workshop/demo/`. Switch chat to **Plan** mode.

Paste:

```
I want to extract the math helpers in workshop/demo/buggy_math.py
into a small package with separate modules for stats and validation,
and keep all current behavior. Produce a plan, don't change anything yet.
```

**Narrate:**
- "Notice no diffs appear — Plan mode can't edit files."
- "It's investigating: reading files, listing the folder."
- "It comes back with a numbered, file-by-file plan I can edit."

Then show the handoff:
> "When the plan looks right, I switch to Agent and say *'execute the plan above'*. Plan + Agent is the safest pattern for non-trivial work."

Key line:
> "Plan mode is your code review *before* the code exists."

---

## 9:00 — Customization layers (2 min)

Open [.github/copilot-instructions.md](../.github/copilot-instructions.md).
> "Every request to Copilot in this repo carries these rules. Pydantic v2, structured logging, non-root Dockerfiles. I don't have to repeat them."

Open [.github/instructions/python.instructions.md](../.github/instructions/python.instructions.md).
> "Scoped via `applyTo` — only attached when Python files are in context."

Open [.github/prompts/add-endpoint.prompt.md](../.github/prompts/add-endpoint.prompt.md).
> "A prompt is a macro. I run it with `/add-endpoint`."

Open [.github/skills/pydantic-endpoint/SKILL.md](../.github/skills/pydantic-endpoint/SKILL.md).
> "A skill is different. The **agent** decides to load it when my task matches the description. I don't invoke it by name."

Single-slide mental model:
- **Instructions** = always-on rules.
- **Prompts** = on-demand macros (you trigger).
- **Skills** = on-demand expertise (agent triggers).

---

## 11:00 — DEMO 3: Skill drives a scaffold (5 min)

Still in **Agent** mode. Paste:

```
Add a new POST /quotes endpoint that accepts a customer ID and a
list of coverage codes, validates them, and returns a stub quote.
Follow our standards.
```

**Narrate:**
- "Watch the chat — it's loading the `pydantic-endpoint` skill because the description matches."
- Point out that it follows the skill's checklist: Pydantic v2 model, size limits, structured log, test file, no print statements.
- Open the generated test file to show the test was written too.

> "The skill is the difference between 'an endpoint' and 'an endpoint that passes our security review.'"

---

## 16:00 — Hands-on (2 min)

Point attendees at [attendee-guide.md](attendee-guide.md). They run through the three short steps (Ask → Plan → Agent + skill).

---

## 18:00 — Q&A + close (2 min)

Likely questions + crisp answers:

- **"When should I use Plan vs Agent?"**
  Plan when the change touches many files, is architectural, or you want a review gate. Agent when the scope is clear and contained.

- **"When should I write a Skill vs a Prompt?"**
  Repeat-this-exact-task → Prompt. Express-domain-expertise-the-agent-should-apply-when-relevant → Skill.

- **"Will Agent mode push to main?"**
  No. Destructive/shared actions require explicit approval; default is local + reversible.

- **"How do I stop it from over-editing?"**
  Tighten `copilot-instructions.md` ("don't refactor unrelated code"). Scope your prompt to specific files, and reject diffs that go beyond what you asked for.

- **"Can skills call other skills?"**
  Yes — skills can reference other skills in their instructions; the agent will load them as needed.

Close:
> "One repo-level instructions file, one skill per workflow you keep redoing. That's 80% of the value."
