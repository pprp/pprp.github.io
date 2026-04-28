---
layout: default
title: "Writing"
permalink: /blog/
author_profile: false
wide: true
---

{% assign featured_post = site.posts | first %}
{% assign writing_topics = "agent:Agent|long-context:Long context|llm-systems:LLM systems|model-compression:Model compression|paper-reading:Paper reading|product-thinking:Product thinking|engineering:Engineering|efficient-llm:Efficient LLM|reasoning:Reasoning|open-models:Open models" | split: "|" %}

<section class="content-index content-index--writing" data-content-filter>
  <header class="content-index__hero">
    <p class="content-index__eyebrow">Writing</p>
    <h1>Research notes, technical essays, and system-level thinking</h1>
    <p>
      Original essays around efficient LLMs, long-context systems, agent engineering,
      model compression, and AI-native product interfaces.
    </p>
  </header>

  <div class="content-index__toolbar">
    <label class="content-index__search">
      <span>Search</span>
      <input type="search" data-content-search placeholder="Search titles, summaries, and topics">
    </label>

    <div class="content-index__filters" aria-label="Filter writing by topic">
      <button class="is-active" type="button" data-filter-value="all">All</button>
      {% for topic_pair in writing_topics %}
        {% assign topic_parts = topic_pair | split: ":" %}
        <button type="button" data-filter-value="{{ topic_parts[0] }}">
          {{ topic_parts[1] }}
        </button>
      {% endfor %}
    </div>
  </div>

  {% if featured_post %}
    <article class="content-feature">
      <div>
        <p class="content-feature__label">Latest Essay</p>
        <h2><a href="{{ featured_post.url | relative_url }}">{{ featured_post.title }}</a></h2>
        {% if featured_post.title_en %}
          <p class="content-feature__subtitle">{{ featured_post.title_en }}</p>
        {% endif %}
        <p>{{ featured_post.excerpt | strip_html | strip_newlines | truncate: 180 }}</p>
      </div>
      <div class="content-feature__meta">
        <span>{{ featured_post.date | date: "%Y年%m月%d日" }}</span>
        {% for topic in featured_post.topics %}
          <a href="{{ '/blog/' | relative_url }}?topic={{ topic | slugify }}">{{ topic | replace: "-", " " }}</a>
        {% endfor %}
      </div>
    </article>
  {% endif %}

  <div class="content-index__status" data-content-status>{{ site.posts | size }} posts</div>

  <div class="content-list">
  {% for post in site.posts %}
    {% capture topic_slugs %}{% for topic in post.topics %}{{ topic | slugify }} {% endfor %}{% endcapture %}
    <article class="content-card" data-content-card data-topics="{{ topic_slugs | strip }}" data-search-text="{{ post.title | strip_html | escape }} {{ post.title_en | strip_html | escape }} {{ post.excerpt | strip_html | strip_newlines | escape }} {{ post.topics | join: ' ' | escape }}">
      <a class="content-card__main" href="{{ post.url | relative_url }}">
        <div class="content-card__meta">
          <span>{{ post.date | date: "%Y年%m月%d日" }}</span>
          {% if post.last_modified_at %}
            <span>Updated {{ post.last_modified_at | date: "%Y.%m.%d" }}</span>
          {% endif %}
        </div>
        <h2>{{ post.title }}</h2>
        {% if post.title_en %}
          <p class="content-card__subtitle">{{ post.title_en }}</p>
        {% endif %}
        <p class="content-card__excerpt">{{ post.excerpt | strip_html | strip_newlines | truncate: 132 }}</p>
      </a>
      <div class="content-card__topics">
        {% for topic in post.topics %}
          <span>{{ topic | replace: "-", " " }}</span>
        {% endfor %}
      </div>
    </article>
  {% endfor %}
  </div>

  <p class="content-index__empty" data-content-empty hidden>No matching essays.</p>
</section>

<script src="{{ '/assets/js/content-index.js' | relative_url }}"></script>
