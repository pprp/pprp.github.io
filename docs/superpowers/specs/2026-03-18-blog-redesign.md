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
- Applied via new SCSS variables in `_sass/_variables.scss` and a new `_sass/_blog.scss` partial

---

## 2. Blog Index Page (`_pages/blog.md`)

Replace the current plain `<ul>` list with a two-panel layout:

**Left sidebar (fixed width ~200px):**
- Site categories derived from post front matter
- Each category shows post count
- Clicking filters the post list (JS, no page reload)
- "All" option at top selected by default

**Right post list:**
- Each post shows: title, date, category tags, estimated reading time
- Sorted by date descending
- No excerpt (keep it dense and scannable)
- Pagination: 10 posts per page using `jekyll-paginate`

---

## 3. Post Layout (`_layouts/post.html`)

Replace the minimal current layout with:

**Structure:**
- Full-width header: title, date, tags, reading time
- Two-column body:
  - Left: sticky TOC (generated from `##` and `###` headings via JS)
  - Right: post content (max-width ~720px)
- Footer: prev/next post navigation

**TOC behavior:**
- Auto-generated from headings in the post
- Highlights current section as user scrolls (IntersectionObserver)
- Hidden on mobile (collapses to a toggle button)

---

## 4. Post Authoring

- All new posts written in Markdown with front matter:
  ```yaml
  ---
  layout: post
  title: 'Post Title'
  date: 2025-08-05 11:00:00 +0800
  categories: [llm, compression]
  ---
  ```
- Existing HTML posts continue to work (layout wraps them)
- Reading time auto-calculated from word count in a Liquid include

---

## 5. Image Support

- Standard Markdown images `![caption](url)` rendered with:
  - `loading="lazy"` attribute
  - `max-width: 100%` responsive sizing
  - Caption rendered below image (from alt text)
- Lightbox: clicking an image opens it full-screen
  - Implemented with a minimal vanilla JS lightbox (~50 lines, no external dependency)
  - Keyboard ESC to close

---

## 6. Performance

- Remove inline Tailwind CSS and Google Fonts from existing HTML posts (migrate to Markdown)
- No CDN JS libraries added (lightbox and TOC are vanilla JS)
- Existing `compress_html` plugin stays active
- Images served from `/images/posts/` with descriptive filenames

---

## 7. Files Changed

| File | Change |
|------|--------|
| `_pages/blog.md` | Rewrite with sidebar+list layout |
| `_layouts/post.html` | Rewrite with TOC sidebar + image support |
| `_sass/_variables.scss` | Add warm minimal color variables |
| `_sass/_blog.scss` | New partial for blog index + post styles |
| `_sass/_base.scss` | Import `_blog.scss` |
| `_includes/reading-time.html` | New include for reading time calculation |
| `_includes/toc.html` | New include for TOC scaffold (JS fills it) |
| `assets/js/blog.js` | New: TOC highlight + category filter + lightbox |
| `_config.yml` | Add paginate config, post defaults |

---

## 8. Out of Scope

- Homepage (`_pages/about.md`) — no changes
- Google Scholar citation integration — no changes
- Search functionality
- Comments system
- Dark mode
