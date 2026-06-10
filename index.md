---
layout: default
title: Thoughts
---

<h1 class="title">Thoughts</h1>
<p class="home-intro">
  Notes by <a href="https://mmoustafa.com">Mohamed Moustafa</a>.
</p>

<ul class="post-list">
  <li>
    <a class="post-title" href="{{ '/forensics/post.html' | relative_url }}">Small Model Forensics</a>
    <span class="post-meta">May 13, 2026</span>
    <span class="post-excerpt">Claude and I made 2,000 API calls to nine small closed-weight models across three providers, discovering some interesting things about how providers scale...</span>
  </li>
  {% for post in site.posts %}
    <li>
      <a class="post-title" href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <span class="post-meta">{{ post.date | date: "%B %-d, %Y" }}</span>
      {% if post.excerpt %}<span class="post-excerpt">{{ post.excerpt | strip_html | strip_newlines | truncate: 160 }}</span>{% endif %}
    </li>
  {% endfor %}
</ul>
