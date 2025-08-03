---
layout: archive
permalink: /cv/
title: "Curriculum Vitae"
author_profile: true
---

<div class="grid__wrapper">
  {% for section in site.data.cv %}
    {% assign section_name = section[0] %}
    {% assign section_items = section[1] %}
    <div class="grid__item" style="width: 100%;">
      <h2 class="archive__item-title">{{ section_name | capitalize }}</h2>
      <hr>
      {% for item in section_items %}
        <div class="archive__item-teaser" style="margin-bottom: 1.5em;">
          {% if item.position %}
            <h3 class="archive__item-title" itemprop="headline" style="margin-bottom: 0.2em;">{{ item.position }}</h3>
            <p class="page__meta" style="margin: 0;">{{ item.company }} | {{ item.year }}</p>
          {% elsif item.degree %}
            <h3 class="archive__item-title" itemprop="headline" style="margin-bottom: 0.2em;">{{ item.degree }}</h3>
            <p class="page__meta" style="margin: 0;">{{ item.uni }} | {{ item.year }}</p>
          {% else %}
             <h3 class="archive__item-title" itemprop="headline" style="margin-bottom: 0.2em;">{{ item.title }}</h3>
          {% endif %}
          
          {% if item.summary %}
            <p class="archive__item-excerpt" style="margin-top: 0.5em;">{{ item.summary }}</p>
          {% elsif item.details %}
            <p class="archive__item-excerpt" style="margin-top: 0.5em;">{{ item.details }}</p>
          {% endif %}
        </div>
      {% endfor %}
    </div>
  {% endfor %}
</div>