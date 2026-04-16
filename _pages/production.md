---
layout: default
title: "Production"
permalink: /production/
author_profile: false
---

<div class="production">
  <section class="production__hero">
    <p class="production__eyebrow">Production</p>
    <h1>Selected products and tools I built over the years</h1>
    <p>
      This page collects projects across AI-native creation, markdown authoring, academic communication,
      annotation workflows, and desktop software. Some are polished products, others are compact tools built
      to remove friction from a specific workflow.
    </p>

    <div class="production__signals">
      <span>AI-native creation</span>
      <span>Writing tools</span>
      <span>Research workflows</span>
      <span>Desktop software</span>
    </div>
  </section>

  <div class="production__grid">
    <article class="production__card">
      <div class="production__mark" aria-hidden="true">SD</div>
      <div class="production__body">
        <p class="production__tag">AI Agent Powered Drawer</p>
        <h2>SoulDraw</h2>
        <p class="production__copy">
          An AI-first drawing product built around the idea that visual creation should feel like collaboration,
          not manual canvas micromanagement.
        </p>
        <p class="production__detail">
          SoulDraw turns intent into diagrams and structured visuals faster by pairing a drawing workspace with an
          embedded agent loop.
        </p>

        <div class="production__actions">
          <a class="production__button production__button--solid" href="https://drawai.md" target="_blank" rel="noopener">Visit site</a>
        </div>
      </div>
    </article>

    <article class="production__card">
      <div class="production__mark" aria-hidden="true">MF</div>
      <div class="production__body">
        <p class="production__tag">Markdown editor</p>
        <h2>MarkFlow</h2>
        <p class="production__copy">
          A Typora-inspired WYSIWYG markdown editor built on CodeMirror 6, designed to let users write in flow and
          publish anywhere.
        </p>
        <p class="production__detail">
          Markdown syntax fades into the background while headings, emphasis, links, tasks, and code render inline.
          The project also includes source toggle, file open/save, and Electron desktop packaging.
        </p>

        <div class="production__actions">
          <a class="production__button production__button--solid" href="https://github.com/pprp/MarkFlow" target="_blank" rel="noopener">Open repo</a>
        </div>
      </div>
    </article>

    <article class="production__card">
      <div class="production__mark" aria-hidden="true">P2B</div>
      <div class="production__body">
        <p class="production__tag">Academic communication</p>
        <h2>Paper2Blog</h2>
        <p class="production__copy">
          A web application that transforms academic papers into readable blog posts with AI, while preserving the
          structure and intent of the source material.
        </p>
        <p class="production__detail">
          It handles PDF ingestion, figure extraction, bilingual generation, and markdown output, making research
          results easier to share with a broader audience.
        </p>

        <div class="production__actions">
          <a class="production__button production__button--solid" href="https://github.com/pprp/Paper2Blog" target="_blank" rel="noopener">Open repo</a>
        </div>
      </div>
    </article>

    <article class="production__card">
      <div class="production__mark" aria-hidden="true">CL</div>
      <div class="production__body">
        <p class="production__tag">LLM utility</p>
        <h2>ClipLLM</h2>
        <p class="production__copy">
          An experiment in using the clipboard as a lightweight bridge between users and language models.
        </p>
        <p class="production__detail">
          The tool explores a minimal interaction pattern: read from the clipboard, hand the content to an LLM, then
          write results back into the same ambient workflow without forcing users into a heavy interface.
        </p>

        <div class="production__actions">
          <a class="production__button production__button--solid" href="https://github.com/pprp/ClipLLM" target="_blank" rel="noopener">Open repo</a>
        </div>
      </div>
    </article>

    <article class="production__card">
      <div class="production__mark" aria-hidden="true">LA</div>
      <div class="production__body">
        <p class="production__tag">Data annotation</p>
        <h2>landmark_annotation</h2>
        <p class="production__copy">
          A keypoint annotation tool built for teams working on landmark detection without a simple, dedicated
          desktop workflow.
        </p>
        <p class="production__detail">
          Inspired by the ease of bounding-box tooling, it focuses on fast image switching, quick saving, and an
          annotation format suited for normalized keypoint coordinates.
        </p>

        <div class="production__actions">
          <a class="production__button production__button--solid" href="https://github.com/pprp/landmark_annotation" target="_blank" rel="noopener">Open repo</a>
        </div>
      </div>
    </article>

    <article class="production__card">
      <div class="production__mark" aria-hidden="true">QP</div>
      <div class="production__body">
        <p class="production__tag">Desktop graphics software</p>
        <h2>QPainter</h2>
        <p class="production__copy">
          A C++/Qt drawing project covering core vector-style interactions such as shapes, Bezier curves, text, zoom,
          file operations, and SVG-oriented workflows.
        </p>
        <p class="production__detail">
          It started as an internship project and became a compact exercise in UI construction, drawing primitives,
          and desktop interaction design.
        </p>

        <div class="production__actions">
          <a class="production__button production__button--solid" href="https://github.com/pprp/QPainter" target="_blank" rel="noopener">Open repo</a>
        </div>
      </div>
    </article>
  </div>
</div>
