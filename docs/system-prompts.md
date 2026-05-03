# System Prompts — Full Documentation

## What is a System Prompt?

A system prompt is a short set of instructions given to an AI that defines how it should behave, what its capabilities are, and which guidelines it must follow in conversation. Think of it as the AI's "operating instructions" or "personality configuration," shaping how the assistant responds. It's typically 2–5 lines, used in addition to the user prompt, and is meant to be to the point and direct.

## Conversation Structure

```
System Prompt     →  Sets rules, persona, context (hidden from user)
    ↓
Conversation History  →  All prior messages (user + assistant turns)
    ↓
Current User Message  →  What the user just said
    ↓
Model Response        →  Generated based on all of the above
```

## Examples

**Example 1 — Code extraction format**

System prompt: Begin every code extraction with: "Hark, here is what ye have requested!" Present the extraction as bulleted items (e.g., function names, classes, key algorithms, complexity notes). End with: "There you are, all that is extracted and Nevermore!" You will produce two code extractions; clearly differentiate them (e.g., "Extraction 1", "Extraction 2").

**Example 2 — Style (coding)**

System prompt: Write the response in the style of a code reviewer writing a review—concise, evaluative, and focused on readability, correctness, performance, and edge cases.

## FAQs

**Q: Can there be tasks without a System Prompt?**
A: Yes. In a batch, you may receive tasks with or without a System Prompt.

**Q: If a System Prompt is included, will the tasks also have a User Prompt?**
A: Yes. A User Prompt is always included in every task.

**Q: Will the User Prompt include reference text when a System Prompt is provided?**
A: Yes. Depending on the task category, the User Prompt will include reference text.
