---
layout: single
permalink: /publications/
title: "Publications"
author_profile: true
---

{% for post in site.publications reversed %}
<div style="margin-bottom: 2em; border-bottom: 1px solid #e5e5e5; padding-bottom: 1em;">
{{ post.content }}
</div>
{% endfor %}