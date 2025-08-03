---
layout: single
permalink: /publications/
title: "Publications"
author_profile: true
---

<style>
  .year-tabs {
    margin-bottom: 1.5em;
    border-bottom: 2px solid #f2f2f2;
    padding-bottom: 10px;
  }
  .year-tabs button {
    background-color: #f2f2f2;
    border: none;
    padding: 10px 15px;
    margin-right: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
    border-radius: 5px;
    font-size: 0.9em;
  }
  .year-tabs button:hover {
    background-color: #ddd;
  }
  .year-tabs button.active {
    background-color: #007bff;
    color: white;
  }
  .pub-panel {
    display: none; /* Hide all panels by default */
  }
  .pub-panel.active {
    display: block; /* Show the active panel */
  }
</style>

{% assign postsByYear = site.publications | group_by_exp:"post", "post.date | date: '%Y'" | reverse %}

<div id="year-tabs" class="year-tabs">
  {% for year in postsByYear %}
    <button onclick="showYear('{{ year.name }}')">{{ year.name }}</button>
  {% endfor %}
</div>

<div id="pub-content">
  {% for year in postsByYear %}
    <div id="year-{{ year.name }}" class="pub-panel">
      {% for post in year.items %}
        <div style="margin-bottom: 2em; border-bottom: 1px solid #e5e5e5; padding-bottom: 1em;">
          {{ post.content }}
        </div>
      {% endfor %}
    </div>
  {% endfor %}
</div>

<script>
  function showYear(year) {
    // Hide all publication panels
    var panels = document.querySelectorAll('.pub-panel');
    panels.forEach(function(panel) {
      panel.style.display = 'none';
      panel.classList.remove('active');
    });

    // Deactivate all buttons
    var buttons = document.querySelectorAll('.year-tabs button');
    buttons.forEach(function(button) {
      button.classList.remove('active');
    });

    // Show the selected year's panel and activate its button
    document.getElementById('year-' + year).style.display = 'block';
    document.getElementById('year-' + year).classList.add('active');
    
    // Find the button with the matching year and activate it
    for (var i = 0; i < buttons.length; i++) {
        if (buttons[i].textContent === year) {
            buttons[i].classList.add('active');
            break;
        }
    }
  }

  // Automatically show the content for the first (most recent) year when the page loads
  document.addEventListener('DOMContentLoaded', function() {
    var firstButton = document.querySelector('.year-tabs button');
    if (firstButton) {
      showYear(firstButton.textContent);
    }
  });
</script>