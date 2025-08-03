import os
import re
import html
from time import strptime
from pybtex.database.input import bibtex

# --- Configuration ---
BIB_FILE = "publications.bib"
OUTPUT_DIR = "../_publications/"

# --- Main Script ---
parser = bibtex.Parser()
bibdata = parser.parse_file(BIB_FILE)

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

for bib_id in bibdata.entries:
    b = bibdata.entries[bib_id].fields
    p = bibdata.entries[bib_id].persons

    try:
        # --- Basic Info ---
        title = b.get("title", "No Title").replace("{", "").replace("}", "")
        year = b.get("year", "N.A.")

        # --- Author Formatting: "S. Eichhorn, A. Mohapatra, C. Goebel" ---
        authors = []
        if "author" in p:
            for author in p["author"]:
                first_name = " ".join(author.first_names)
                last_name = " ".join(author.last_names)
                # Create initial like "S."
                initial = f"{first_name[0]}."
                authors.append(f"{initial} {last_name}")
        authors_str = ", ".join(authors)

        # --- Venue Formatting ---
        venue = ""
        if 'booktitle' in b:
            venue = b['booktitle']
        elif 'journal' in b:
            venue = b['journal']
        
        # --- URL / DOI ---
        paper_url = b.get("url", b.get("doi", ""))
        if paper_url and "doi.org" not in paper_url:
             if "doi" in paper_url:
                paper_url = "https://doi.org/" + paper_url.split("doi.org/")[-1]


        # --- Build Recommended Citation String ---
        citation = f"{authors_str}. \"{title}\". <em>{venue}</em>, {year}."

        # --- Generate Filename ---
        safe_title = re.sub(r'[^a-zA-Z0-9_-]', '', title.replace(" ", "-"))[:50]
        md_filename = f"{year}-{safe_title}.md"

        # --- Generate the ENTIRE HTML content for the page ---
        html_content = f"""---
title: "{html.escape(title)}"
collection: publications
permalink: /publication/{os.path.splitext(md_filename)[0]}
date: {year}-01-01
---

<p style="font-size: 1.1em; margin-bottom: 0.5em;"><b>{html.escape(title)}</b></p>
<p style="margin-bottom: 0.5em;">Published in <em>{html.escape(venue)}</em>, {year}</p>
"""
        if paper_url:
            html_content += f'<p style="margin-bottom: 0.5em;"><a href="{paper_url}" target="_blank">Access paper here</a></p>\n'
        
        html_content += f'<p>Recommended citation: {citation}</p>'


        # --- Write the Markdown File ---
        with open(os.path.join(OUTPUT_DIR, md_filename), 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"SUCCESS: Processed '{title[:50]}...'")

    except Exception as e:
        print(f"ERROR: Failed to process entry {bib_id}. Reason: {e}")