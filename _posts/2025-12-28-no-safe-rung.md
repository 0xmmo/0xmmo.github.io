---
layout: post
title: "No Safe Rung"
date: 2025-12-28 12:00:00 +0000
icon: 🪜
excerpt: "The prevailing narrative implies a ceiling — that somewhere on the seniority ladder there's a rung where humans become irreplaceable. There isn't."
---

*We're not replacing junior SWEs. We're replacing every SWE. Including me, a senior engineer for multiple YC companies.*

---

The prevailing narrative around AI and software engineering goes something like this: AI is coming for junior developers, but senior engineers are safe for a while. The Harvard study confirms it — junior employment drops 9-10% at AI-adopting firms while senior headcount barely moves. Stanford's payroll data shows developers aged 22-25 lost nearly 20% of their jobs between 2022 and 2025. Entry-level hiring at the 15 biggest tech firms fell 25% in a single year. Marc Benioff announced Salesforce would hire "no new engineers" in 2025. The junior apocalypse is real and it's here.

But this framing is wrong. Not because juniors aren't being replaced — they are. It's wrong because it implies a ceiling. It implies that somewhere on the seniority ladder there's a rung where humans become irreplaceable. There isn't.

We're not watching AI eat the bottom of the engineering org chart. We're watching it eat the entire thing, starting from the bottom because that's the path of least resistance.

## The Wrong Mental Model

When people try to reason about which engineers AI will replace, they reach for the traditional model of what makes a senior engineer valuable. They list things like:

- Fix complex, cross-system bugs
- Read and interpret production logs and traces
- Design system architecture
- Navigate ambiguous requirements
- Mentor junior engineers
- Make trade-offs between competing constraints
- Understand the codebase deeply

Then they look at current AI tools, note that they struggle with some of these tasks, and conclude that senior engineers are safe. This is the equivalent of looking at the first iPhone in 2007 and concluding that mobile phones will never replace cameras, GPS devices, or music players.

The mistake is treating the current snapshot of AI capability as a statement about its ceiling. But the more fundamental mistake runs deeper than that. It's a misunderstanding of what intelligence *is* and why it mattered in the first place.

## The Knowledge Thesis

Here is my claim: **the only thing that levels up an engineer is knowledge.**

You might object — what about aptitude? What about raw intelligence? I'd argue aptitude is simply the speed at which you acquire and synthesize knowledge. A "10x engineer" isn't ten times smarter in some abstract sense. They've accumulated more relevant knowledge — about systems, failure modes, patterns, tools, trade-offs — and they can retrieve and apply it faster.

Every meaningful jump in an engineer's career comes from knowledge accumulation:

- You debug your first production outage and learn how distributed systems actually fail.
- You ship a feature that collapses under load and learn why you should have used a queue.
- You read a codebase written by someone better than you and absorb patterns you couldn't have invented.
- You sit in a hundred architecture reviews and develop an intuition for what will and won't scale.

Senior engineers aren't valuable because they're *smarter*. They're valuable because they've *seen more*. They carry a vast internal library of patterns, anti-patterns, failure modes, and solutions built from years of lived experience across systems, languages, and domains.

This is precisely why LLMs are so dangerous to the profession. Not because they're smarter than us. Because they *know more than us*, and the gap is not close.

## A Million Staff Engineer Lifetimes

Consider what an LLM has actually consumed during training. Every Stack Overflow question and answer. Every GitHub issue, pull request, and code review. Every technical blog post, RFC, and API reference. Every computer science textbook, every conference talk transcript, every postmortem from every major outage at every company that published one.

An LLM has, in a very real sense, accumulated the experience and knowledge required for a million staff engineer lifetimes. It hasn't just read about how to design a distributed cache — it's read every implementation, every benchmark, every failure story, every competing approach. It hasn't just seen one way to structure a React app — it's seen every way anyone has ever structured a React app and written about it publicly.

