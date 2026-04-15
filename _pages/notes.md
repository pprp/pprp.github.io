---
layout: default
title: "Notes"
permalink: /notes/
author_profile: false
---

<h2>Translated Notes</h2>

<p>Chinese translations and reposted reading notes based on official engineering and research blogs.</p>

{% assign sorted_notes = site.notes | sort: "date" | reverse %}

<div class="blog-grid">
  {% for note in sorted_notes %}
    <div class="blog-card">
      <a href="{{ note.url }}">
        <div class="blog-title">{{ note.title }}</div>
        {% if note.title_en %}
          <div class="blog-title-en">{{ note.title_en }}</div>
        {% endif %}
        <div class="blog-date">{{ note.note_source }} · {{ note.date | date: "%Y年%m月%d日" }}</div>
      </a>
    </div>
  {% endfor %}
</div>
