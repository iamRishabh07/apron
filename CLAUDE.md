# Apron Evals — Outlier Annotation Project

## Project Overview

This is a personal workspace for Outlier's Apron Evals annotation project. The work involves evaluating pairs of AI model responses by comparing them against a System Prompt, Conversation History, and User Prompt, then selecting the better response with a single, cohesive justification.

## Folder Structure

```
Apron Evals/
├── CLAUDE.md                          # This file — project overview and eval rules
├── reference.md                       # Quick-reference cheat sheet for all eval rules
├── docs/                              # Full raw documentation by section
│   ├── system-prompts.md              # System Prompts section docs
│   ├── conversation-history.md        # Conversation History section docs
│   ├── task-structure.md              # Task Structure and evaluation flow docs
│   ├── rating-guidelines.md           # How to rate — examples and truthfulness caveat
│   ├── if-vs-tf.md                    # IF vs TF distinction with decision examples
│   ├── justification-guidelines.md   # How to write the final justification
│   ├── common-errors.md              # Common rater errors and how to avoid them
│   ├── localization.md               # Localization category rules and common errors
│   ├── verbosity.md                  # Verbosity rating scale, truncation rules, and examples
│   └── style-and-clarity.md          # Style and Clarity category rules and what NOT to penalize here
├── examples/                          # Saved task examples organized by category
│   ├── coding/
│   ├── writing/
│   └── reasoning/
├── notes/                             # Free-form personal notes from sessions
└── templates/                         # Reusable eval checklists and templates
```

## Evaluation Workflow

Each task follows this structure (components are optional depending on the task):

1. **System Prompt** (if present) — defines the AI's behavior/persona for the task
2. **Conversation History** (if present) — prior user–assistant turns (up to 6 turns)
3. **User Prompt** — the current message to evaluate against (may include reference text)
4. **Two model responses** — evaluate both, then pick the better one with a single justification

## Core Eval Rules

### What to evaluate
- Use the **full context**: System Prompt + Conversation History + User Prompt
- Only evaluate the **latest turn** (the User Prompt) — do NOT re-evaluate responses in the Conversation History
- Determine whether each response has issues, then state which you prefer and why

### Task structure rules
- Tasks may or may not include a System Prompt
- A User Prompt is **always** present in every task
- Conversation History may have 0–6 prior turns
- Tasks may combine a System Prompt AND Conversation History
- Task categories vary by batch (coding, writing, reasoning, etc.)

### System Prompt rules
- System prompts define behavior, persona, capabilities, and constraints
- They are typically 2–5 lines — direct and to the point
- Treat them as the AI's operating instructions when evaluating responses

### Conversation History rules
- Act as if you've been part of the ongoing conversation
- Use history as essential context — carry it forward when evaluating
- Only the **latest User Prompt** is the target of evaluation

## IF vs TF — Key Distinction

**IF (Instruction Following):** Response omitted or ignored part of the prompt — no accuracy problem, just missed instruction.

**TF (Truthfulness):** Response acknowledged the prompt but fulfilled it incorrectly (wrong language, wrong output, code errors, false statements).

> Truthfulness is based on how well the response **understood the prompt** — not external real-world accuracy.

## Justification Rules

- Two previous justifications are shown as reference only
- Submit **ONE single, cohesive block of text** — never submit both separated by a line
- Either edit/refine the stronger previous justification, or write a new one from scratch

## Key Reference Files

- Full guidelines: `docs/system-prompts.md`, `docs/conversation-history.md`, `docs/task-structure.md`
- Rating examples and truthfulness caveat: `docs/rating-guidelines.md`
- IF vs TF decision guide: `docs/if-vs-tf.md`
- Justification rules: `docs/justification-guidelines.md`
- Common rater errors: `docs/common-errors.md`
- Quick rules summary: `reference.md`
- Saved examples by category: `examples/coding/`, `examples/writing/`, `examples/reasoning/`
