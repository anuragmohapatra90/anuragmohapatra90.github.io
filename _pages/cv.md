---
layout: archive
permalink: /cv/
title: "Curriculum Vitae"
author_profile: true
---

{% for section in site.data.cv %}
  {% assign section_name = section[0] %}
  {% assign section_items = section[1] %}
  
  <h2 style="border-bottom: 1px solid #e5e5e5; padding-bottom: 0.5em;">{{ section_name | capitalize }}</h2>
  
  {% for item in section_items %}
    <div style="margin-bottom: 1.5em;">
      {% if item.position %}
        <h3 style="margin-bottom: 0.2em;">{{ item.position }}</h3>
        <p class="page__meta" style="margin: 0;">{{ item.company }} | {{ item.year }}</p>
      {% elsif item.degree %}
        <h3 style="margin-bottom: 0.2em;">{{ item.degree }}</h3>
        <p class="page__meta" style="margin: 0;">{{ item.uni }} | {{ item.year }}</p>
      {% else %}
         <h3 style="margin-bottom: 0.2em;">{{ item.title }}</h3>
      {% endif %}
      
      {% if item.summary %}
        <p style="margin-top: 0.5em;">{{ item.summary | markdownify }}</p>
      {% elsif item.details %}
        <p style="margin-top: 0.5em;">{{ item.details | markdownify }}</p>
      {% endif %}
    </div>
  {% endfor %}
  
{% endfor %}