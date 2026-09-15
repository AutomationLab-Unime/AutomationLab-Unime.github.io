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
  .home-highlights {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.25rem;
    margin-top: 2.5rem;
  }
  .home-highlight-card {
    padding: 1.25rem 1.2rem;
    border: 1px solid var(--global-divider-color);
    border-radius: 0.75rem;
    background: var(--global-card-bg-color);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  .home-highlight-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.1);
  }
  .home-highlight-card .card-icon {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
    color: var(--global-theme-color);
  }
  .home-highlight-card h3 {
    margin: 0 0 0.35rem;
    font-size: 0.95rem;
    font-weight: 600;
  }
  .home-highlight-card p {
    margin: 0;
    font-size: 0.85rem;
    color: var(--global-text-color-light);
    line-height: 1.55;
  }
---

<div class="home-hero">
  <h1>Automation and Robotics Laboratory</h1>
  <p class="hero-sub">Department of Engineering &middot; University of Messina</p>
  <p>Developing bio-inspired models and intelligent control systems for autonomous robots, with a particular emphasis on spiking neural networks and locomotion control in legged and mobile platforms.</p>
</div>

The Automation and Robotics Laboratory is fully equipped to support teaching, seminars, internship activities, and thesis supervision for engineering students, all centered around the topics covered in the courses on Industrial Automation and Robotics and Bio-Inspired Robotics. Research activities at the lab focus on developing models for locomotion control in legged robots and on implementing feedforward, recurrent, and spiking neural networks for the control of mobile robots.

Key activities include laboratory sessions for the courses on Industrial Automation and Robotics and Bio-Inspired Robotics, as well as lectures and seminars on related subjects. The lab also hosts internal internship placements and thesis projects for engineering students, with topics closely tied to industrial automation, robotics, and bio-inspired systems. Ongoing research explores biorobotics and locomotion control in legged robots, with a particular emphasis on the development of bio-inspired models based on spiking neural networks for navigation control in mobile robots.

<div class="home-highlights">
  <div class="home-highlight-card">
    <div class="card-icon"><i class="fa-solid fa-graduation-cap"></i></div>
    <h3>Teaching</h3>
    <p>Laboratory sessions for Industrial Automation, Bio-Inspired Robotics, and related courses.</p>
  </div>
  <div class="home-highlight-card">
    <div class="card-icon"><i class="fa-solid fa-microscope"></i></div>
    <h3>Research</h3>
    <p>Spiking neural networks, locomotion control, and bio-inspired navigation for mobile robots.</p>
  </div>
  <div class="home-highlight-card">
    <div class="card-icon"><i class="fa-solid fa-file-lines"></i></div>
    <h3>Theses &amp; Internships</h3>
    <p>Internal placements and thesis projects on automation, robotics, and AI-driven control systems.</p>
  </div>
</div>
