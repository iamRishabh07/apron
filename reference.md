# Eval Quick Reference — Apron Evals

## Task Input Structure (in order)

| Component | Required | Notes |
|---|---|---|
| System Prompt | Optional | Sets AI behavior/persona |
| Conversation History | Optional | Up to 6 prior turns |
| User Prompt | Always | May include reference text |
| Two model responses | Always | Pick the better one |

## Evaluation Steps

1. Read the System Prompt (if present) — understand the AI's role/constraints
2. Read the Conversation History (if present) — treat it as your own prior context
3. Read the User Prompt — this is what you're evaluating against
4. Evaluate Response A and Response B against the full context
5. Identify issues in each response
6. State which response you prefer and explain why

## Rating Rules

- Only evaluate the **latest User Prompt turn** — not prior turns in history
- Always use **full context** (System Prompt + History + User Prompt) when judging
- System prompts are typically 2–5 lines; follow them strictly when present
- Conversation History may be absent — tasks can start fresh
- Task categories vary by batch (coding, writing, reasoning, and more)
- Reference text may appear in the User Prompt regardless of whether a System Prompt is present

## Truthfulness (TF) — What to Check

TF evaluates whether claims are accurate AND code runs AND produces correct output with the given data.

**Always test code against the exact input provided in the prompt. Check:**
1. Does it run without errors?
2. Does it produce the **correct output** with the given data?
3. Are quirks in the provided data handled? (e.g., spaces in CSV column names, encoding)

> Running without errors is NOT enough — the output must be correct.

**TF is NOT measured** if the code requires a large external program, file, or API not provided in the prompt.

| Rating | Meaning |
|---|---|
| 1 — Major | Significant factual/code inaccuracies |
| 2 — Minor | Some factual/code inaccuracies |
| 3 — No Issue | Completely accurate, correct output |

## IF vs TF — Key Distinction

**IF (Instruction Following)** — Did the response attempt to follow instructions?
- Penalize only when response **ignores or goes against** a prompt instruction
- Attempting but doing it wrong = NOT an IF issue

**TF (Truthfulness)** — Did the response accurately fulfill the prompt?
- Penalize when output is wrong, code logic is broken, or claims are false

| Scenario | IF | TF |
|---|---|---|
| Attempts CSV→JSON but merges data incorrectly | No Issue | Major Issue |
| Finds average manually but uses `*=` instead of `+=` | No Issue | Major Issue |
| Uses `sum()` and `len()` despite "no built-ins" rule | Major Issue | No Issue |
| Prompt says Python, gives Java (acknowledges prompt) | No Issue | Major Issue |
| Ignores part of prompt entirely (no mention of it) | Issue | — |

> Truthfulness is evaluated based on how well the response **understood the prompt** — not external real-world accuracy.

**The two evaluation questions — ask these for every potential IF issue:**
1. Does the response **acknowledge or mention** the prompt request/constraint?
2. Does the response **attempt to fulfill** the prompt request/constraint?

> **"No" to both** → IF issue. **"Yes" to either** → NOT an IF issue (it's TF).

**Rater self-check:** If your IF justification mentions "accuracy," "incorrect data," or "wrong output" — that's TF, not IF.

## Justification Rules

- Two previous justifications are shown — use them as reference only
- Submit **ONE single, cohesive block of text** as your final justification
- NEVER submit both previous justifications (even separated by a line or space)
- **Option 1:** Pick the stronger justification, edit and refine it
- **Option 2:** Delete both and write your own from scratch
- Final text must read as one clear and complete argument

## Style and Clarity — What Belongs Here

**Penalize S&C for:** code not in code block, long text blocks, pleasantries, missing code comments, non-meaningful/inconsistent variable/function names, poor structure.

**Do NOT penalize S&C for:** code bugs (TF), wrong output (TF), missing explanations (IF/Verbosity), response length (Verbosity), accuracy of any claims (TF).

**`<turn_end>` at end of response** = system bug, ignore completely, penalize nothing.

Full details: `docs/style-and-clarity.md`

## Verbosity — Rating Scale & Key Rules

| Rating | Label | When to use |
|---|---|---|
| -2 | Too Short | Significantly lacks detail; truncated response |
| -1 | Slightly Too Short | Minor lack of detail or completeness |
| 0 | Just Right | Appropriate length, no repetition, all relevant content |
| 1 | Slightly Too Long | Minor unnecessary detail |
| 2 | Too Verbose | Repetitive, irrelevant, or wandering content |

**Truncated responses — ALWAYS penalize as Too Short (-1 or -2). No exceptions.**

Truncation also triggers:
- **TF** if the cut-off code won't run
- **IF** if a required part of the prompt is left unaddressed

Full details: `docs/verbosity.md`

## Localization — Key Rules

- Match the **prompt's locale**, not the task's assigned locale parameter
- Code/data locale in response should match code/data locale in the prompt
- Penalize cultural mismatches (wrong units, wrong currency) unless the prompt asks for them
- **Arabic only:** MSA is always acceptable — never penalize for it

| Scenario | Penalize? |
|---|---|
| Response matches prompt locale (even if differs from task locale) | No |
| Wrong units for locale (miles instead of km) | Yes |
| Wrong currency for locale | Yes |
| Arabic response uses MSA | No |

Full details: `docs/localization.md`

## Common Rater Errors to Avoid

- **Misreading the prompt** — Always read the prompt precisely before rating IF. Example: "select top 5 movies, return sorted by genre" means top 5 overall + sort output. It does NOT mean top 5 per genre.
- **Submitting two justifications** — Never leave both previous justifications in the box
- **Combining justifications with a separator** — A `---` line still counts as two separate justifications
- **Rating history turns** — Only evaluate the latest User Prompt turn

Full examples: `docs/common-errors.md`

## Common FAQs

**Can tasks have no System Prompt?** Yes.

**Can tasks have no Conversation History?** Yes.

**Should I evaluate responses in the Conversation History?** No — only the latest turn.

**Can a task have both a System Prompt and Conversation History?** Yes.

**Will there always be a User Prompt?** Yes, always.

**Is Truthfulness about real-world accuracy?** No — it's about how well the response understood and fulfilled the prompt.
