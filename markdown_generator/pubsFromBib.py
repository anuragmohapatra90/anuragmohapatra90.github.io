from pybtex.database.input import bibtex
import pybtex.database.input.bibtex
from time import strptime
import string
import html
import os
import re

# This dictionary is now simplified. We will process one file
# and the script will determine the type of publication on its own.
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
    """Produce entities within text."""
    return "".join(html_escape_table.get(c, c) for c in text)

for pubsource in publist:
    parser = bibtex.Parser()
    bibdata = parser.parse_file(publist[pubsource]["file"])

    for bib_id in bibdata.entries:
        b = bibdata.entries[bib_id].fields
        
        try:
            # General data cleanup
            pub_year = f'{b["year"]}'
            pub_month = "01"
            pub_day = "01"

            if "month" in b.keys():
                if len(b["month"]) < 3:
                    pub_month = "0" + b["month"]
                    pub_month = pub_month[-2:]
                elif b["month"] not in range(12):
                    tmnth = strptime(b["month"][:3], '%b').tm_mon
                    pub_month = "{:02d}".format(tmnth)
                else:
                    pub_month = str(b["month"])
            
            if "day" in b.keys():
                pub_day = str(b["day"])

            pub_date = f"{pub_year}-{pub_month}-{pub_day}"
            clean_title = b["title"].replace("{", "").replace("}", "").replace("\\", "").replace(" ", "-")
            url_slug = re.sub("\\[.*\\]|[^a-zA-Z0-9_-]", "", clean_title)
            url_slug = url_slug.replace("--", "-")
            md_filename = (f"{pub_date}-{url_slug}.md").replace("--", "-")
            html_filename = (f"{pub_date}-{url_slug}").replace("--", "-")

            # Start building the citation string
            citation = ""
            for author in bibdata.entries[bib_id].persons["author"]:
                citation += f" {author.first_names[0]} {author.last_names[0]},"
            
            citation = citation.strip(',') # remove last comma
            citation += f" \"{html_escape(b['title'])}\"."

            # Venue Logic: Check for 'journal' or 'booktitle'
            venue = ""
            if 'journal' in b:
                venue = b['journal']
            elif 'booktitle' in b:
                venue = f"In the proceedings of {b['booktitle']}"
            
            if venue:
                 citation += f" *{html_escape(venue)}*, {pub_year}."

            # YAML header
            md = f"---\ntitle: \"{html_escape(b['title'])}\"\n"
            md += f"collection: {publist[pubsource]['collection']['name']}\n"
            md += f"permalink: {publist[pubsource]['collection']['permalink']}{html_filename}\n"
            md += f"date: {pub_date}\n"
            
            if venue:
                md += f"venue: '{html_escape(venue)}'\n"

            if "url" in b:
                md += f"paperurl: '{b['url']}'\n"
            
            md += f"citation: '{html_escape(citation)}'\n"
            md += "---\n"

            # Markdown Content
            if "url" in b:
                md += f"\n[Access paper here]({b['url']}){{:target='_blank'}}\n"
            else:
                md += f"\nUse [Google Scholar](https://scholar.google.com/scholar?q={html.escape(clean_title.replace('-', '+'))}){{:target='_blank'}} for full citation.\n"

            md_filename = os.path.basename(md_filename)

            with open(f"../_publications/{md_filename}", 'w', encoding="utf-8") as f:
                f.write(md)
            
            print(f'SUCCESSFULLY PARSED {bib_id}: "{b["title"][:60]}"')

        except KeyError as e:
            print(f'WARNING: Missing Expected Field {e} from entry {bib_id}: "{b["title"][:30]}"')
            continue