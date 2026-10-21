---
layout: page
title: Projects
permalink: /projects/
nav: true
nav_order: 3

_styles: |
  .post-header {
    display: none;
  }
  .projects-groups {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 2rem;
  }
  .projects-group {
    margin-bottom: 2.5rem;
  }
  /* Collapsed groups shrink to their pill so the pills flow side by side. */
  .projects-group.collapsed {
    margin-bottom: 0;
  }
  .projects-group-header {
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
    cursor: pointer;
    user-select: none;
    transition: filter 0.2s ease;
  }
  .projects-group-header:hover {
    color: #ffffff;
    filter: brightness(0.92);
  }
  .projects-group-header i {
    font-size: 0.9rem;
  }
  .projects-group-title {
    margin: 0;
    font-size: inherit;
    font-weight: inherit;
    color: inherit;
  }
  .projects-count {
    background-color: rgba(255, 255, 255, 0.25);
    border-radius: 999px;
    padding: 0.15rem 0.6rem;
    font-size: 0.85rem;
    font-weight: 600;
  }
  .projects-group.collapsed .projects-grid {
    display: none;
  }
  /* Expanded: the group takes the full row and the grid drops below the pills. */
  .projects-group:not(.collapsed) {
    flex: 1 0 100%;
  }
  .projects-group:not(.collapsed) .projects-group-header {
    margin-bottom: 1.25rem;
  }
  .projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(14rem, 1fr));
    gap: 1.5rem;
  }
  .projects-card {
    display: flex;
    flex-direction: column;
    text-align: center;
    background-color: var(--global-card-bg-color);
    border: 1px solid var(--global-divider-color);
    border-radius: 0.75rem;
    padding: 1.25rem 1rem;
  }
  .projects-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
  }
  .projects-title {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
    margin: 0.25rem 0;
    font-size: 1.05rem;
    line-height: 1.35;
    color: var(--global-text-color);
  }
  .projects-title a {
    color: var(--global-theme-color);
    text-decoration: none;
  }
  .projects-title a:hover {
    text-decoration: underline;
  }
  .projects-body {
    display: flex;
    flex-direction: column;
    justify-content: center;
    flex-grow: 1;
    margin: 0.5rem 0;
  }
  .projects-bottom {
    display: flex;
    align-items: flex-end;
    gap: 0.75rem;
    padding-top: 0.75rem;
  }
  .projects-cdl {
    margin: 0;
    font-size: 0.8rem;
    color: var(--global-text-color-light);
    text-align: left;
  }
  .projects-author {
    margin: 0;
    font-size: 0.8rem;
    color: var(--global-text-color-light);
  }
  .projects-year {
    margin: 0 0 0 auto;
    font-size: 0.8rem;
    color: var(--global-text-color-light);
    align-self: flex-end;
  }
---

{::nomarkdown}

<div class="projects-groups">
{% for group in site.data.projects.groups %}
<div class="projects-group collapsed">
  <div class="projects-group-header" tabindex="0" role="button" aria-expanded="false">
    <i class="fa-solid fa-diagram-project"></i>
    <h2 class="projects-group-title">{{ group.title }}</h2>
    <span class="projects-count">{{ group.items | size }}</span>
  </div>

  <div class="projects-grid">
    {% for item in group.items %}
    <div class="projects-card">
      <h3 class="projects-title">
        <a href="{{ item.link }}" title="{{ item.title }}">{{ item.title }}</a>
      </h3>
      {% if item.cdl %}
      <div class="projects-body">
        <p class="projects-author">{{ item.author }}</p>
      </div>
      <div class="projects-bottom">
        <p class="projects-cdl">CdL: {{ item.cdl }}</p>
        {% if item.year %}<p class="projects-year">{{ item.year }}</p>{% endif %}
      </div>
      {% else %}
      <div class="projects-body">
        <p class="projects-author">{{ item.author }}</p>
      </div>
      <div class="projects-bottom">
        {% if item.year %}<p class="projects-year">{{ item.year }}</p>{% endif %}
      </div>
      {% endif %}
    </div>
    {% endfor %}
  </div>
</div>
{% endfor %}
</div>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.projects-group-header').forEach(function(header) {
      header.addEventListener('click', function() {
        var group = header.parentElement;
        var expanded = header.getAttribute('aria-expanded') === 'true';
        header.setAttribute('aria-expanded', expanded ? 'false' : 'true');
        group.classList.toggle('collapsed', expanded);
      });
      header.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          header.click();
        }
      });
    });
  });
</script>

{:/nomarkdown}
