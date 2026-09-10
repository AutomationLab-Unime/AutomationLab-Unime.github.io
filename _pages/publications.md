---
layout: page
permalink: /publications/
title: publications
description: Publications of the lab, kept up to date from OpenAlex.
nav: true
nav_order: 2

_styles: |
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
  #publications .bibliography > li .badges {
    margin-top: 0.5rem;
  }
---

{::nomarkdown}

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
  <button id="pub-load-more" class="btn btn-sm z-depth-0" type="button" hidden>Load more</button>
</div>

<script>
  (function () {
    "use strict";

    var LIST_LIMIT = 20;
    var STEP = 20;

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
        current = { header: el, items: [] };
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
    });

    items.forEach(function (li) {
      var titleEl = li.querySelector(".title");
      var linksEl = li.querySelector(".links");
      if (!titleEl || !linksEl) {
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
      return (value || "").toLowerCase().replace(/\s+/g, " ").trim();
    }

    function render() {
      var query = norm(search ? search.value : "");
      var limit = query ? Infinity : LIST_LIMIT;
      var visible = 0;
      groups.forEach(function (group) {
        var shown = 0;
        group.items.forEach(function (li) {
          var match = !query || norm(li.textContent).indexOf(query) !== -1;
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
        ? visible + " result(s)"
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
      search.addEventListener("input", render);
    }

    render();
  })();
</script>

{:/nomarkdown}