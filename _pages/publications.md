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

<script src="/assets/js/custom-scripts.js"></script>