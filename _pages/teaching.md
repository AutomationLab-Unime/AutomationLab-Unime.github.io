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
  .teaching-degree {
    margin: 0.25rem 0;
    font-size: 0.9rem;
    color: var(--global-text-color);
  }
  .teaching-professor {
    margin: 0.25rem 0 0;
    font-size: 0.8rem;
    color: var(--global-text-color-light);
  }
---

{::nomarkdown}

<div class="teaching-grid">
  {% for item in site.data.teaching.items %}
  <div class="teaching-card">
    <h3 class="teaching-title">
      <a href="{{ item.link }}">{{ item.title }}</a>
    </h3>
    <p class="teaching-degree">{{ item.degree }}</p>
    <p class="teaching-professor">Docente: {{ item.professor }}</p>
  </div>
  {% endfor %}
</div>

{:/nomarkdown}