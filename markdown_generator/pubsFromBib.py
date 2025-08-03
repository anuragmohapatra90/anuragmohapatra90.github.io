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
    r"\\'e": 'é', r"\\`e": 'è', r"\\'c": 'ć',
    r'{\\"o}': 'ö', r'{\\"u}': 'ü', r'{\\"a}': 'ä',
    r'{\\"O}': 'Ö', r'{\\"U}': 'Ü', r'{\\"A}': 'Ä',
    r"{\\'e}": 'é', r"{\\`e}": 'è', r"{\\'c}": 'ć',
    r'\ss': 'ß', r'{\ss}': 'ß',
    r'{\c{c}}': 'ç', r'{\c{s}}': 'ş',
    r'&': '&amp;',
}

def decode_latex(text):
    """Replaces LaTeX special characters with their unicode equivalent."""
    for latex, unicode in LATEX_SUBS.items():
        text = text.replace(latex, unicode)
    # Remove any remaining curly braces that are not part of a command
    text = text.replace("{", "").replace("}", "")
    return text

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
        
        # --- Author Formatting: "S. Eichhorn, A. Mohapatra, C. Goebel" ---
        authors = []
        if "author" in p:
            for author in p["author"]:
                first_name_parts = [decode_latex(part) for part in author.first_names]
                last_name_parts = [decode_latex(part) for part in author.last_names]
                full_first_name = " ".join(first_name_parts)
                full_last_name = " ".join(last_name_parts)
                initial = f"{full_first_name[0]}." if full_first_name else ""
                authors.append(f"{initial} {full_last_name}")
        authors_str = ", ".join(authors)

        # --- Venue Formatting ---
        venue = decode_latex(b.get('booktitle', b.get('journal', '')))
        
        # --- ROBUST URL FINDER ---
        paper_url = ""
        if 'url' in b and b['url']:
            paper_url = b['url']
        elif 'doi' in b and b['doi']:
            paper_url = "https://doi.org/" + b['doi']

        # --- Build Recommended Citation ---
        citation = f"{authors_str}. \"{title}\". <em>{venue}</em>, {year}."

        # --- Generate Filename ---
        safe_title = re.sub(r'[^a-zA-Z0-9_-]', '', title.replace(" ", "-"))[:50]
        md_filename = f"{year}-{safe_title}.md"
        permalink = f"/publication/{os.path.splitext(md_filename)[0]}"

        # --- Generate Page Content ---
        md_content = f"""---
title: "{html.escape(title)}"
collection: publications
permalink: {permalink}
date: {year}-01-01
---
<p style="font-size: 1.1em; margin-bottom: 0.5em;"><b>{html.escape(title)}</b></p>
<p style="margin-bottom: 0.5em;"><em>{html.escape(venue)}</em>, {year}</p>
"""
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