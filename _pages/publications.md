---
layout: page
permalink: /publications/
title: Publications
nav: true
nav_order: 2

_styles: |
  .post-header {
    display: none;
  }
  .pub-header {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1.5rem;
  }
  #pub-search {
    flex: 1 1 16rem;
    padding: 0.5rem 0.75rem;
    font-size: 0.95rem;
    color: var(--global-text-color);
    background-color: var(--global-bg-color);
    border: 1px solid var(--global-divider-color);
    border-radius: 0.5rem;
  }
  #pub-count {
    font-size: 0.85rem;
    color: var(--global-text-color-light);
    white-space: nowrap;
  }
  #pub-load-more {
    font-size: 1.1rem;
    padding: 0.625rem 1.75rem;
    font-weight: 600;
    color: var(--global-theme-color);
    border: 2px solid var(--global-theme-color);
    border-radius: 0.5rem;
  }
  .pub-footer {
    display: flex;
    justify-content: center;
    margin-top: 1.5rem;
  }
  #publications ol.bibliography {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  #publications .bibliography > li {
    background-color: var(--global-card-bg-color);
    border: 1px solid var(--global-divider-color);
    border-radius: 0.75rem;
    padding: 1.25rem 1.25rem;
    margin-bottom: 1rem;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
  }
  #publications .bibliography > li:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
  }
  #publications .bibliography > li .row {
    margin-left: 0;
    margin-right: 0;
  }
  #publications .bibliography > li .col-sm-8,
  #publications .bibliography > li .col-sm-10 {
    width: 100%;
    flex: 0 0 100%;
    max-width: 100%;
    padding-left: 0;
    padding-right: 0;
  }
  #publications .bibliography > li .title {
    margin: 0 0 0.25rem;
    font-size: 1.05rem;
    font-weight: 500;
  }
  #publications .bibliography > li .title a {
    color: var(--global-theme-color);
    text-decoration: none;
  }
  #publications .bibliography > li .title a:hover {
    text-decoration: underline;
  }
  #publications .bibliography > li .author {
    font-size: 0.9rem;
    color: var(--global-text-color);
  }
  #publications .bibliography > li .periodical {
    font-size: 0.85rem;
    color: var(--global-text-color-light);
  }
  #publications .bibliography > li .links {
    margin-top: 0.5rem;
  }
  /* BibTeX panel opened by the "Cite" button. It reuses the theme's
     `.hidden`/`.open` toggle (same mechanism as the abstract panel). */
  #publications .bibliography > li .bibtex pre {
    padding-right: 3rem; /* leave room for the copy button */
    font-size: 0.8rem;
    line-height: 1.5;
  }
  #publications .bibliography > li .bibtex .copy {
    opacity: 1;
  }
  #publications .bibliography > li .badges {
    margin-top: 0.5rem;
  }
  #publications .bibliography > li .author > em {
    font-style: normal;
    font-weight: 700;
    border-bottom: none;
  }
  #publications .bibliography > li .author > span.more-authors.more-authors-expanded {
    border-bottom: none;
  }
  #publications > h2 {
    display: flex;
    width: fit-content;
    align-items: center;
    gap: 0.5rem;
    background-color: var(--global-theme-color);
    color: #ffffff;
    font-size: 1.1rem;
    font-weight: 600;
    line-height: 1;
    padding: 0.5rem 1.1rem;
    border-radius: 999px;
    border-bottom: none;
    margin-top: 2rem;
    margin-bottom: 1.25rem;
  }
  #publications > h2 i {
    font-size: 0.9rem;
  }
  #publications > h2 a {
    color: #ffffff;
  }
  .pub-year-count,
  #publications > h2 span.pub-year-count {
    background-color: rgba(255, 255, 255, 0.25);
    border-radius: 999px;
    padding: 0.15rem 0.6rem;
    font-size: 0.85rem;
    font-weight: 600;
    line-height: 1;
  }
  .pub-title-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background-color: var(--global-theme-color);
    color: #ffffff;
    font-size: 1.1rem;
    font-weight: 600;
    line-height: 1;
    padding: 0.5rem 1.1rem;
    border-radius: 999px;
    margin: 0 0 1.25rem;
  }
  .pub-title-pill i {
    font-size: 0.9rem;
  }
---

{::nomarkdown}

<h1 class="pub-title-pill">
  <i class="fa-solid fa-book-open"></i>
  Publications
  <span class="pub-year-count" id="pub-total-count">{% bibliography_count %}</span>