Dario Amodei, in *Machines of Loving Grace*, describes the endgame as "a country of geniuses in a datacenter" — millions of instances, each operating at 10x-100x human speed, each carrying the accumulated knowledge of the entire public corpus of human software engineering. He's not talking about AI as a fancy autocomplete. He's talking about AI that can "write difficult codebases from scratch" and "be given tasks that take hours, days, or weeks to complete, and then goes off and does those tasks autonomously, in the way a smart employee would."

We are not there yet. But we are closer than most people realize. SWE-Bench Verified — the standard benchmark for measuring an AI's ability to resolve real GitHub issues — went from single-digit percentages in early 2024 to over 80% by late 2025. Claude Opus 4.5 broke 80%. Two years from useless to resolving four out of five real-world software issues autonomously. Extrapolate that curve even conservatively and the destination is obvious.

## "But They Don't Know *Our* Codebase"

The most common objection I hear from senior engineers is the familiarity argument: *Sure, an LLM knows a lot in general, but it doesn't know our specific codebase, our business logic, our internal conventions, our undocumented assumptions.*

This is true today. And it's irrelevant to the trajectory.

The reason an LLM doesn't know your codebase isn't because it *can't*. It's because it currently lacks the interfaces to acquire that knowledge efficiently. Your codebase isn't hidden behind some fundamental cognitive barrier. It's hidden behind authentication screens, Slack threads, Jira tickets, internal wikis, and tribal knowledge that lives in people's heads because nobody wrote it down.

These are interface problems, not intelligence problems. And interface problems get solved.

Consider what's already happened in the last two years. AI went from "can barely write a function" to "can autonomously resolve 80% of real GitHub issues." Context windows went from 4K tokens to over a million. AI agents gained the ability to execute shell commands, browse documentation, run tests, and iterate on failures. Each of these was an interface problem that got solved.

The remaining interface problems — accessing Slack, navigating Jira, authenticating through SSO, understanding your CI/CD pipeline — are not harder than the ones already solved. They're easier. They're just engineering work. And ironically, they're exactly the kind of engineering work that AI is good at.

## The Tactical Reality

Think about everything a software engineer actually *does* in a day. Not the idealized job description — the actual tactical work:

1. **Communicates with managers and coworkers** — Slack, email, meetings, stand-ups
2. **Reads, writes, and edits code** — the core technical work
3. **Uses the command line** — git, build tools, deployment scripts, debugging
4. **Browses the web for information** — Stack Overflow, documentation, blog posts
5. **Browses internal resources** — Slack history, Jira tickets, Confluence pages, internal docs
6. **Uses browser-based tools** — dashboards, admin panels, monitoring systems
7. **Authenticates via web interfaces built for humans** — SSO, OAuth, 2FA

Now assess where AI stands on each of these:

Items 2, 3, and 4 are effectively solved. AI coding agents read, write, and edit code at a level that's already superhuman for many task types. They execute shell commands fluently. They browse the web and synthesize documentation better than most humans. Google reports 25%+ of internal code is now AI-generated. Microsoft is at 30%. Y Combinator's Winter 2025 batch had a quarter of founders reporting 95% AI-generated code.

Items 5, 6, and 7 are partially solved and improving rapidly. MCP (Model Context Protocol) and similar standards are giving AI agents the ability to interact with arbitrary tools and services. Every major platform is racing to build AI-native APIs. The authentication problem — the last truly human-dependent interface — is being worked on from every angle.

Item 1 — communication with humans — is the final frontier, and arguably the one that matters least for raw productivity. When AI can do items 2-7 autonomously, the remaining human role is reduced to "tell the AI what to build and verify that it built the right thing." That's not a senior engineer's job. That's a product manager's job.

We've achieved roughly half of this list and are working our way through the rest. The trajectory is unmistakable.

## The Evidence Against My Thesis (And Why It Doesn't Hold)

I want to be honest about the counterarguments, because they're real and they're being raised by serious people.

**The METR Study.** In early 2025, METR ran a randomized controlled trial with 16 experienced open-source developers and found that AI tools made them 19% *slower*, even though the developers themselves believed they'd gotten 20% faster. This is the best empirical evidence we have, and it points in the opposite direction of my thesis.

