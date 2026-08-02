---
layout: redirect
title: "Preventing agent doom loops with per-object reasoning traces"
date: 2025-11-27 21:16:52 +0000
icon: 🕵️
excerpt: "When an agent updates an external system through a tool, it tends to eventually get stuck in a loop: fixing one issue produces a second, and fixing the second brings back the first."
notion_id: 2b8013e9-768a-8058-a944-f0df1f7a77ed
---

When an agent updates an external system through a tool, it tends to eventually get stuck in a loop: fixing one issue produces a second, and fixing the second brings back the first.

This happens to any agent modifying an external object, but it's most obvious in coding agents — the unstable bug wall you hit that blocks progress without manual intervention. [Ilya Sutskever](https://youtu.be/aR20FWCCjAs?si=0sxm9e_2YM1t3vve&t=238) cites it as the key example of LLMs failing at simple human tasks.

The solution is simple. The golden rule: **don't modify an object until you understand how it ended up in its current state** (this is [Chesterton's Fence](https://fs.blog/chestertons-fence/)).

What counts as an object is an engineering tradeoff. For coding agents a codebase is too big, a function too small — a class or module is about right. The "how it ended up in its current state" piece is the **reasoning trace**: every time an agent modifies an object, it must give a concise reason for the change, and we persist that on the object to be reviewed on future modifications. \[1\]

A real example: a personal AI assistant keeps a user profile (the object) in chat context, updated every few messages via an `updateUserProfile` tool. We inject a `reasoningForUpdates` argument that is never shown in chat context, only saved for future reference.


```javascript
{
  name: "updateUserProfile",
  parameters: {
    firstName: { type: "string" },
    primaryLanguage: { type: "string" },
    residenceCityAndState: { type: "string" },
    // injected:
    reasoningForUpdates: { type: "array", items: { type: "string" } },
    required: ["reasoningForUpdates"],
  },
}
```

Say I mention I live in San Francisco. My profile gets `residenceCityAndState: "San Francisco, CA"` and the trace left behind is `"User asked about San Francisco residential parking permits"`.

Later I ask for the weather in Austin, TX. With **only** the existing profile as context, the LLM won't hesitate to flip my residence to Austin — wrong, I was just traveling. And next time I ask about San Francisco weather, it flips right back. A doom loop.

Instead, we pass the profile's accumulated reasoning traces as context right as we're about to update. Armed with the parking-permit inquiry from before, any capable LLM will **not** touch `residenceCityAndState`. It has the confidence for **stability**.

This might cost you a second LLM call, and at scale you'll deduplicate traces and pay for context — but those are details. The golden rule once more: don't modify an object until you understand how it ended up in its current state. It seems simple because it is.

---

\[1\] This can be done with good ol' code comments for coding agents. Although this is very fragile as LLMs do not like to append to comments across changes or use them as a history log, so I keep a separate index for reasoning traces on a project's files.
