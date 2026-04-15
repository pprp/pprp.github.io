(function () {
  function getRenderableMermaidBlocks() {
    return Array.from(
      document.querySelectorAll(
        "pre code.language-mermaid, .highlighter-rouge code.language-mermaid, .language-mermaid code"
      )
    );
  }

  function loadMermaidScript() {
    if (window.mermaid) {
      return Promise.resolve(window.mermaid);
    }

    return new Promise(function (resolve, reject) {
      var existing = document.querySelector('script[data-mermaid-loader="true"]');
      if (existing) {
        existing.addEventListener("load", function () {
          resolve(window.mermaid);
        });
        existing.addEventListener("error", reject);
        return;
      }

      var script = document.createElement("script");
      script.src = "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js";
      script.async = true;
      script.dataset.mermaidLoader = "true";
      script.onload = function () {
        resolve(window.mermaid);
      };
      script.onerror = reject;
      document.head.appendChild(script);
    });
  }

  function renderBlocks(mermaid) {
    var blocks = getRenderableMermaidBlocks();
    if (!blocks.length) {
      return;
    }

    mermaid.initialize({
      startOnLoad: false,
      theme: "default",
      securityLevel: "loose",
      fontFamily: "inherit",
      flowchart: {
        htmlLabels: true,
        useMaxWidth: true,
        curve: "basis",
      },
      sequence: {
        useMaxWidth: true,
      },
    });

    blocks.forEach(function (code, index) {
      var source = code.textContent.trim();
      if (!source) {
        return;
      }

      var target =
        code.closest(".highlighter-rouge") ||
        code.closest("pre") ||
        code.parentElement;

      if (!target || target.dataset.mermaidProcessed === "true") {
        return;
      }

      var wrapper = document.createElement("div");
      wrapper.className = "mermaid-block";

      var diagram = document.createElement("div");
      diagram.className = "mermaid";
      diagram.textContent = source;
      diagram.id = "mermaid-diagram-" + index;

      wrapper.appendChild(diagram);
      target.dataset.mermaidProcessed = "true";
      target.replaceWith(wrapper);
    });

    mermaid.run({
      nodes: document.querySelectorAll(".mermaid-block .mermaid"),
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    if (!getRenderableMermaidBlocks().length) {
      return;
    }

    loadMermaidScript()
      .then(function (mermaid) {
        if (!mermaid) {
          return;
        }
        renderBlocks(mermaid);
      })
      .catch(function (error) {
        console.error("Failed to initialize Mermaid", error);
      });
  });
})();