But the METR study captures a snapshot of a specific moment with specific tools. Most participants had less than 50 hours of experience with their AI tools. The study authors themselves noted that "deeply understood open source repos are close to a worst-case scenario" for AI assistance — the developers already had such deep familiarity that AI's knowledge advantage was minimized. And the tools used (Cursor Pro with Claude 3.5/3.7 Sonnet) are already two generations behind what's available now.

**The benchmark-to-reality gap.** SWE-Bench Pro, a harder and more realistic version of SWE-Bench, shows models dropping from 80%+ to roughly 23% on more complex tasks. On private, previously unseen codebases, performance drops further — to 15-18%. The gap between benchmarks and real-world deployment is enormous.

This is true, and it matters for estimating *timelines*. But it doesn't change the *trajectory*. Every year, the harder benchmarks get solved too. The gap shrinks. SWE-Bench Verified went from single digits to 80% in two years. There's no reason to believe SWE-Bench Pro won't follow a similar curve.

**The Stack Overflow survey.** The 2025 survey of 49,000+ developers showed trust in AI output cratering to 29%, down from 40% in 2024. Two-thirds of developers cite frustration with "AI solutions that are almost right, but not quite." Only 3% report high trust.

This tells us that current tools are frustrating to use. It doesn't tell us that future tools will be. The first generation of any technology is always frustrating. The question isn't whether today's tools are perfect — it's whether the problems they have are solvable. Code that's "almost right but not quite" is a solvable problem. It's a problem that gets better with every model generation, every context window expansion, every improvement in tool use and error correction.

## The Amodei Framework

In *Machines of Loving Grace*, Amodei proposes thinking about AI's impact through what he calls "the marginal returns to intelligence." The key question for any domain is: *how much does being smarter help, and what other factors limit progress?*

In biology, intelligence helps enormously but is bottlenecked by the physical speed of experiments — cells divide at a fixed rate regardless of how smart the researcher is. In manufacturing, intelligence helps with design but is bottlenecked by physical materials and supply chains. In governance, intelligence helps with policy design but is bottlenecked by human institutions and political will.

In software engineering? The marginal returns to intelligence are nearly unbounded, and the complementary physical factors are nearly zero.

Software is pure thought-stuff. The inputs are knowledge and reasoning. The outputs are text files. There is no waiting for cells to divide. There is no supply chain for bits. The "factory floor" is a computer that operates at the speed of light. Software engineering is, by Amodei's own framework, among the *most* vulnerable domains to AI disruption — precisely because it has the fewest physical-world bottlenecks.

Amodei estimates that powerful AI "could come as early as 2026" and acknowledges that "in the long run AI will become so broadly effective and so cheap that [comparative advantage] will no longer apply." He's describing the CEO of the company building the tools that are replacing us, admitting — in carefully hedged language — that the economic logic protecting human engineers has an expiration date.

He's right. And his hedging understates the urgency.

## The Comparative Advantage Trap

The most sophisticated defense of human engineers is the comparative advantage argument: even if AI is better at everything, humans will still be employed because AI and humans have different resource costs and different relative advantages across tasks.

Amodei himself makes this argument for the short term: "As long as AI is only better at 90% of a given job, the other 10% will cause humans to become highly leveraged, increasing compensation."

This is economically sound and practically misleading. Yes, in theory, as long as there's a single task where a human's opportunity cost is lower than spinning up an AI, the human remains employable. In practice, the number of such tasks is shrinking with every model release. And the economic logic only works if the remaining human-advantaged tasks are valuable enough to sustain employment. Being the cheapest option for 3% of a job description doesn't pay a mortgage.

LessWrong contributor *A_donor* crystallized this in a post arguing that SWE automation would crash the crypto market: the path isn't from "AI can't code" to "AI replaces all coders" overnight. It's a gradual squeeze where AI handles an increasing share of tasks, teams shrink, hiring freezes spread, and the remaining engineers compete for fewer and fewer roles that still require a human in the loop. The jobs don't disappear in a dramatic moment. They erode.

