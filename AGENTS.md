# Repository Guidelines

## Project Structure & Module Organization

This repo is a Jekyll-based personal site. Core content lives in `_pages/` for standalone pages and `_posts/` for dated blog posts named `YYYY-MM-DD-slug.md`. Shared templates are in `_layouts/` and `_includes/`, site data is in `_data/`, and styling is split between `assets/css/main.scss` and `_sass/` partials. Static media belongs in `images/`; supporting docs and design notes live in `docs/`. The `google_scholar_crawler/` folder is a separate Python utility for citation data. Treat `_site/`, `vendor/`, `.bundle/`, and `.sass-cache/` as generated output, not source.

Do not use SVG as a plotted figure format under `images/`. Keep editable diagrams as `.drawio` source files and publish rendered figures as `.png`.

博客最下方应该添加引用，仿照：

```
@misc{dong2025agentmem,
    author = {Dong, Peijie},
    title = {LLM Agent 记忆管理方案},
    year = {2025},
    month = aug,
    day = {7},
    howpublished = {\url{https://pprp.github.io/tech/agentmem/}},
    url = {https://pprp.github.io/tech/agentmem/},
    urldate = {2026-04-28},
    note = {Blog post. Accessed: 2026-04-28},
    language = {Chinese}
}
```

## Build, Test, and Development Commands

- `bash run_server.sh` - installs Ruby gems into `vendor/bundle` and starts the local Jekyll live-reload server.
- `bundle exec jekyll build` - performs a full production-style build into `_site/`.
- `bundle exec jekyll serve --livereload` - useful when you want direct control over the dev server flags.
- `python3 -m venv .venv && source .venv/bin/activate && pip install -r google_scholar_crawler/requirements.txt` - sets up the crawler environment.
- `GOOGLE_SCHOLAR_ID=... python3 google_scholar_crawler/main.py` - refreshes scholar JSON when working on citation automation.

## Coding Style & Naming Conventions

Follow the style already present in each file. Use YAML front matter on every page and post. Keep page, include, and asset names lowercase with hyphens where possible; SCSS partials keep the leading underscore convention (for example `_modern-enhancements.scss`). In SCSS, preserve the existing 4-space indentation and grouped selector style. Prefer editing source files such as `assets/css/main.scss` or `_sass/*.scss`; avoid hand-editing generated output in `_site/`.

## Testing Guidelines

There is no formal automated test suite yet. Validate changes by running `bundle exec jekyll build` and then checking the site locally in the browser. For UI changes, review `/`, `/blog/`, and any edited post or page on both desktop and mobile widths. For crawler work, confirm the script writes expected data to `results/gs_data.json`.

## Commit & Pull Request Guidelines

Recent history uses short, imperative commit subjects such as `Fix image paths to use relative URLs` and `Add concept images to Intent Canvas blog posts`. Keep commits focused, capitalized, and free of trailing periods. PRs should explain the user-visible change, list touched paths, link the related issue when applicable, and include screenshots for layout or styling updates.
