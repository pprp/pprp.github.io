# State-Centric Serving Review Package

This directory is a pre-publication review package for the long-form blog draft on state-centric serving.

It intentionally does **not** modify `_posts/` yet.

## Contents

- `blog.zh.md`
  Chinese long-form draft written in a paper-style structure.

- `blog.en.md`
  English counterpart aligned to the same section order, figures, and claims.

- `references.bib`
  Expanded bibliography covering model cards, serving papers, memory-system papers, and benchmark papers.

- `data/`
  CSV files retained from the initial draft package.

- `assets/`
  Review-ready figures. Quantitative plots from the original package are retained; the structural diagrams were regenerated in this round.

- `generate_figures.py`
  Generates the draw.io source and the corresponding SVG/PNG figure assets from one declarative spec.

- `figures.drawio`
  Editable draw.io source generated from the same figure spec.

## What changed in this round

1. The essay was reframed from a short opinion piece into a research-style blog.
2. The argument is now organized around service horizon, serving constraints, memory architecture, evaluation, and speculative state artifacts.
3. The diagram style was rebuilt around a cleaner, academic-tech visual system with shared color semantics and editable source generation.
4. The bilingual drafts now follow the same section numbering so they can be reviewed side by side.
5. A second detail pass expanded the main argument with concrete coding-agent scenarios, serving-mechanism explanations, memory-stack analogies, evaluation examples, and state-artifact governance caveats.
6. A list-compression pass removed ordinary bullet/numbered lists longer than four items, replacing them with prose, grouped tables, and flow-line explanations.

## Review focus

If you are reviewing the package, the highest-value questions are:

1. Is the central thesis too aggressive, too weak, or about right?
2. Which sections still feel speculative beyond the current evidence base?
3. Which figures help, and which ones still feel too dense?
4. Should the eventual published version stay this research-heavy, or be shortened before moving into `_posts/`?