The Harvard data already shows this erosion in action. It's not layoffs driving the junior decline — it's *slower hiring*. Companies don't fire juniors. They just stop replacing them when they leave. The same pattern will move up the seniority ladder.

## The Pipeline Problem Nobody Is Talking About

Here's what keeps me up at night. If AI replaces the junior rung of the engineering ladder, where do future senior engineers come from?

Today's senior engineers became senior by spending years as juniors. They debugged their first production outage. They shipped their first terrible architecture and learned from the fallout. They got code reviews from people better than them and slowly internalized the patterns.

If companies stop hiring juniors — and the data says they already are — then the pipeline that produces senior engineers dries up. Harvard's Amy Edmondson calls this "short-sighted," noting that entry-level positions are "crucial for developing future leaders."

But here's the dark irony: by the time the pipeline problem manifests (5-10 years from now), AI may have advanced to the point where senior engineers aren't needed either. The pipeline problem assumes a future where senior human engineers are still valuable. If that assumption is wrong — if AI continues on its current trajectory — then the pipeline problem is moot. You don't need to train human replacements for roles that no longer exist.

## What's Left

I want to be clear about what I'm *not* saying. I'm not saying AI will replace all software engineers next quarter. I'm not saying current tools are sufficient. I'm not saying the transition will be clean or painless.

What I'm saying is that the structural barriers people point to — domain knowledge, codebase familiarity, architectural judgment, communication skills — are not permanent moats. They are interface problems and knowledge problems. And we are building systems whose entire purpose is to solve interface problems and knowledge problems.

Amodei puts it plainly: "I am *not* talking about AI as merely a tool to analyze data... I'm talking about using AI to perform, direct, and improve upon nearly everything."

He's talking about biology in that quote. But the shoe fits software engineering even better. Biology has cells that divide at fixed speeds. Software has no such constraint. Biology requires physical labs and materials. Software requires a text editor. Every factor that slows AI's takeover of other domains — the physical world, the speed of experiments, the need for specialized equipment — is *absent* from software engineering.

The LessWrong forecasting community puts "superhuman coder" arrival between 2027 and 2033, with a within-model median of 2028. Ryan Greenblatt of Redwood Research, one of the more careful forecasters, gives 45% probability to full AI R&D automation by 2033. Even the conservative end of these estimates is within a typical engineer's career horizon.

Google's 2025 DORA report captures the current transitional moment perfectly: individual developer output surged 98% with AI adoption, but organizational delivery metrics stayed flat. Addy Osmani calls this the "80% problem" — AI gets you 80% of the way there, and the last 20% is where things break down. His metaphor: "We got faster cars, but the roads got more congested."

That 80% will become 90%. Then 95%. Then 99%. And at some point, the remaining 1% isn't a job description anymore — it's a button you push before the AI starts working.

## The Honest Conclusion

I'm a senior engineer at multiple YC companies, and I'm telling you: there is no safe rung on this ladder. Not mine. Not yours.

The only honest position is to acknowledge that we are in a profession with a visible expiration date. Not because we're bad at our jobs. Not because juniors are replaceable and seniors aren't. But because the thing that made us valuable — accumulated knowledge and the ability to apply it — is precisely the thing that LLMs do better than us and will only get better at.

Amodei, to his credit, admits he doesn't have answers for what comes after: "The brevity of this section is not at all to be taken as a sign that I don't take these issues seriously — on the contrary, it is a sign of a lack of clear answers."

Neither do I. But I'd rather face the question honestly than hide behind the comforting fiction that seniority makes us safe. The AI doesn't care about your title. It cares about the same thing you do: solving the problem. And it has read every solution ever published.

The question isn't whether AI will replace senior engineers. The question is when. And the honest answer — the one that the data, the benchmarks, the trajectories, and the people building these systems all point to — is: sooner than we think.

---

*"Intelligence may be very powerful, but it isn't magic fairy dust." — Dario Amodei*

*He's right. It isn't magic. It's engineering. And engineering problems get solved.*
