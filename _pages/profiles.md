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
  .people-pill {
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
    margin: 2.5rem 0 1rem;
  }
  .people-pill i {
    font-size: 0.9rem;
  }
  .people-count {
    background-color: rgba(255, 255, 255, 0.25);
    border-radius: 999px;
    padding: 0.15rem 0.6rem;
    font-size: 0.85rem;
    font-weight: 600;
  }
  .people-panel {
    background-color: var(--global-card-bg-color);
    background-color: color-mix(in srgb, var(--global-theme-color) 6%, transparent);
    border: 1px solid var(--global-divider-color);
    border-radius: 1rem;
    padding: 1.5rem;
  }
  .people-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(20rem, 1fr));
    gap: 1.25rem;
  }
  .people-card {
    display: flex;
    align-items: center;
    gap: 1rem;
    text-align: left;
    background-color: var(--global-card-bg-color);
    border: 1px solid var(--global-divider-color);
    border-radius: 0.75rem;
    padding: 1rem 1.25rem;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  .people-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
  }
  .people-avatar {
    width: 5rem;
    height: 5rem;
    flex-shrink: 0;
    object-fit: cover;
    border-radius: 50%;
  }
  .people-avatar-fallback {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background-color: var(--global-theme-color);
    color: #ffffff;
    font-size: 1.5rem;
    font-weight: 600;
    text-transform: uppercase;
  }
  .people-info {
    flex: 1;
    min-width: 0;
  }
  .people-name {
    margin: 0;
    font-size: 1.05rem;
    color: var(--global-text-color);
  }
  .people-role {
    margin: 0.2rem 0 0;
    font-size: 0.85rem;
    color: var(--global-text-color-light);
  }
  .people-contacts {
    display: flex;
    gap: 0.5rem;
    margin-top: 0.6rem;
  }
  .people-email,
  .people-orcid {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 1.9rem;
    height: 1.9rem;
    font-size: 1rem;
    color: var(--global-theme-color);
    border: 1px solid var(--global-divider-color);
    border-radius: 50%;
    transition: color 0.2s ease, background-color 0.2s ease;
  }
  .people-orcid {
    font-size: 1.15rem;
  }
  .people-email:hover,
  .people-orcid:hover {
    color: #ffffff;
    background-color: var(--global-theme-color);
  }
---

{::nomarkdown}

{% for group in site.data.people.groups %}
<section class="people-group">
  <h2 class="people-pill">
    <i class="fa-solid fa-user"></i>
    {{ group.title }}
    <span class="people-count">{{ group.members | size }}</span>
  </h2>

  <div class="people-panel">
    <div class="people-grid">
      {% for member in group.members %}
      <div class="people-card">
        {% if member.image %}
        <img src="{{ member.image | relative_url }}" alt="{{ member.name }} {{ member.surname }}" class="people-avatar">
        {% else %}
        <div class="people-avatar people-avatar-fallback">{{ member.name | slice: 0 }}{{ member.surname | slice: 0 }}</div>
        {% endif %}
        <div class="people-info">
          <h3 class="people-name">{{ member.name }} {{ member.surname }}</h3>
          <p class="people-role">{{ member.role }}</p>
          {% if member.email or member.orcid %}
          <div class="people-contacts">
            {% if member.email %}
            <a class="people-email" href="mailto:{{ member.email }}" title="{{ member.email }}" aria-label="Email {{ member.name }} {{ member.surname }}">
              <i class="fa-solid fa-envelope"></i>
            </a>
            {% endif %}
            {% if member.orcid %}
            {% assign orcid_id = member.orcid | remove: "https://" | remove: "http://" %}
            {% assign orcid_id = orcid_id | remove: "orcid.org/" %}
            <a class="people-orcid" href="https://orcid.org/{{ orcid_id }}" target="_blank" rel="noopener noreferrer" title="{{ orcid_id }}" aria-label="ORCID {{ member.name }} {{ member.surname }}">
              <i class="ai ai-orcid"></i>
            </a>
            {% endif %}
          </div>
          {% endif %}
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</section>
{% endfor %}

{:/nomarkdown}
