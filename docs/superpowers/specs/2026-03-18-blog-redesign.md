# Blog Redesign & UI Improvement Spec

Date: 2026-03-18

## Overview

Improve the personal academic website (Jekyll/AcadHomepage) with a proper blog system, better UI, image support, and faster load times. The homepage (`about.md`) is left unchanged. All changes are scoped to the blog index, post layout, and site-wide CSS.

---

## 1. Visual Style

- Background: warm white `#fffdf7`
- Headings: serif font (Georgia or Noto Serif SC for CJK)
- Accent color: purple `#805ad5`
- Body text: `#4a5568`
- Code blocks: light purple tint `#faf5ff` with border `#d6bcfa`
- New SCSS variables added to `_sass/_variables.scss`
- New `_sass/_blog.scss` partial imported from `assets/css/main.scss` at end of file

---

## 2. Blog Index Page (`_pages/blog.md`)

**No pagination.** All posts rendered server-side by Liquid, filtering done client-side via JS.

**Category slugs:** All category names in post front matter must be single-word hyphenated slugs (e.g., `llm`, `model-compression`). No spaces in category names.

**Left sidebar (~200px):**
- Category list rendered server-side by Liquid from `site.posts`
- Each category shows post count
- Single-select: clicking an active category deselects back to "All"
- "All" selected by default

**Right post list:**
- All posts as `<li>` elements, sorted by date descending
- Each `<li>` has `data-categories="llm model-compression"` (space-separated slugs; `""` if post has no categories)
- JS filter: `data-categories.split(' ').filter(Boolean)` — post is shown if the selected category is **included in** its categories array (not an exact set match)
- Posts with no categories are hidden when any specific category is selected
- Empty filter result: no special handling
- Each post: title (link), date, category tags
- No reading time on the blog index — `post.content` is not available in `site.posts` loops in standard Jekyll

**JS loading:** `blog.md` hardcodes `<script src="{{ '/assets/js/blog.js' | relative_url }}"></script>` as the last line of the page's Markdown content. Using `relative_url` ensures correct path resolution regardless of `baseurl` config.

---

## 3. Post Layout (`_layouts/post.html`)

**Inheritance:** `post.html` uses `layout: default`. The `default.html` layout structure (confirmed):
```
body > masthead > div#main > (sidebar + article.page > div.page__inner-wrap > section.page__content > {{ content }}) > scripts.html > /body
```
A `<script>` tag at the end of `post.html`'s content renders inside `section.page__content`, before `scripts.html` and before `</body>`. This is safe — the post DOM is fully rendered before the script executes.

**CSS conflict resolution:** `_blog.scss` overrides the theme's width constraint for post pages:
```scss
.page__content:has(.post-body) {
  max-width: 100%;
  padding: 0;
}
```
`:has()` support assumed (Chrome 105+, Safari 15.4+, Firefox 121+); older browser degradation accepted.

**Structure of `post.html` content:**
```html
<div class="post-header">
  <h1>{{ page.title }}</h1>
  <div class="post-meta">
    <span class="post-date">{{ page.date | date: "%Y-%m-%d" }}</span>
    {% for cat in page.categories %}
      <span class="post-tag">{{ cat }}</span>
    {% endfor %}
    {% assign _rt_words = content | strip_html | number_of_words %}
    {% assign _rt_min = _rt_words | divided_by: 200 | at_least: 1 %}
    {{ _rt_min }} min read
    {{- "<!-- divided_by uses integer division; at_least:1 handles posts under 200 words -->" -}}
  </div>
</div>
<div class="post-body">
  <aside class="post-toc">
    {% include toc.html %}
  </aside>
  <div class="post-content">
    {{ content }}
  </div>
</div>
<nav class="post-nav">
  {% if page.previous %}
    <a href="{{ page.previous.url | relative_url }}">← {{ page.previous.title }}</a>
  {% endif %}
  {% if page.next %}
    <a href="{{ page.next.url | relative_url }}">{{ page.next.title }} →</a>
  {% endif %}
</nav>
<script src="{{ '/assets/js/blog.js' | relative_url }}"></script>
```

**Note on Jekyll navigation variables:** In Jekyll, `page.previous` is the chronologically **older** post and `page.next` is the chronologically **newer** post. The layout above uses `page.previous` for the "← older" link and `page.next` for the "newer →" link, which is the conventional display order.

**`_includes/toc.html`** — new file (does not exist in the current theme), static HTML only. The `<nav>` is hidden by default via CSS (`#toc { display: none; }` in `_blog.scss`) to prevent flash of empty TOC before JS runs. JS sets it to visible after building the list (or keeps it hidden if no headings found):
```html
<nav id="toc">
  <button id="toc-toggle" aria-label="Toggle table of contents">Contents ▾</button>
  <ul id="toc-list"></ul>
</nav>
```
All TOC logic lives exclusively in `blog.js`. No other theme file includes `toc.html`.

