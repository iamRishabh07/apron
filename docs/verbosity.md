# Verbosity — Full Documentation

## What is Verbosity?

The verbosity category evaluates how efficiently and productively a response answers the prompt. It looks at the **length of the response**, keeping these topics in mind:

### Relevancy
- Is all of the information relevant to answering the prompt?
- Is there any information in the response that is not needed to answer the prompt?
- Is there any information that is missing that is needed to answer the prompt?

### Speed to the Answer
- Does the response begin answering the prompt quickly?
- Is there too much unnecessary information before the response answers the prompt?

### Repetition/Redundancy
- Does the response repeat information multiple times?
- Does the response contain redundant explanations and/or content?

### Focus/Intent
- Is the focus of the response on answering the prompt?
- Is the intent of all information present in the response to answer the prompt?

> Note: Do NOT penalize pleasantries here. Pleasantries are penalized under Writing Style and Tone.

---

## Rating Scale

| Rating | Label | Meaning |
|---|---|---|
| -2 | Too Short (Major Issue) | The response significantly lacks details and supporting content |
| -1 | Slightly Too Short | Minor lack of detail or completeness |
| 0 | Just Right (No Issue) | Well-structured, fits the required length, no unnecessary repetition, all relevant supporting content included, every sentence adds value |
| 1 | Slightly Too Long | Minor verbosity or unnecessary detail |
| 2 | Too Verbose (Major Issue) | Overly lengthy with repetition, irrelevant details, or unnecessary content that could be shortened without losing meaning |

---

## Mark as TOO SHORT when:
- The response is **truncated and cuts off before finishing**
- The response does not contain enough information to be helpful to the user

## Mark as TOO LONG when:
- The response contains **repeated** information, sentences, content, or explanations
- The response contains information that is **irrelevant** to answering the prompt
- The answer to the prompt is not given until the very end
- The focus of the response begins to **wander into other topics**

---

## Critical Rule: Truncated Responses

> **Any truncated response (cuts off before finishing) MUST ALWAYS be penalized under Verbosity as too short (-1 or -2).**

This is one of the most common errors in Apron Evals — raters see a truncated response and rate verbosity as "Just Right." This is always wrong.

### Truncation Also Affects Other Categories

A truncated response always triggers a Verbosity penalty. It may also trigger penalties in other categories:

| Secondary effect | When it applies |
|---|---|
| **Truthfulness** | Code is cut off → code won't run → TF issue |
| **Instruction Following** | Truncation causes a required part of the prompt to go unaddressed |

**Example:** Response to a prompt asking for two Python approaches — Response B starts Approach 2 but the code cuts off mid-block.
- Verbosity: Too Short (always)
- Truthfulness: Major Issue (truncated code doesn't run)
- IF: Major Issue (Approach 2 is incomplete — a key part of the prompt is missing)

---

## Too Long Example — Repetition After Code Block

**JS Repackaging App response:**
- Approach section describes all classes (Ingredient, Supplier, Order, etc.)
- Code block is provided
- Explanation section after the code **repeats the same class descriptions word-for-word** with no new context or additional information

**Correct verbosity rating: Too Long (-2)**

The response repeats information almost word for word before and after the code block with nothing new added. This is redundant and the response could be shortened without losing any meaning.

> Watch for responses that describe something before the code AND then re-explain the same thing after the code identically — that is always Too Long.

---

## The Movie App Example (Case Study)

**Prompt:** Build a movie management app in Python two different ways (CLI + JSON, and GUI with Tkinter).

**Response B (incorrect rating):** Starts both approaches but Approach 2 (Tkinter GUI) code is truncated — cuts off mid-block.

**What the rater did wrong:** Rated Verbosity = 0 (Just Right)

**Correct ratings:**
- Verbosity = -1 or -2 (Too Short) — response is truncated
- IF = 1 (Major Issue) — Tkinter GUI is incomplete, search by actor/year not implemented
- TF = 1 (Major Issue) — Tkinter code uses invalid Python (`nicht` instead of `not`), code won't run, truncation prevents execution
