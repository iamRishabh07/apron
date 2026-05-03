# Side-by-Side Rankings — Full Documentation

## What is Side-by-Side (SxS) Ranking?

The last section of each task is to compare Response A and Response B and choose which is better.

## The Two Parts of Your Rating

1. **Individual Scores** — Evaluate Response A and Response B separately using the overall scoring rubric:
   - [5] Perfect — No issues
   - [4] Good — 1 Minor Issue, or could be improved in ways not directly covered by dimensions
   - [3] Okay — 2 Minor Issues
   - [2] Bad — 1 Major Issue
   - [1] Horrible — 2 Major Issues

2. **Side-by-Side Rating** — A 1–7 scale (left to right, 4 being "No preference") where you declare which response you preferred overall:
   - A is much better → A
   - A is slightly better → a
   - No preference → –
   - B is slightly better → b
   - B is much better → B

---

## The Alignment Principle — Most Important Rule

> **Your final SxS preference rating must be a logical summary of your individual scores. It should NEVER contradict them.**

### Rule 1: Scores must match the SxS direction

If you rated Response A = 4 and Response B = 3, your SxS must favor A. There should be no contradictions between individual response ratings and the SxS ranking.

### Rule 2: Justification must support the ranking

If you rank Response A as the better response, your justification must explain why A is better. You cannot describe B as superior in your text and then click A as the winner.

---

## Common Errors

### Error 1: Score vs. Preference Contradiction
- **Scenario:** Rater gives A = 1, B = 2, then selects "A is much better" in SxS
- **Why it's wrong:** B scored higher. Selecting A as better directly contradicts the scores.

### Error 2: "No Preference" with a Clear Score Difference
- **Scenario:** A = 2, B = 3, rater selects "No preference" and then picks Response A to be used
- **Why it's wrong:** There IS a clear preference — B scored higher. Selecting no preference misrepresents the scores, and choosing A to be used contradicts B's higher score.

### Error 3: Justification Paradox
- **Scenario:** Rater writes "Response 2 is negligibly better than Response 1" in the justification, but then clicks Response A (Response 1) as the winner
- **Why it's wrong:** The justification explicitly says B is better, but the radio button says A. This is a direct self-contradiction.

---

## Case Studies

### Case Study 1: Caesar Cipher Task (Finland locale)
- Response A overall: 1 (Horrible)
- Response B overall: 2 (Bad)
- SxS chosen: **A is much better** ← ERROR

Correct SxS should favor B since B scored higher than A.

### Case Study 2: Hotel CSV Conversion Task
- Response A overall: 2 (Bad)
- Response B overall: 3 (Okay)
- SxS: "No preference" but Response A selected to be used ← ERROR
- Justification: "Response 2 is negligibly better than Response 1" ← this SUPPORTS B but the button selected A

Both the SxS rating and the response choice contradict the scores and the justification.

---

## Knowledge Check Example

**If Response A = 3 overall and Response B = 4 overall, which SxS is appropriate?**

| Option | SxS Slider | Justification | Appropriate? |
|---|---|---|---|
| A | B slightly better | B follows all prompt instructions; A only provided 3 test cases instead of 5 | ✓ Yes |
| B | B much better | B has fully functioning code; A has a runtime error | ✓ Yes |
| C | A slightly better | A's explanation is more helpful | ✗ No — contradicts scores (B=4 > A=3) |
| D | B slightly better | "Response A is better than B due to minor localization issue" | ✗ No — justification contradicts both slider and scores |

---

## Pre-Submission Checklist

Before submitting, always verify:
- [ ] The response with the higher overall score is also ranked higher in SxS
- [ ] Your justification describes why the ranked-higher response is better
- [ ] No part of your justification contradicts your SxS ranking choice
- [ ] If scores are equal, "No preference" is appropriate
