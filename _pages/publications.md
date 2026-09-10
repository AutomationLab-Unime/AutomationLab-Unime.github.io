---
layout: page
permalink: /publications/
title: publications
description: Publications of the lab, kept up to date from OpenAlex.
nav: true
nav_order: 2

_styles: |
  .pub-toolbar {
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
---

{::nomarkdown}

<div class="pub-toolbar">
  <input type="search" id="pub-search" placeholder="Cerca per titolo, autore, anno ..." aria-label="Search publications">
  <div class="pub-actions">
    <span id="pub-count" role="status"></span>
    <button id="pub-load-more" class="btn btn-sm z-depth-0" type="button" hidden>Carica altri</button>
  </div>
</div>

<div id="publications" class="publications">
  {% bibliography %}
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
    for (var i = 0; i < container.children.length; i++) {
      var el = container.children[i];
      if (el.tagName === "H2") {
        current = { header: el, items: [] };
        groups.push(current);
      } else if (el.classList && el.classList.contains("bibliography")) {
        var kids = el.children;
        for (var j = 0; j < kids.length; j++) {
          if (!current) {
            current = { header: null, items: [] };
            groups.push(current);
          }
          current.items.push(kids[j]);
        }
      }
    }

    var items = [];
    groups.forEach(function (group) {
      items.push.apply(items, group.items);
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
        ? visible + " risultato/i"
        : "Mostrati " + visible + " di " + items.length;
      moreBtn.hidden = !!(query || visible >= items.length);
      moreBtn.textContent = "Carica altri (" + (items.length - visible) + " da mostrare)";
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