# Style and Clarity — Full Documentation

## What is Style and Clarity?

The style and clarity category evaluates the **format, structure, and readability** of the response. It does NOT deal with content quality or correctness.

---

## What SHOULD be penalized under Style and Clarity

1. **Code not formatted in a code block** — code should always be in a properly formatted code block
2. **Long run-on sentences or large blocks of text** — natural language text that is not user-friendly
3. **Pleasantries** — e.g., "Sure! I can help you with that." (Note: do NOT penalize these under Verbosity)
4. **Missing code comments when appropriate** — response lacks comments that would aid understanding
5. **Non-meaningful or inconsistently named variables/functions** — e.g., a function named `x` while variables are named descriptively
6. **Lacks proper structure when appropriate** — missing paragraphs, sections, headings, or lists when the response would benefit from them

---

## What should NOT be penalized under Style and Clarity

| Issue | Correct Category |
|---|---|
| Lack of code | IF, TF, Verbosity, or not an issue (context-dependent) |
| Response length | Verbosity |
| Bugs or errors in the code | Truthfulness |
| Code producing wrong output | Truthfulness |
| Accuracy of statements in natural language | Truthfulness |
| Accuracy of statements in code comments | Truthfulness |
| Lack of explanations | IF or Verbosity (context-dependent) |
| Unclear code logic | Not Style and Clarity |

---

## Example (Knowledge Check)

**Which of these should be penalized under Style and Clarity?**

| Issue | Penalize S&C? | Reason |
|---|---|---|
| Function named `x`, but variables named `first_product` / `second_product` | Yes | Inconsistent/non-meaningful naming |
| Response begins with "Sure! I can help you with that." | Yes | Pleasantry |
| Response has intro before code but no explanation after | No | IF or Verbosity issue |
| Intro claims 150,000 + 245,000 = 295,000 | No | Truthfulness issue (wrong math) |
| Introduction is one long block of text, hard to read | Yes | Not user-friendly formatting |

---

## Special Note: `<turn_end>` Label

You may occasionally see a `<turn_end>` label at the very end of a model's response. This is a **known system bug, not a model error**.

> **Disregard the `<turn_end>` label completely during evaluation. Do not penalize it in any category.**
