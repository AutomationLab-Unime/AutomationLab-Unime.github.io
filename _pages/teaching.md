---
layout: page
permalink: /teaching/
title: Teaching
description: Course materials, schedules, and resources for classes taught.
nav: true
nav_order: 6
calendar: true

_styles: |
  .teaching-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(14rem, 1fr));
    gap: 1.5rem;
  }
  .teaching-card {
    display: flex;
    flex-direction: column;
    text-align: center;
    background-color: var(--global-card-bg-color);
    border: 1px solid var(--global-divider-color);
    border-radius: 0.75rem;
    padding: 1.25rem 1rem;
  }
  .teaching-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
  }
  .teaching-title {
    margin: 0.25rem 0;
    font-size: 1.05rem;
    color: var(--global-text-color);
  }
  .teaching-title a {
    color: var(--global-theme-color);
    text-decoration: none;
  }
  .teaching-title a:hover {
    text-decoration: underline;
  }
  .teaching-body {
    display: flex;
    flex-direction: column;
    justify-content: center;
    flex-grow: 1;
    margin: 0.5rem 0;
  }
  .teaching-degree {
    margin: 0;
    font-size: 0.9rem;
    color: var(--global-text-color);
  }
  .teaching-professor {
    margin: 0;
    font-size: 0.8rem;
    color: var(--global-text-color-light);
  }
  .teaching-bottom {
    display: flex;
    justify-content: center;
    padding-top: 0.75rem;
    margin-top: 0.75rem;
    border-top: 1px solid var(--global-divider-color);
  }
  .teaching-material {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    font-size: 0.85rem;
    color: var(--global-theme-color);
    text-decoration: none;
  }
  .teaching-material:hover {
    text-decoration: underline;
  }
  .teaching-pill {
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
    margin: 2rem 0 1.25rem;
  }
  .teaching-pill i {
    font-size: 0.9rem;
  }
  .teaching-count {
    background-color: rgba(255, 255, 255, 0.25);
    border-radius: 999px;
    padding: 0.15rem 0.6rem;
    font-size: 0.85rem;
    font-weight: 600;
  }
---

{::nomarkdown}

{% assign degree_groups = site.data.teaching.items | group_by: "degree" %}
{% for group in degree_groups %}
<section class="teaching-group">
  <h2 class="teaching-pill">
    <i class="fa-solid fa-graduation-cap"></i>
    {{ group.name }}
    <span class="teaching-count">{{ group.items | size }}</span>
  </h2>

  <div class="teaching-grid">
    {% for item in group.items %}
    <div class="teaching-card">
      <h3 class="teaching-title">
        <a href="{{ item.link }}">{{ item.title }}</a>
      </h3>
      <div class="teaching-body">
        <p class="teaching-degree">{{ item.degree }}</p>
      </div>
      <p class="teaching-professor">Docente: {{ item.professor }}</p>
      {% if item.material %}
      <div class="teaching-bottom">
        <a class="teaching-material" href="{{ item.material }}" title="{{ item.title }}">
          <i class="fa-solid fa-link"></i> Material
        </a>
      </div>
      {% endif %}
    </div>
    {% endfor %}
  </div>
</section>
{% endfor %}

{:/nomarkdown}