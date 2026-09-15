---
layout: about
title: Home
permalink: /
subtitle: University of Messina

profile:
  align: right
  image: logo.png
  image_circular: false
  more_info: >
    <p>University of Messina, Department of Engineering</p>
    <p>Block B, 3rd Floor, Room 333</p>

selected_papers: false
social: false

announcements:
  enabled: false

latest_posts:
  enabled: false

_styles: |
  .home-hero {
    position: relative;
    margin: -2rem -2rem 2rem;
    padding: 3.5rem 2rem 3rem;
    border-radius: 0;
    background: linear-gradient(135deg, #1a3a4a 0%, #0d253f 100%);
    color: #ffffff;
    overflow: hidden;
  }
  .home-hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background: url('/assets/img/lab.jpg') center/cover no-repeat;
    opacity: 0.35;
  }
  .home-hero > * { position: relative; z-index: 1; }
  .home-hero h1 {
    margin: 0 0 0.4rem;
    font-size: 1.8rem;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: -0.02em;
  }
  .home-hero .hero-sub {
    margin: 0 0 1.2rem;
    font-size: 1rem;
    color: rgba(255,255,255,0.8);
  }
  .home-hero p {
    margin: 0;
    color: rgba(255,255,255,0.92);
    line-height: 1.65;
    max-width: 42rem;
  }
  .home-section-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.25rem;
    margin-top: 2.5rem;
  }
  .home-section-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    text-decoration: none;
    color: inherit;
    background-color: var(--global-card-bg-color);
    border: 1px solid var(--global-divider-color);
    border-radius: 0.75rem;
    padding: 1.5rem 1rem;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  .home-section-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
  }
  .home-section-card .card-emoji {
    font-size: 2rem;
    line-height: 1;
    margin-bottom: 0.6rem;
  }
  .home-section-card h3 {
    margin: 0;
    font-size: 1.05rem;
    font-weight: 600;
    color: var(--global-text-color);
  }
  .home-section-card:hover h3 {
    color: var(--global-theme-color);
  }
---

<div class="home-hero">
  <h1>Automation and Robotics Laboratory</h1>
  <p class="hero-sub">Department of Engineering</p>
  <p>Developing bio-inspired models and intelligent control systems for autonomous robots, with a particular emphasis on spiking neural networks and locomotion control in legged and mobile platforms.</p>
</div>

The Automation and Robotics Laboratory is fully equipped to support teaching, seminars, internship activities, and thesis supervision for engineering students, all centered around the topics covered in the courses on Industrial Automation and Robotics and Bio-Inspired Robotics. Research activities at the lab focus on developing models for locomotion control in legged robots and on implementing feedforward, recurrent, and spiking neural networks for the control of mobile robots.

Key activities include laboratory sessions for the courses on Industrial Automation and Robotics and Bio-Inspired Robotics, as well as lectures and seminars on related subjects. The lab also hosts internal internship placements and thesis projects for engineering students, with topics closely tied to industrial automation, robotics, and bio-inspired systems. Ongoing research explores biorobotics and locomotion control in legged robots, with a particular emphasis on the development of bio-inspired models based on spiking neural networks for navigation control in mobile robots.

<div class="home-section-grid">
  <a class="home-section-card" href="/teaching/">
    <span class="card-emoji">&#x1F393;</span>
    <h3>Teaching</h3>
  </a>
  <a class="home-section-card" href="/publications/">
    <span class="card-emoji">&#x1F4D6;</span>
    <h3>Publications</h3>
  </a>
  <a class="home-section-card" href="/projects/">
    <span class="card-emoji">&#x1F4C8;</span>
    <h3>Projects</h3>
  </a>
</div>
