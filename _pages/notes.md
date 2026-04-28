---
layout: default
title: "Notes"
permalink: /notes/
author_profile: false
wide: true
---

{% assign sorted_notes = site.notes | sort: "date" | reverse %}

<section class="content-index content-index--notes" data-content-filter>
  <header class="content-index__hero">
    <p class="content-index__eyebrow">Notes</p>
    <h1>Primary-source reading notes for agent and systems work</h1>
    <p>
      Chinese translations and structured reading notes from OpenAI, Anthropic,
      source-code readings, and engineering blogs.
    </p>
  </header>

  <div class="content-index__toolbar">
    <label class="content-index__search">
      <span>Search</span>
      <input type="search" data-content-search placeholder="Search notes, sources, and topics">
    </label>

    <div class="content-index__filters" aria-label="Filter notes by source">
      <button class="is-active" type="button" data-filter-value="all">All</button>
      {% assign note_sources = site.notes | map: "note_source" | compact | uniq | sort %}
      {% for source in note_sources %}
        <button type="button" data-filter-value="{{ source | slugify }}">{{ source }}</button>
      {% endfor %}
    </div>
  </div>

  <div class="content-index__status" data-content-status>{{ sorted_notes | size }} notes</div>

  <div class="content-list">
  {% for note in sorted_notes %}
    <article class="content-card" data-content-card data-topics="{{ note.note_source | slugify }}" data-search-text="{{ note.title | strip_html | escape }} {{ note.title_en | strip_html | escape }} {{ note.note_source | escape }} {{ note.original_author | escape }} {{ note.excerpt | strip_html | strip_newlines | escape }} {{ note.topics | join: ' ' | escape }}">
      <a class="content-card__main" href="{{ note.url | relative_url }}">
        <div class="content-card__meta">
          <span>{{ note.note_source }}</span>
          {% if note.original_author %}
            <span>{{ note.original_author }}</span>
          {% endif %}
          <span>{{ note.date | date: "%Y年%m月%d日" }}</span>
        </div>
        <h2>{{ note.title }}</h2>
        {% if note.title_en %}
          <p class="content-card__subtitle">{{ note.title_en }}</p>
        {% endif %}
        <p class="content-card__excerpt">{{ note.excerpt | strip_html | strip_newlines | truncate: 132 }}</p>
      </a>
      <div class="content-card__topics">
        {% if note.topics %}
          {% for topic in note.topics %}
            <span>{{ topic | replace: "-", " " }}</span>
          {% endfor %}
        {% else %}
          <span>{{ note.note_source }}</span>
        {% endif %}
      </div>
    </article>
  {% endfor %}
  </div>

  <p class="content-index__empty" data-content-empty hidden>No matching notes.</p>
</section>

<script src="{{ '/assets/js/content-index.js' | relative_url }}"></script>
