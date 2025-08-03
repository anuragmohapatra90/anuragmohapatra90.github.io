import os
import re
import html
from pybtex.database.input import bibtex

# --- Configuration ---
BIB_FILE = "publications.bib"
OUTPUT_DIR = "../_publications/"

# --- LaTeX Character Decoding ---
LATEX_SUBS = {
    r'\\"o': 'ö', r'\\"u': 'ü', r'\\"a': 'ä',
    r'\\"O': 'Ö', r'\\"U': 'Ü', r'\\"A': 'Ä',
    r"\\'e": 'é', r"\\`e": 'è', r'\\ss': 'ß',
    r'{\\"o}': 'ö', r'{\\"u}': 'ü', r'{\\"a}': 'ä',
    r'{\\"O}': 'Ö', r'{\\"U}': 'Ü', r'{\\"A}': 'Ä',
    r"{\\'e}": 'é', r"{\\`e}": 'è', r'{\ss}': 'ß',
    r'{\c{c}}': 'ç', r'{\c{s}}': 'ş',
}

def decode_latex(text):
    """Replaces LaTeX special characters with their unicode equivalent."""
    for latex, unicode in LATEX_SUBS.items():
        text = text.replace(latex, unicode)
    return text.replace("{", "").replace("}", "")

# --- Main Script ---
parser = bibtex.Parser()
bibdata = parser.parse_file(BIB_FILE)

os.makedirs(OUTPUT_DIR, exist_ok=True)

for bib_id in bibdata.entries:
    b = bibdata.entries[bib_id].fields
    p = bibdata.entries[bib_id].persons

    try:
        # --- Data Extraction and Cleaning ---
        title = decode_latex(b.get("title", "No Title"))
        year = b.get("year", "N.A.")
        
        authors = ", ".join([f"{decode_latex(author.first_names[0])}. {decode_latex(author.last_names[0])}" for author in p.get("author", [])])
        
        venue = decode_latex(b.get('booktitle', b.get('journal', '')))
        
        # --- ROBUST URL FINDER ---
        paper_url = b.get('url', "https://doi.org/" + b.get('doi', '') if 'doi' in b else "")

        # --- Generate Filename ---
        safe_title = re.sub(r'[^a-zA-Z0-9_-]', '', title.replace(" ", "-"))[:50]
        md_filename = f"{year}-{safe_title}.md"
        permalink = f"/publication/{os.path.splitext(md_filename)[0]}"

        # --- Logic for Manuscripts vs. Published Papers ---
        is_under_review = "under review" in venue.lower() or "manuscript" in venue.lower()

        # --- Generate Page Content ---
        md_content = f"""---
title: "{html.escape(title)}"
collection: publications
permalink: {permalink}
date: {year}-01-01
---
<p style="font-size: 1.1em; margin-bottom: 0.5em;"><b>{html.escape(title)}</b></p>
"""
        if is_under_review:
            md_content += f'<p style="margin-bottom: 0.5em;"><em>Status: {html.escape(venue)}</em></p>\n'
            citation = f"{authors}. \"{title}\". ({year})."
        else:
            md_content += f'<p style="margin-bottom: 0.5em;">Published in <em>{html.escape(venue)}</em>, {year}</p>\n'
            # THIS IS THE CORRECTED LINE: The f-string is now properly terminated.
            citation = f"{authors}. \"{title}\". <em>{html.escape(venue)}</em>, {year}."

        # --- Link Logic ---
        if paper_url:
            md_content += f'<p style="margin-bottom: 0.5em;"><a href="{paper_url}" target="_blank">Access paper here</a></p>\n'
        else:
            google_scholar_query = html.escape(title.replace(" ", "+"))
            md_content += f'<p style="margin-bottom: 0.5em;"><a href="https://scholar.google.com/scholar?q={google_scholar_query}" target="_blank">Search on Google Scholar</a></p>\n'
        
        md_content += f'<p>Recommended citation: {citation}</p>'

        # --- Write the File ---
        with open(os.path.join(OUTPUT_DIR, md_filename), 'w', encoding='utf-8') as f:
            f.write(md_content)

        print(f"SUCCESS: Processed '{title[:50]}...'")

    except Exception as e:
        print(f"ERROR: Failed to process entry {bib_id}. Reason: {e}")