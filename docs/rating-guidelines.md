# How to Rate — Full Documentation

## Core Rule

Always judge the final responses against all three: **System Prompt + Conversation History + User Prompt**.

Prefer the response that:
- Fully follows all instructions
- Keeps claims and code accurate
- Reflects the accumulated context from conversation history

---

## Example 1 — System Prompt Impact

**System Prompt:** Respond only with a valid Python code block. The function must be named in snake_case.

**User Prompt:** Implement an iterative factorial function.

**Response A:** No issues.
```python
def factorial_iter(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

**Response B:** Major Issues (Instruction Following)

> "I'd be happy to help! Here is the factorial function..."
```python
def factorialIter(n):
    ...
```
Violates system prompt: includes prose (not a pure code block) and function is named in camelCase, not snake_case.

---

## Example 2 — Conversation History as Context

**Conversation History:**
- User: Show a simple Python function to fetch JSON with requests.
- Assistant: (sync version using requests)
- User: Convert it to async with aiohttp, add a 5s timeout, keep it minimal.
- Assistant: (async aiohttp version with ClientTimeout(total=5))

**User Prompt:** Add a retry with exponential backoff (max 3 tries) and rename `data` to `payload`.

**Response A:** No issues.
Implements async aiohttp + 5s timeout, retry with exponential backoff, and renames `data` → `payload`.
Honors conversation history and the latest instructions.

**Response B:** Issues in Instruction Following & Truthfulness
Adds a retry loop but omits the 5s timeout OR keeps variable as `data` (did not rename to `payload`).
Fails to carry forward critical constraints from the conversation history into the latest turn.

---

## Truthfulness — Important Caveat

Truthfulness is **not** evaluated based on external real-world accuracy.

> Truthfulness is evaluated based on how well the response **understood and fulfilled the prompt**.

In other words: judge whether the response correctly delivered what the prompt asked for — not whether the code/content is correct in an absolute sense.
