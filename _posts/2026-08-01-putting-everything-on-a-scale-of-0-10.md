---
layout: post
title: "Putting everything on a scale of 0-10"
date: 2026-08-01 22:41:59 -0700
icon: 🔟
excerpt: "I open the weather app. 143 AQI. I don't know what that means. Oh, it's orange-red. I don't know what that means either."
---

I open the weather app. 143 AQI. I don't know what that means. Oh, it's orange-red. I don't know what that means either. I'm at a concert and my phone says 79 dB, no clue, is that bad? A 7.x earthquake just hit Japan?

Here's my proposal.

Most environmental quantities would be better off with a well-defined 0-10 index. Oh, it's an unbounded measure? Well yes, that's how most numbers work. Let it exceed 10 in those rare cases. Let me explain.

The UV index is a great example. There is no physical unit called "one UV". You take the UV irradiance spectrum and weight each wavelength by how much it actually burns skin. Because raw energy didn't mean damage (325nm is 0.3% as harmful as 295nm, and short stuff never reaches the ground at all) the science folk in charge had an epiphany: we should focus on making these numbers *useful to humans*. So they quantified damage, then chose a divisor that lands the values on a human scale:

- 0-3 you're fine, go outside
- 3-6 shirt, sunscreen
- 6-8 stay in the shade midday
- 8-10 stay inside
- 10+ extreme

Well, many more values humans encounter in their daily environment should be made *useful to humans*. Let's start with AQI (Air Quality Index), they got so close and made an index. But decided it should be 0-500 AND the midpoint is objectively "very bad". Then dBs, a number I've only ever seen between 50 and 80 but have never once acted on. Let's make them 0-10.

Even better, let's anchor the *meaning* of the numbers between those different phenomena we're measuring.

- 0-3 not bad
- 3-6 concerning
- 6-8 high
- 8-10 very bad
- 10+ extreme

The Richter scale got even closer but unfortunately didn't normalize properly: an 8 is catastrophic and rare, instead of 8 meaning "pretty bad, but there's worse".

yours truly grug mo
