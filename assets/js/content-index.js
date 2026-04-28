(function () {
  function normalize(value) {
    return (value || "").toString().trim().toLowerCase();
  }

  function updateUrlTopic(topic) {
    if (!window.history || !window.URLSearchParams) return;

    var url = new URL(window.location.href);
    if (!topic || topic === "all") {
      url.searchParams.delete("topic");
    } else {
      url.searchParams.set("topic", topic);
    }
    window.history.replaceState({}, "", url.toString());
  }

  function initContentFilters(root) {
    var cards = Array.prototype.slice.call(root.querySelectorAll("[data-content-card]"));
    var search = root.querySelector("[data-content-search]");
    var buttons = Array.prototype.slice.call(root.querySelectorAll("[data-filter-value]"));
    var status = root.querySelector("[data-content-status]");
    var empty = root.querySelector("[data-content-empty]");
    var activeTopic = "all";

    if (window.URLSearchParams) {
      var params = new URLSearchParams(window.location.search);
      activeTopic = normalize(params.get("topic")) || "all";
    }

    function setActiveButton() {
      buttons.forEach(function (button) {
        button.classList.toggle("is-active", normalize(button.dataset.filterValue) === activeTopic);
      });
    }

    function applyFilter() {
      var query = normalize(search && search.value);
      var visibleCount = 0;

      cards.forEach(function (card) {
        var topics = normalize(card.dataset.topics).split(/\s+/).filter(Boolean);
        var searchable = normalize(card.dataset.searchText);
        var matchesTopic = activeTopic === "all" || topics.indexOf(activeTopic) !== -1;
        var matchesSearch = !query || searchable.indexOf(query) !== -1;
        var isVisible = matchesTopic && matchesSearch;

        card.hidden = !isVisible;
        if (isVisible) visibleCount += 1;
      });

      if (status) {
        status.textContent = visibleCount + (visibleCount === 1 ? " item" : " items");
      }
      if (empty) {
        empty.hidden = visibleCount !== 0;
      }
      setActiveButton();
    }

    buttons.forEach(function (button) {
      button.addEventListener("click", function () {
        var nextTopic = normalize(button.dataset.filterValue);
        activeTopic = activeTopic === nextTopic ? "all" : nextTopic;
        updateUrlTopic(activeTopic);
        applyFilter();
      });
    });

    if (search) {
      search.addEventListener("input", applyFilter);
    }

    if (buttons.length && !buttons.some(function (button) {
      return normalize(button.dataset.filterValue) === activeTopic;
    })) {
      activeTopic = "all";
    }

    applyFilter();
  }

  function initToc() {
    var toc = document.querySelector("[data-toc-list]");
    var content = document.querySelector(".reading-content");
    if (!toc || !content) return;

    var headings = Array.prototype.slice.call(content.querySelectorAll("h2, h3")).filter(function (heading) {
      return heading.id && heading.textContent.trim();
    });

    if (!headings.length) {
      var tocWrapper = toc.closest(".reading-toc");
      if (tocWrapper) tocWrapper.hidden = true;
      return;
    }

    var links = headings.map(function (heading) {
      var item = document.createElement("li");
      var link = document.createElement("a");

      link.href = "#" + heading.id;
      link.textContent = heading.textContent;
      link.className = "toc-depth-" + heading.tagName.slice(1);
      item.appendChild(link);
      toc.appendChild(item);
      return link;
    });

    if (!("IntersectionObserver" in window)) return;

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;

        links.forEach(function (link) {
          link.classList.toggle("is-active", link.getAttribute("href") === "#" + entry.target.id);
        });
      });
    }, {
      rootMargin: "0px 0px -65% 0px",
      threshold: 0
    });

    headings.forEach(function (heading) {
      observer.observe(heading);
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    Array.prototype.forEach.call(document.querySelectorAll("[data-content-filter]"), initContentFilters);
    initToc();
  });
}());
