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
  .projects-group {
    margin-bottom: 2.5rem;
  }
  .projects-group-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    color: var(--global-theme-color);
    border-bottom: 1px solid var(--global-divider-color);
    padding-bottom: 0.5rem;
    margin-bottom: 1.5rem;
    cursor: pointer;
    user-select: none;
    transition: color 0.2s ease;
  }
  .projects-group-header:hover {
    color: var(--global-hover-color);
  }
  .projects-group-title {
    margin: 0;
    font-size: 1.25rem;
    font-weight: 600;
  }
  .projects-group-toggle {
    font-size: 1rem;
    line-height: 1;
    transition: transform 0.2s ease;
  }
  .projects-group.collapsed .projects-group-toggle {
    transform: rotate(0deg);
  }
  .projects-group .projects-group-toggle {
    transform: rotate(90deg);
  }
  .projects-group.collapsed .projects-grid {
    display: none;
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

{% for group in site.data.projects.groups %}
<div class="projects-group collapsed">
  <div class="projects-group-header" tabindex="0" role="button" aria-expanded="false">
    <span class="projects-group-toggle"><i class="fa-solid fa-chevron-right"></i></span>
    <h2 class="projects-group-title">{{ group.title }}</h2>
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