**TOC JS (in `blog.js`):**
- Guard: if `#toc-list` doesn't exist, exit early
- Query `.post-content` for `h2` and `h3` elements
- kramdown auto-generates `id` attributes on all headings — the JS reads `heading.id` to build anchor links
- Build `<li><a href="#id">text</a></li>` list into `#toc-list`
- If no headings found, set `#toc` to `display: none`
- IntersectionObserver: `rootMargin: "0px 0px -60% 0px"`, `threshold: 0`
  - Track a `lastActive` variable (initially `null`).
  - On each observer callback, process only entries where `isIntersecting: true`. If any such entry exists, mark its TOC link active, unmark all others, update `lastActive`.
  - Entries where `isIntersecting: false` are ignored entirely — do not clear `lastActive` on exit events.
  - Result: active highlight updates when a heading enters the top 40% of the viewport; retains the last highlighted item when scrolling between headings or past the end; nothing highlighted on initial load before any heading has entered (acceptable).
- Mobile (< 768px): `#toc` `position: static`, `#toc-list` hidden by default, `#toc-toggle` visible; clicking toggle shows/hides `#toc-list`
- Desktop: `#toc` `position: sticky; top: 2rem`, `#toc-toggle` hidden, `#toc-list` always visible

---

## 4. Post Authoring

All new posts use Markdown with front matter:

```yaml
---
layout: post
title: 'Post Title'
date: 2025-08-05 11:00:00 +0800
categories: [llm, model-compression]
---
```

`_config.yml` — add a new list item under the existing `defaults:` key. The current file has one entry (`type: pages`). Add a second entry as a sibling (same indentation level):
```yaml
defaults:
  - scope:
      path: ''
      type: pages
    values:
      layout: default
      author_profile: true
  # ADD THIS:
  - scope:
      path: ''
      type: posts
    values:
      layout: post
      author_profile: false
```
Using `path: ''` with `type: posts` is the canonical Jekyll form — it scopes to all posts regardless of directory.

---

## 5. Reading Time Include (`_includes/reading-time.html`)

Reading time is shown **on post pages only**.

- Call site in `post.html`: `{% include reading-time.html %}`
- Inside `post.html`, `content` is the special Jekyll layout variable containing the rendered post body. It is NOT accessible as `page.content` from within a layout — it is only available as `content` directly.
- The include is called with no parameters; it uses `content` directly via the layout scope:
  ```liquid
  {% if content %}
    {% assign words = content | strip_html | number_of_words %}
    {% assign minutes = words | divided_by: 200 | at_least: 1 %}
    {{ minutes }} min read
  {% endif %}
  ```
- `strip_html` applied before `number_of_words` to avoid counting HTML tags
- Outputs nothing if content is empty
- Note: Jekyll includes do NOT inherit the calling layout's `content` variable — `content` is only available in layout files, not includes. Therefore, reading time must be computed **inline in `post.html`** rather than in a separate include. Remove `_includes/reading-time.html` from the files list; inline the Liquid directly in `post.html`'s `post-meta` div.

---

## 6. Image Support

Applied to `.post-content img` only. **Execution order in `blog.js` on DOMContentLoaded:**

1. Guard: if `.post-content` doesn't exist, exit
2. Set `loading="lazy"` on all `.post-content img`
3. Figure-wrap: for each img **not already inside `<figure>`** and **not inside `<a>`**:
   - Wrap in `<figure>`
   - If `img.alt` is non-empty and non-whitespace, append `<figcaption>` with that text
4. Bind lightbox click handlers on all `.post-content img` **not inside `<a>`** (queried after figure-wrap)

**Lightbox behavior:**
- Clicking eligible img creates and appends a full-screen `<div>` overlay (lazy-init on first click, reused thereafter)
- Image displayed centered in overlay
- ESC key or click outside the image closes it
- Vanilla JS, ~50 lines

**CSS:**
```scss
.post-content img {
  max-width: 100%;
  height: auto;
  display: block;
}
```

---

## 7. `blog.js` Responsibility Map

| Function | Blog index | Post page |
|---|---|---|
| Category filter | ✓ | — |
| TOC builder + scroll highlight | — | ✓ |
| Image lazy load + figure wrap + lightbox | — | ✓ |

Each function guards against missing DOM nodes and exits early if its required elements are absent.

---

## 8. Performance

- No CDN JS libraries added (all JS local in `assets/js/blog.js`)
- `compress_html` plugin stays active
- Existing HTML posts not migrated
- `blog.js` loaded only on blog index and post pages (not site-wide)
- All `src` and `href` paths use `| relative_url` filter for correct `baseurl` resolution

---

## 9. Files Changed

| File | Change |
|------|--------|
| `_pages/blog.md` | Rewrite with sidebar+list layout; `<script>` with `relative_url` at bottom |
| `_layouts/post.html` | Rewrite with two-column layout; `<script>` with `relative_url` at bottom |
| `_sass/_variables.scss` | Add warm minimal color variables |
| `_sass/_blog.scss` | New partial; includes `.page__content:has(.post-body)` override |
| `assets/css/main.scss` | Add `@import "blog"` at end of file |
| ~~`_includes/reading-time.html`~~ | Not needed — reading time inlined directly in `post.html` using `content` variable |
| `_includes/toc.html` | New: static HTML only — `<nav id="toc">` with toggle and empty list |
| `assets/js/blog.js` | New: category filter + TOC + scroll highlight + lazy load + figure wrap + lightbox |
| `_config.yml` | Add posts defaults entry under existing `defaults:` key |

---

## 10. Out of Scope

- Homepage (`_pages/about.md`) — no changes
- Google Scholar citation integration — no changes
- Migration of existing HTML posts to Markdown
- Pagination
- Search functionality
- Comments system
- Dark mode
- Lightbox focus trapping / full WCAG compliance
- `:has()` fallback for older browsers
