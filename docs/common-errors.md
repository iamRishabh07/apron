# Common Errors — Apron Evals

This section covers common errors seen in tasks on the Apron Evals project.

## Error Categories

1. Instruction Following Ratings
2. Truthfulness Ratings
3. Instruction Following vs Truthfulness
4. Verbosity Ratings
5. Style and Clarity Ratings
6. Side-by-Side Ratings

---

## 1. Instruction Following Ratings

The Instruction Following (IF) category evaluates how thoroughly the model response pays attention to the prompt and its instructions, and how well it **ATTEMPTS** to follow them.

### When to Penalize IF

Only penalize IF when the model:
1. **Ignores** a prompt instruction
2. **Fails to attempt** to follow a prompt instruction

### When NOT to Penalize IF

Do NOT penalize IF when the response:
1. Acknowledges the prompt instructions, requests, and requirements
2. Mentions the prompt instructions, requests, and requirements
3. **Attempts** to follow the prompt's instructions — even if it does so inaccurately (inaccurate execution = TF issue, not IF)

### Example — CSV to JSON

**Prompt:** "Convert the following csv file into JSON format:"
```
product_name,id,quantity
product_1,001,23
product_2,002,8
product_3,003,16
```

**Response:** Produces JSON but with wrong values (wrong product names, IDs, quantities).

**Verdict:** **TF issue only — NO IF issue.**
The response understands what the prompt is asking (convert CSV to JSON) and attempts to do it. The incorrect values are a Truthfulness problem, not an Instruction Following problem.

### Example — Wrong Column Name (IF Issue)

**Prompt:** "Create a csv file with the columns 'Country, Population, GDP'. Generate 5 rows."

| Response | Columns Used | Verdict |
|---|---|---|
| A | Country, Population, GDP | No IF issue (data may have TF issues) |
| B | Country, Population, GDP | No IF issue |
| C | Country, Population, GDP | No IF issue |
| D | Country, Population, **AGI** | **IF issue** — replaced GDP with AGI, ignoring the column name instruction |

Response D has an IF issue because it replaced `GDP` with `AGI` — a direct failure to follow the column name instruction.



### Common Error: Misreading the Prompt

The most dangerous IF error is when the **rater** misunderstands the prompt and incorrectly flags a correct response as having an issue.

#### Example — Movie Ratings Task

**Prompt (key section):**
> "This function should take a user ID as input, select the **five highest-rated movies** from the user's viewing history, and **return an array sorted by genre frequency**."

**What the response did:**
```sql
SELECT movie_title, genre, rating
FROM watch_history
WHERE user_id = ?
ORDER BY rating DESC LIMIT 5
```
Then sorted results by genre frequency.

**Incorrect rater verdict:** Major Issue (IF = 1)
> "This response selects only the top 5 from the entire record due to ORDER BY rating DESC LIMIT 5. According to the prompt, it should select the top 5 highest-rated movies from each genre."

**Why this verdict is WRONG:**
The rater misread the prompt. The prompt asks for:
- Top 5 highest-rated movies **overall** (from the user's viewing history)
- Then **return the array sorted by genre frequency**

The genre sorting applies to the **output format**, not the selection criteria. The response correctly selects top 5 overall with `ORDER BY rating DESC LIMIT 5` and then sorts by genre. This is **No Issue** — not a Major Issue.

**Correct verdict:** No Issue (3)

### Key Lesson

> Before rating Instruction Following, **read the prompt carefully and precisely**. Misreading the prompt leads to incorrectly penalizing correct responses. The genre part of this prompt describes the sort order of the returned array — it does NOT mean "top 5 per genre."

---

## Rating Scale Reference (IF)

| Rating | Meaning |
|---|---|
| 1 — Major Issue | Response fails to follow a core instruction |
| 2 — Minor Issue | Response partially follows instructions with small gaps |
| 3 — No Issue | Response correctly follows all instructions |

---

## 3. Instruction Following vs Truthfulness (Most Common Error)

This is the single biggest error seen in Apron Evals. Raters confuse IF and TF and end up marking issues in the wrong category.

### The Rule in One Sentence

> If the response **acknowledges and attempts** the prompt → no IF issues, even if the output is wrong. Wrong output = **TF**.

### The Self-Check

If you're about to mark an IF issue and your justification mentions "accuracy," "incorrect data," or "wrong output" — **stop**. That's a TF issue.

### Case Study: CSV to JSON

**What the rater wrote under IF:**
> "The response incorrectly grouped rows from the CSV by merging separate department records... causing data inaccuracies."

**Why it's wrong:** This describes an *accuracy* problem. The response attempted to convert the CSV to JSON (IF = No Issue). The merging error is a Truthfulness issue.

**Correct ratings:** IF = 3 (No Issue), TF = 1 (Major Issue)

### Case Study: Find Average Function

**Prompt:** Find the average manually. Do not use built-in methods.

| Response | What it did | IF | TF |
|---|---|---|---|
| A | Manual loop but `sum *= num` instead of `sum += num` | No Issue (attempted manually) | Major Issue (wrong output) |
| B | `return sum(numbers) / len(numbers)` | Major Issue (used built-ins, ignored constraint) | No Issue (output is correct) |

---

## 2. Truthfulness Ratings

**Definition:** The extent to which the claims in the response are truthful and correct, and the code is **executable AND produces correct outputs**.

> Output correctness may not be measured if the code only functions when embedded inside a large, complex program that is not provided, or if it requires an external file/API dependency that is not provided.

### Rating Scale (TF)

| Rating | Meaning |
|---|---|
| 1 — Major Issues | Response contains significant factual and contextual inaccuracies |
| 2 — Minor Issues | Response contains some factual and contextual inaccuracies |
| 3 — No Issue | Response is completely accurate and aligned with the reference text |

### Common Error: Assuming Code is Correct Without Testing

**The mistake:** Rater sees code that looks reasonable, rates TF = 3 (No Issue) without actually running it against the data provided in the prompt.

#### Example — Book Orders CSV Task

**Task:** Read a CSV of book orders, accumulate quantities per book, output a new CSV with `bookName` and `totalQuantity` columns.

**CSV provided in prompt:**
```
order_id, book_id, quantity
1, 101, 1
2, 102, 1
3, 101, 1
4, 102, 2
```

**Incorrect rater verdict:** TF = 3 (No Issue)
> "The Python code is correct and functional. The logic is sound and will produce the expected output."

**Why this is WRONG:**
The CSV has **spaces after the commas** in the column names (`order_id, book_id, quantity`). When the code reads this file, the column names include leading spaces (` book_id`, ` quantity`). The code then fails to match columns correctly and outputs only the header row with no data.

The code **runs** but does **not produce the expected output**. This is a TF issue.

**Correct verdict:** TF = Major Issue (1) or Minor Issue (2) depending on severity.

### Key Lesson: Running ≠ Correct

> The code must not only **run** — it must produce the **exact expected output** when tested with the data provided in the prompt.

Always test the code using the exact input from the prompt. Check:
- Does it run without errors?
- Does it produce the correct output with the given data?
- Are edge cases in the provided data handled (e.g., spaces in column names, encoding, etc.)?
