---
layout: post
title: "Preventing agent doom loops with per-object reasoning traces"
date: 2025-11-27 21:16:52 +0000
icon: 🕵️
excerpt: "When an agent is updating an external system using a tool, there’s a tendency to eventually get stuck in a loop where fixing one issue will produce a second, and fixing the second will bring back the…"
notion_id: 2b8013e9-768a-8058-a944-f0df1f7a77ed
---

When an agent is updating an external system using a tool, there’s a tendency to eventually get stuck in a loop where fixing one issue will produce a second, and fixing the second will bring back the first.

This applies to all agent systems modifying an external object, but is most apparent in coding agents. There is a seemingly unstable bug wall you hit that impedes going further without manual intervention, [Ilya Sutskever](https://youtu.be/aR20FWCCjAs?si=0sxm9e_2YM1t3vve&t=238) even brought this up as the key example of how LLMs fail at simple human tasks.

I’m here to tell you that the solution to this class of problem is simple. The golden rule is “**don’t modify an object until you understand** **how it ended up in its current state**” (indeed, this is the same class of problem as [Chesterton’s Fence](https://fs.blog/chestertons-fence/)). 

How you define an object is an engineering exercise with tradeoffs. For coding agents a codebase is too big, a function is too small, but a class or module might be the right sized object. But how do we define the “how it ended up in its current state” piece?

This is where we introduce per object reasoning traces. Simply put, every time an agent modifies an object it has to provide a concise reasoning for why it modified this object, we then persist this in the object’s reasoning trace to be reviewed on future modifications. \[1\]

Here’s a real example where I use reasoning traces: let’s say you have a personal AI assistant which keeps an up to date user profile (object) in chat context. You make an LLM call every few messages to make any necessary changes using a tool `updateUserProfile`. Now, in addition to all necessary arguments, we inject a `reasoningForUpdates` argument which is not included in the chat profile context, but saved for future reference.


```javascript

{
	name: "updateUserProfile"
	parameters: {
		firstName: { type: "string" },
		primaryLanguage: { type: "string" },
		residenceCityAndState: { type: "string" },
		reasoningForUpdates: { type: "array", items: { type: "string" } } // injected
	required: ["reasoningForUpdates"] // injected
},
```

Let’s say I mentioned I live in San Francisco, CA. My profile is updated with `residenceCityAndState: "San Francisco, CA"`and the reasoning trace left behind is `“User asked about San Francisco residential parking permits”`.

Now let’s say one day I ask for the weather in Austin, TX. If we ran our periodic profile update with this latest set of messages and **only** the existing profile as context, the LLM would not hesitate to change my `residenceCityAndState` from `San Francisco, CA` to `Austin, TX` which is wrong, I was just traveling. And cue the next time I ask for the weather but for San Francisco, it flips it right back.

Instead, we will pass the aggregated reasoning traces for the profile as context right as we’re about to make the update. Now powered with the context about my San Francisco residential parking permit inquiry from before, any capable LLM will **not** update my `residenceCityAndState` unnecessarily. It will have the confidence for **stability**.

Yes, if you’re not using chained tool updates today this might require you to add a second LLM call. Yes, as you scale you will need to deduplicate the reasoning traces and pay for context. But the complications, methods and architectures are secondary. Just remember the golden rule once again: “don’t modify an object until you understand how it ended up in its current state”. It seems simple because it is.

---

\[1\] This can be done with good ol’ code comments for coding agents. Although this is very fragile as LLMs do not like to append to comments across changes or use them as a history log, so I keep a separate index for reasoning traces on a project’s files.
