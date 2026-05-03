# Conversation History — Full Documentation

## What is Conversation History?

Conversation history is the full record of messages exchanged between the user and the AI — everything said so far in the chat. In this project, you may see a user–assistant dialog of up to 6 turns. In such cases, the User Prompt is simply the next message in that conversation.

To complete tasks well, act as if you've been part of the ongoing chat: use the conversation history as essential context and carry it forward into your latest prompt.

## Example (Coding-Related)

**Conversation History:**

Turn 1 — User: Write a Python function that fetches JSON from a URL using requests. Keep it brief and production-ready.

Turn 1 — Assistant:
```python
import requests

def fetch_json(url: str, *, timeout: float = 3.0) -> dict:
    """Fetch JSON from the given URL with basic error handling."""
    resp = requests.get(url, timeout=timeout)
    resp.raise_for_status()
    return resp.json()
```

Turn 2 — User: Rewrite it to be async using aiohttp, include a timeout, and add a short docstring.

Turn 2 — Assistant:
```python
import asyncio
import aiohttp

async def fetch_json(url: str, *, timeout: float = 3.0) -> dict:
    """Asynchronously fetch JSON from the given URL."""
    timeout_cfg = aiohttp.ClientTimeout(total=timeout)
    async with aiohttp.ClientSession(timeout=timeout_cfg) as session:
        async with session.get(url) as resp:
            resp.raise_for_status()
            return await resp.json()
```

**User Prompt (latest turn):** Replace the variable name `data` with `payload` and set timeout to 5 seconds.

This is the prompt you must consider during evaluation — and the Conversation History provides the context (Python → async aiohttp version). Use it to judge whether the next response correctly applies the requested refactor.

## FAQs

**Q: Can there be tasks without a Conversation History?**
A: Yes. In a batch, you may get tasks with or without a Conversation History.

**Q: Can there be tasks with a Conversation History and reference text?**
A: Yes.

**Q: Should we evaluate responses included in the Conversation History?**
A: No. Only evaluate the latest turn (the User Prompt).

**Q: Can there be tasks with both a System Prompt and Conversation History?**
A: Yes. Such cases may exist.
