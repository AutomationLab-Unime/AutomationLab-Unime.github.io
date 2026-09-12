---
layout: page
permalink: /people/
title: People
nav: true
nav_order: 7

_styles: |
  .post-header {
    display: none;
  }
  .people-section {
    color: var(--global-theme-color);
    border-bottom: 1px solid var(--global-divider-color);
    padding-bottom: 0.5rem;
    margin-top: 2rem;
    margin-bottom: 1.5rem;
  }
  .people-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 1.5rem;
    justify-content: center;
  }
  .people-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 12rem;
    text-align: center;
    background-color: var(--global-card-bg-color);
    border: 1px solid var(--global-divider-color);
    border-radius: 0.75rem;
    padding: 1.25rem 1rem;
  }
  .people-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
  }
  .people-avatar {
    width: 7rem;
    height: 7rem;
    object-fit: cover;
    border-radius: 50%;
    margin-bottom: 0.75rem;
  }
  .people-avatar-fallback {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background-color: var(--global-theme-color);
    color: #ffffff;
    font-size: 2rem;
    font-weight: 600;
    text-transform: uppercase;
  }
  .people-name {
    margin: 0.25rem 0;
    font-size: 1.05rem;
    color: var(--global-text-color);
  }
  .people-role {
    margin: auto 0 0;
    padding-top: 0.5rem;
    font-size: 0.85rem;
    color: var(--global-text-color-light);
  }
---

{::nomarkdown}

{% for group in site.data.people.groups %}

<h2 class="people-section">{{ group.title }}</h2>

<div class="people-grid">
  {% for member in group.members %}
  <div class="people-card">
    {% if member.image %}
    <img src="{{ member.image | relative_url }}" alt="{{ member.name }} {{ member.surname }}" class="people-avatar">
    {% else %}
    <div class="people-avatar people-avatar-fallback">{{ member.name | slice: 0 }}{{ member.surname | slice: 0 }}</div>
    {% endif %}
    <h3 class="people-name">{{ member.name }} {{ member.surname }}</h3>
    <p class="people-role">{{ member.role }}</p>
  </div>
  {% endfor %}
</div>

{% endfor %}

{:/nomarkdown}