---
layout: single
permalink: /publications/
title: "Publications"
author_profile: true
---

<style>
  .year-tabs button {
    background-color: #f1f1f1; border: none; padding: 10px 15px;
    margin: 0 5px 10px 0; cursor: pointer; border-radius: 4px;
    transition: background-color 0.3s; font-size: 1em;
  }
  .year-tabs button:hover { background-color: #ddd; }
  .year-tabs button.active { background-color: #007bff; color: white; }
  .pub-panel { display: none; }
</style>

{% assign postsByYear = site.publications | group_by_exp:"post", "post.date | date: '%Y'" | reverse %}

<div class="year-tabs">
  {% for year in postsByYear %}
    <button class="year-button" onclick="showYear(this, '{{ year.name }}')">{{ year.name }}</button>
  {% endfor %}
</div>

{% for year in postsByYear %}
  <div id="panel-{{ year.name }}" class="pub-panel">
    {% for post in year.items %}
      <div style="margin-bottom: 2em; border-bottom: 1px solid #e5e5e5; padding-bottom: 1em;">
        {{ post.content }}
      </div>
    {% endfor %}
  </div>
{% endfor %}

<script>
  function showYear(buttonElement, year) {
    // Hide all publication panels
    var allPanels = document.querySelectorAll('.pub-panel');
    allPanels.forEach(function(panel) {
      panel.style.display = 'none';
    });

    // Deactivate all buttons
    var allButtons = document.querySelectorAll('.year-button');
    allButtons.forEach(function(btn) {
      btn.classList.remove('active');
    });

    // Show the target panel and activate the clicked button
    var targetPanel = document.getElementById('panel-' + year);
    if (targetPanel) {
      targetPanel.style.display = 'block';
    }
    buttonElement.classList.add('active');
  }

  // Automatically show the content for the first (most recent) year
  document.addEventListener('DOMContentLoaded', function() {
    var firstButton = document.querySelector('.year-button');
    if (firstButton) {
      firstButton.click();
    }
  });
</script>