</h1>

<div class="pub-header">
  <input
    type="search"
    id="pub-search"
    placeholder="Search by title, author, year..."
    aria-label="Search publications"
  >
  <span id="pub-count" role="status"></span>
</div>

<div id="publications" class="publications">
  {% bibliography %}
</div>

<div class="pub-footer">
  <button id="pub-load-more" class="btn z-depth-0" type="button" hidden>Load more</button>
</div>

<script>
  (function () {
    "use strict";

    var PAGE_STEP = 20;
    var STEP = 20;
    var LIST_LIMIT = PAGE_STEP;

    var search = document.getElementById("pub-search");
    var counter = document.getElementById("pub-count");
    var moreBtn = document.getElementById("pub-load-more");
    var container = document.getElementById("publications");
    if (!container) {
      return;
    }

    var groups = [];
    var current = null;
    Array.prototype.forEach.call(container.children, function (el) {
      if (el.tagName === "H2") {
        var yIcon = document.createElement("i");
        yIcon.className = "fa-solid fa-calendar";
        el.insertBefore(yIcon, el.firstChild);
        var yCount = document.createElement("span");
        yCount.className = "pub-year-count";
        el.appendChild(yCount);
        current = { header: el, countEl: yCount, items: [] };
        groups.push(current);
      } else if (el.tagName === "OL" || (el.classList && el.classList.contains("bibliography"))) {
        var lis = Array.prototype.filter.call(el.children, function (child) {
          return child.tagName === "LI";
        });
        if (!current) {
          current = { header: null, items: [] };
          groups.push(current);
        }
        Array.prototype.push.apply(current.items, lis);
      }
    });

    var items = [];
    groups.forEach(function (group) {
      Array.prototype.push.apply(items, group.items);
      if (group.countEl) {
        group.countEl.textContent = group.items.length;
      }
    });

    var totalBadge = document.getElementById("pub-total-count");
    if (totalBadge && !totalBadge.textContent.trim()) {
      totalBadge.textContent = items.length;
    }
    if (totalBadge) {
      totalBadge.hidden = false;
    }

    // The BibTeX panel is rendered server-side, so it must stay out of the text
    // searched by the search box: otherwise every entry would match technical
    // keywords such as "article", "doi" or "http".
    function searchableText(li) {
      var clone = li.cloneNode(true);
      var noise = clone.querySelectorAll(".bibtex");
      for (var n = 0; n < noise.length; n++) {
        if (noise[n].parentNode) {
          noise[n].parentNode.removeChild(noise[n]);
        }
      }
      return norm(clone.textContent);
    }

    // al-folio ships this button as "Bib"; the lab site labels it "Cite".
    function setupCiteButton(li, linksEl) {
      var btn = linksEl.querySelector("a.bibtex");
      if (!btn) {
        return;
      }
      var panel = li.querySelector(".bibtex.hidden");
      var keyed = li.querySelector("[id]");
      if (!panel) {
        // No citation was generated for this entry: drop the dead button.
        if (btn.parentNode) {
          btn.parentNode.removeChild(btn);
        }
        return;
      }

      btn.textContent = "Cite";
      btn.setAttribute("title", "Show the BibTeX citation");
      btn.setAttribute("aria-label", "Show the BibTeX citation");
      btn.setAttribute("aria-expanded", "false");
      btn.setAttribute("tabindex", "0");
      // Put it after DOI/PDF instead of before them.
      linksEl.appendChild(btn);
      if (keyed && keyed.id) {
        panel.id = "bibtex-" + keyed.id;
        btn.setAttribute("aria-controls", panel.id);
      }

      // The theme's common.js toggles the panel on click; read the new state on
      // the next tick so aria-expanded stays in sync.
      btn.addEventListener("click", function () {
        window.setTimeout(function () {
          btn.setAttribute(
            "aria-expanded",
            panel.classList.contains("open") ? "true" : "false"
          );
        }, 0);
      });
      btn.addEventListener("keydown", function (event) {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          btn.click();
        }
      });
    }

    items.forEach(function (li) {
      li.__searchText = searchableText(li);

      var titleEl = li.querySelector(".title");
      var linksEl = li.querySelector(".links");
      if (!linksEl) {
        return;
      }
      setupCiteButton(li, linksEl);
      if (!titleEl) {
        return;
      }
      var htmlBtn = null;
      var links = linksEl.querySelectorAll("a");
      for (var i = 0; i < links.length; i++) {
        if (links[i].textContent.trim().toLowerCase() === "html") {
          htmlBtn = links[i];
          break;
        }
      }
      if (htmlBtn && htmlBtn.href) {
        htmlBtn.style.display = "none";
        var a = document.createElement("a");
        a.href = htmlBtn.href;
        a.target = "_blank";
        a.rel = "noopener";
        a.textContent = titleEl.textContent;
        titleEl.textContent = "";
        titleEl.appendChild(a);
      }
    });

    function norm(value) {
      return (value || "")
        .toLowerCase()
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .replace(/\s+/g, " ")
        .trim();
    }

    function render() {
      var query = norm(search ? search.value : "");
      var limit = query ? Infinity : LIST_LIMIT;
      var visible = 0;
      var matched = 0;
      groups.forEach(function (group) {
        var shown = 0;
        group.items.forEach(function (li) {
          var match = !query || (li.__searchText || "").indexOf(query) !== -1;
          if (match) {
            matched++;
          }
          var show = match && visible < limit;
          li.style.display = show ? "" : "none";
          if (show) {
            visible++;
            shown++;
          }
        });
        if (group.header) {
          group.header.style.display = shown ? "" : "none";
        }
      });
      counter.textContent = query
        ? visible + " of " + matched + " result(s)"
        : "Showing " + visible + " of " + items.length;
      moreBtn.textContent = "Load more (" + (items.length - visible) + " remaining)";
      moreBtn.hidden = !!(query || visible >= items.length);
    }

    if (moreBtn) {
      moreBtn.addEventListener("click", function () {
        LIST_LIMIT += STEP;
        render();
      });
    }
    if (search) {
      search.addEventListener("input", function () {
        if (!norm(search.value)) {
          LIST_LIMIT = PAGE_STEP;
        }
        render();
      });
    }

    render();
  })();
