from pybtex.database.input import bibtex
from time import strptime
import html
import os
import re

# Simplified configuration to process a single BibTeX file.
publist = {
    "publication": {
        "file": "publications.bib",
        "collection": {"name": "publications",
                       "permalink": "/publication/"}
    }
}

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
}

def html_escape(text):
    return "".join(html_escape_table.get(c, c) for c in text)

# Main processing loop
for pubsource in publist:
    parser = bibtex.Parser()
    bibdata = parser.parse_file(publist[pubsource]["file"])

    for bib_id in bibdata.entries:
        b = bibdata.entries[bib_id].fields
        
        try:
            # --- Basic Data Extraction ---
            pub_year = b.get("year", "1900")
            pub_month = b.get("month", "01")
            pub_day = b.get("day", "01")

            # --- Date Formatting ---
            if len(pub_month) < 3:
                pub_month = "0" + pub_month
                pub_month = pub_month[-2:]
            else:
                try:
                    tmnth = strptime(pub_month[:3], '%b').tm_mon
                    pub_month = f"{tmnth:02d}"
                except ValueError:
                    pub_month = "01" # Default if month name is not recognized

            pub_date = f"{pub_year}-{pub_month}-{pub_day}"

            # --- Filename Generation ---
            clean_title = b.get("title", "").replace("{", "").replace("}", "").replace("\\", "").replace(" ", "-")
            url_slug = re.sub(r'[^a-zA-Z0-9_-]', '', clean_title)
            md_filename = f"{pub_date}-{url_slug[:50]}.md".replace("--", "-")

            # --- Citation Generation ---
            authors = ""
            if "author" in bibdata.entries[bib_id].persons:
                for author in bibdata.entries[bib_id].persons["author"]:
                    authors += f"{author.first_names[0]} {author.last_names[0]}, "
            
            citation = f"{authors.strip(', ')}. \"{html_escape(b.get('title', 'No Title'))}.\""

            # --- Venue Logic (Robust) ---
            venue = ""
            if 'journal' in b:
                venue = b['journal']
            elif 'booktitle' in b:
                venue = f"In {b['booktitle']}"
            elif 'school' in b:
                venue = b['school']

            if venue:
                citation += f" <em>{html_escape(venue)}</em>, {pub_year}."
            else:
                citation += f" {pub_year}."

            # --- Start YAML Front Matter ---
            md = "---\n"
            md += f"title: \"{html_escape(b.get('title', 'No Title'))}\"\n"
            md += f"collection: {publist[pubsource]['collection']['name']}\n"
            md += f"permalink: {publist[pubsource]['collection']['permalink']}{os.path.splitext(md_filename)[0]}\n"
            md += f"date: {pub_date}\n"
            
            if venue:
                md += f"venue: '{html_escape(venue)}'\n"

            if "url" in b:
                md += f"paperurl: '{b['url']}'\n"
            
            md += f"citation: '{html_escape(citation)}'\n"
            md += "---\n"
            
            # --- Main Content ---
            md += f"\n[Download paper here]({b.get('url', '#')}){{:target='_blank'}}\n"
            md += f"\nRecommended citation: {citation}\n"

            # --- Write File ---
            with open(f"../_publications/{md_filename}", 'w', encoding="utf-8") as f:
                f.write(md)
            
            print(f'SUCCESSFULLY PARSED: {b.get("title", "NO TITLE")[:60]}')

        except Exception as e:
            print(f'ERROR processing {bib_id}: {e}')
            continue