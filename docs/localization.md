# Localization — Full Documentation

## What is Localization?

The localization category covers how well the response adheres to the appropriate language and culture for each task.

## What to Look For

- The locale in the response matches the locale in the prompt
- Grammar, spelling, wording, and phrasing are appropriate for the locale; if it contains multiple words in other languages, it should be flagged
- Formats, dates, units of measurement, etc. are appropriate for the locale
- Cultural references are appropriate for the locale

## Rating Scale

| Rating | Meaning |
|---|---|
| 1 — Major Issues | Response is in a completely different language than expected or fully aligned with a different dialect from another locale |
| 2 — Minor Issues | Response contains a few minor issues such as words typically not used in the locale, spellings typical of other dialects, etc. |
| 3 — No Issues | The language used in the response perfectly aligns with what a native speaker would use |

---

## Common Errors and How to Avoid Them

### 1. Match the Prompt's Locale, Not the Task's Locale Parameter

The locale of the response should match the locale of the **prompt**, even if it doesn't match the locale parameter assigned to the task.

> Do NOT penalize a response for not matching the task's locale if it matches the locale of the prompt.

**Example:** Task is assigned `hi_IN` locale, but the prompt is written in `hi_Latn` and the response is also in `hi_Latn` → **No localization issue**. The response matches the prompt.

### 2. Code/Data Locale Follows the Prompt's Code/Data

If the prompt gives code or data as an example, and the response also gives code or data, the locale of that code/data in the response should match the locale of the code/data given in the prompt as an example.

> Do NOT penalize a response when it is matching the prompt.

### 3. Cultural Mismatches Must Be Penalized

Watch out for mismatches in cultural references. Penalize all cultural mismatches **unless they are specifically asked for in the prompt**.

**Examples of cultural mismatches:**
- Response uses **miles** as a unit of measurement, but the assigned locale typically uses **kilometers** → localization issue
- Response uses **USD** as the currency, but the assigned locale has a different currency → localization issue

### 4. Arabic Locales — MSA Exception

**FOR ARABIC LOCALES ONLY:** It is acceptable to use MSA (Modern Standard Arabic) in the response, even if the prompt is in `ar_EG` or `ar_SA`.

> Do NOT penalize a response for using MSA in the response, regardless of whether or not it is matching the prompt.

---

## Quick Decision Guide

| Scenario | Penalize? |
|---|---|
| Response locale matches prompt locale, even if it differs from task locale parameter | No |
| Response locale matches the code/data locale from the prompt examples | No |
| Response uses wrong units of measurement for the locale (e.g., miles instead of km) | Yes |
| Response uses wrong currency for the locale | Yes |
| Arabic response uses MSA even if prompt is ar_EG or ar_SA | No |
| Response contains multiple words in a different language | Yes (flag it) |
