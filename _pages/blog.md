---
layout: default
title: "Blog"
permalink: /blog/
---

<h2>All Posts</h2>

<div class="blog-grid">
  {% for post in site.posts %}
    <div class="blog-card">
      <a href="{{ post.url }}">
        <div class="blog-title">{{ post.title }}</div>
        {% if post.title_en %}
          <div class="blog-title-en">{{ post.title_en }}</div>
        {% endif %}
        <div class="blog-date">{{ post.date | date: "%Y年%m月%d日" }}</div>
      </a>
    </div>
  {% endfor %}
</div>