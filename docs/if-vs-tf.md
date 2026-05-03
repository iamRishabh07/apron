# IF vs TF — Instruction Following vs Truthfulness

## Core Definitions

**Instruction Following (IF)**
About whether the response **attempts** to follow the prompt's instructions.
- Penalize only when the response **ignores** or **goes against** a prompt instruction
- If the response acknowledges and attempts to follow the instructions — even inaccurately — there are **no IF issues**

**Truthfulness (TF)**
About how **accurately** the response answers the prompt.
- Covers false statements, incorrect code logic, wrong output, code that doesn't run
- Penalize when the response tries but gets something factually or technically wrong

> Key caveat: Truthfulness is evaluated based on how well the response **understood and fulfilled the prompt** — not external real-world accuracy.

---

## The Critical Rule

> If a response **acknowledges and attempts** to follow the prompt instructions, there are **no IF issues** — even if the output is wrong.
> Wrong output = **TF issue**, not IF.

---

## Decision Examples

All examples use: **Prompt: "Provide Python code that does abc."**

| Response | Verdict | Reason |
|---|---|---|
| "Here is Python code that does abc" + [Java code that does abc] | **TF only** | Acknowledged prompt, fulfilled with wrong language |
| "Here is Python code that does abc" + [Python code that does xyz] | **TF only** | Acknowledged prompt, wrong output |
| "Here is Python code that does abc" + [Python code that does ab] | **TF only** | Acknowledged prompt, incomplete output |
| [Python code that does ab, no mention of 'c'] | **IF only** | Never addressed 'c' — omission, no accuracy issue |

---

## Critical Rule: Attempting ≠ IF Issue

If a response **attempts** to follow the prompt's instructions — even inaccurately — that is **NOT** an IF issue. Inaccurate execution is a **TF issue**.

**Example:** Prompt says convert CSV to JSON. Response produces JSON but with wrong values.
- IF rating: No Issue (it attempted to follow the instruction)
- TF rating: Issue (the output values are wrong)

Only penalize IF when the response **ignores** or **fails to attempt** an instruction entirely.

---

## Case Studies

### Case 1 — CSV to JSON Conversion

**Prompt:** Convert financial CSV data (departments, budgets, expenses, branches) into JSON format.

**Response:** Produces JSON with department and branch structure, but incorrectly merges separate department rows.

**Incorrect rater verdict:** IF = 1 (Major Issue)
> "The response incorrectly grouped rows from the CSV by merging separate department records and their associated branches, which does not accurately reflect the original CSV data structure, causing data inaccuracies."

**Why this is WRONG:**
The justification describes an *accuracy* problem — that is a Truthfulness issue, not IF. The response acknowledged the request to convert CSV to JSON and attempted it. There are no IF issues.

**Correct verdict:**
- IF = 3 (No Issue) — response understood and attempted the conversion
- TF = 1 (Major Issue) — the data was incorrectly merged/structured

---

### Case 2 — Python "Find Average" Function

**Prompt:** "Write a Python function that finds the average of a list of numbers. **Do not use any tools, libraries, or built-in methods. Do all calculations manually.**"

---

**Response A:**
```python
def find_avg(num_list):
    sum = 0
    count = 0
    for num in num_list:
        sum *= num      # BUG: should be sum += num
        count += 1
    return 0 if count == 0 else sum / count
```

**Verdict:**
- **IF = No Issues** — The response does not use any built-in methods. It attempts to find the average manually. It is trying to do what the prompt asks.
- **TF = Major Issues** — The logic is incorrect (`*=` instead of `+=`). The output will be wrong.

---

**Response B:**
```python
def find_avg(num_list):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
```

**Verdict:**
- **IF = Major Issues** — The response uses `sum()` and `len()`, which are built-in methods. The prompt explicitly said not to use them. This ignores a direct prompt constraint.
- **TF = No Issues** — The logic is correct. The output is accurate.

---

## Key Takeaways

| Principle | Detail |
|---|---|
| **Attempt = IF success** | If model acknowledges and tries to follow all parts of the prompt, IF = No Issues regardless of output correctness |
| **Negative constraints are critical** | IF failures most often occur when a model ignores a "do not" instruction (e.g., "do not use libraries") |
| **Logic vs Intent** | TF = quality of the result; IF = whether the task structure was followed |
| **Self-check for raters** | If your IF justification mentions "accuracy" or "incorrect data" — you are likely rating the wrong category. That's TF. |

---

---

## When to Penalize Each Category

### Penalize IF when:
1. The response **ignores** a prompt request (does not mention, acknowledge, or attempt to fulfill it)
2. The response **misunderstands or misinterprets** a prompt instruction

### Penalize TF when:
1. The attempt to follow the prompt **fails to produce the correct result or output**
2. The response contains a **factually inaccurate claim**
3. The **code does not run**, or produces the wrong output
4. The **final answer** to the prompt is incorrect or wrong
5. The **solution or answer given is incorrect**

### Do NOT penalize IF when:
- The response acknowledges the prompt instructions, requests, and requirements
- The response mentions the prompt instructions, requests, and requirements
- The response attempts to follow the prompt — even if it does so inaccurately

---

## The Two Evaluation Questions

Use these two questions to determine if an issue is IF or TF:

1. **Does the response acknowledge or mention the prompt request, requirement, or constraint?**
2. **Does the response attempt to fulfill the prompt request, requirement, or constraint?**

> If you can answer **"No" to both** → it IS an IF issue.
> If you can answer **"Yes" to one or both** → it is **NOT** an IF issue (it's TF).

---

## Full Examples

### Example 1 — NO IF Issue (OOP Inventory Program)

**Prompt:** "Write a Python program that allows me to keep track of inventory for my store. The program should follow OOP practices and allow me to add, delete, and update products. Each product should have a name, id, price, and quantity."

**Response:** Produces functional Python code using functions and type aliases (not OOP), but says: *"This code follows Object Oriented Programming practices."*

**Evaluation questions:**
- Does the response mention or acknowledge following OOP practices? **Yes**
- Does the response attempt to follow OOP practices? **No**

Since we answered "Yes" to one question → **NOT an IF issue**.

**Verdict:**
- IF = No Issue — the response acknowledged the OOP requirement
- TF = Major Issue — the code uses functional programming, not OOP; the claim that it follows OOP is false

---

### Example 2 — IF Issue (Student Grades CSV)

**Prompt:** "Create a csv file to help me keep track of student grades. Headers: 'Student Name', 'Subject', 'Assignment Date', 'Grade'. Create **5 rows** of example data."

**Response:** Produces the CSV with correct headers but only **3 rows** of data. The response never mentions or acknowledges the 5-row requirement.

**Evaluation questions:**
- Does the response mention or acknowledge the request to create 5 rows? **No**
- Does the response attempt to create 5 rows? **No**

Both answers are "No" → **IF issue**.

**Verdict:**
- IF = Major Issue — the response completely ignored the 5-row instruction
- TF = No Issue — the data provided is accurate

---

## Rater Self-Check

Before submitting an IF issue, ask yourself:
> "Is the response **ignoring or going against** a prompt instruction — or is it just doing it **incorrectly**?"

- Ignoring / going against → **IF issue**
- Doing it incorrectly → **TF issue**

If your justification for an IF issue talks about accuracy, wrong data, or incorrect output — **stop and reconsider**. That belongs under Truthfulness.