</script>

<script>
  (function () {
    "use strict";

    var container = document.getElementById("publications");
    if (!container) {
      return;
    }

    var SELF_LAST = {{ site.scholar.last_name | jsonify }};
    var SELF_FIRST = {{ site.scholar.first_name | jsonify }};

    function norm(value) {
      return (value || "")
        .toLowerCase()
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .replace(/[^a-z0-9 ]/g, " ")
        .replace(/\s+/g, " ")
        .trim();
    }

    var SELF_LAST_NORM = SELF_LAST.map(norm);
    var SELF_FIRST_NORM = SELF_FIRST.map(norm);

    function isSelf(first, last) {
      return SELF_LAST_NORM.indexOf(norm(last)) !== -1 && SELF_FIRST_NORM.indexOf(norm(first)) !== -1;
    }

    function boldSelfAuthors(span) {
      var text = (span.textContent || "").trim();
      var parts = text.split(", ");
      var changed = false;
      for (var i = 0; i < parts.length; i++) {
        var words = parts[i].trim().split(/\s+/);
        if (words.length < 2) {
          continue;
        }
        var last = words.pop();
        var first = words.join(" ");
        if (isSelf(first, last)) {
          var wrapped = "<strong>" + parts[i].trim() + "</strong>";
          if (span.innerHTML.indexOf(wrapped) === -1) {
            span.innerHTML = span.innerHTML.split(parts[i].trim()).join(wrapped);
            changed = true;
          }
        }
      }
      return changed;
    }

    function hideSelfAuthors(span) {
      span.classList.remove("more-authors-expanded");
      span.removeAttribute("data-bolded");
    }

    function tryBold(span, attempts, lastText) {
      if (attempts > 40) {
        return;
      }
      var text = (span.textContent || "").trim();
      if (/more author/i.test(text)) {
        if (span.hasAttribute("data-open")) {
          setTimeout(function () {
            tryBold(span, attempts + 1, "");
          }, 150);
        } else {
          hideSelfAuthors(span);
        }
        return;
      }
      boldSelfAuthors(span);
      if (text === lastText) {
        span.classList.add("more-authors-expanded");
        span.setAttribute("data-bolded", "1");
        return;
      }
      setTimeout(function () {
        tryBold(span, attempts + 1, text);
      }, 150);
    }

    container.addEventListener("click", function (event) {
      var span = event.target.closest("span.more-authors");
      if (!span) {
        return;
      }
      var opening = !span.hasAttribute("data-open");
      span.setAttribute("data-open", opening ? "1" : "");
      if (!opening) {
        hideSelfAuthors(span);
        return;
      }
      tryBold(span, 0, "");
    });
  })();
</script>

{:/nomarkdown}