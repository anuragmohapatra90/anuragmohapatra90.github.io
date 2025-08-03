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
</style>

{% assign pubs_sorted = site.publications | sort: 'date' | reverse %}
{% assign postsByYear = pubs_sorted | group_by_exp:"post", "post.date | date: '%Y'" %}

<div id="year-tabs" class="year-tabs">
  {% for year in postsByYear %}
    <button class="year-button" data-year="{{ year.name }}">{{ year.name }}</button>
  {% endfor %}
</div>

<div id="pub-content">
  {% for year in postsByYear %}
    <div id="panel-{{ year.name }}" class="pub-panel">
      {% for post in year.items %}
        <div style="margin-bottom: 2em; border-bottom: 1px solid #e5e5e5; padding-bottom: 1em;">
          {{ post.content }}
        </div>
      {% endfor %}
    </div>
  {% endfor %}
</div>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    const yearButtons = document.querySelectorAll('.year-button');
    const pubPanels = document.querySelectorAll('.pub-panel');

    function showYear(year) {
      // Hide all panels
      pubPanels.forEach(panel => {
        panel.style.display = 'none';
      });

      // Deactivate all buttons
      yearButtons.forEach(button => {
        button.classList.remove('active');
      });

      // Find and show the target panel and activate the target button
      const targetPanel = document.getElementById('panel-' + year);
      const targetButton = document.querySelector(`.year-button[data-year="${year}"]`);

      if (targetPanel) {
        targetPanel.style.display = 'block';
      }
      if (targetButton) {
        targetButton.classList.add('active');
      }
    }

    // Add click event listeners to all buttons
    yearButtons.forEach(button => {
      button.addEventListener('click', function() {
        showYear(this.dataset.year);
      });
    });

    // Show the first year by default, if any buttons exist
    if (yearButtons.length > 0) {
      const firstYear = yearButtons[0].dataset.year;
      showYear(firstYear);
    }
  });
</script>