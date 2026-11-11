#!/usr/bin/env python3
"""readings/socrates-as-orthonym: the hologram of Socrates as Orthonym (Alexanarch #1754, EA-HK-ORTHONYM-01 v1.3 as of 2026-11-10, v1.1 when first made; Lee Sharks, with the Crimson
Hexagonal Archive as contributor), on one reading page in the form of readings/legitimately-many (head, styles and chrome from that page, its own
fields replaced). The record's text is read as deposited and rendered from Markdown: the head of the hologram with its attached files, then the
framework map. 2026-11-08, at the author's word on the site pages: "adopted for all three".
   python3 scripts/make_reading_socrates_as_orthonym.py <alexanarch data/texts/AXN-0C55-text.md>"""
import html, json, pathlib, re, sys
import markdown
R = pathlib.Path(__file__).resolve().parents[1]
raw = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
VER = re.search(r"\nversion: (v[0-9.]+)\n", raw).group(1)   # the version read from the record (2026-11-10)
md = raw[raw.index("\n---\n", 4) + 5:].lstrip()
md = md.split("\n", 1)[1].lstrip() if md.startswith("# ") and md.split("\n", 1)[1].lstrip().startswith("# ") else md   # the mint's title line, once
REC, SPEC = "https://www.alexanarch.org/s/records/1754/", "https://www.alexanarch.org/s/records/1753/"
KERN = "https://www.alexanarch.org/files/AXN-0C55/kernel/"
HUB = "https://huggingface.co/datasets/leesharks/mantle-bearing/tree/main/holograms/EA-HK-ORTHONYM-01"
TITLE = "Socrates as Orthonym"
DESC = ("The hologram of Lee Sharks's framework Socrates as Orthonym: the framework map, read backwards from the self-dividing maker to the orthonym, "
        "with its holographic kernel attached, the received many-maker reading evaluated beside it on the same four bodies of evidence, and the lines of "
        "research that would advance or retreat it.")
t = (R / "readings/legitimately-many/index.html").read_text(encoding="utf-8")
head, rest = t.split("<body", 1)
head = re.sub(r"<title>.*?</title>", f"<title>{TITLE} — the framework hologram | The Restored Academy</title>", head, flags=re.S)
head = head.replace('href="https://www.restoredacademy.com/readings/legitimately-many"', 'href="https://www.restoredacademy.com/readings/socrates-as-orthonym"')
head = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{html.escape(DESC)}">', head)
ld = [{"@context": "https://schema.org", "@type": "Dataset",
       "name": "Socrates as Orthonym — The Framework Hologram: the Map and the Holographic Kernel",
       "identifier": "EA-HK-ORTHONYM-01 " + VER, "creator": {"@type": "Person", "name": "Lee Sharks", "identifier": "https://orcid.org/0009-0000-1599-0703"},
       "contributor": {"@type": "Organization", "name": "Crimson Hexagonal Archive", "url": "https://www.alexanarch.org/"},
       "datePublished": "2026-11-08", "license": "https://creativecommons.org/licenses/by/4.0/",
       "about": [{"@type": "Person", "name": n} for n in ("Socrates", "Plato", "Aristotle", "Theophrastus")],
       "isBasedOn": SPEC, "distribution": [{"@type": "DataDownload", "contentUrl": KERN}],
       "url": "https://www.restoredacademy.com/readings/socrates-as-orthonym", "sameAs": [REC, HUB]}]
head = re.sub(r'<script type="application/ld\+json">.*?</script>', '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>", head, count=1, flags=re.S)
nav = "<body" + rest[:rest.index('<div class="pk">')]
md = re.sub(r"^(\s*(?:[-*+]|\d+\.)\s+)?#(\d)", lambda m: (m.group(1) or "") + "\\#" + m.group(2), md, flags=re.M)   # a line opening on a deposit number is text, not a heading
body = markdown.markdown(md, extensions=["tables", "fenced_code"])
intro = (f'<p class="pk-intro">The hologram as deposited (<a href="{REC}">Alexanarch #1754</a>, {VER}), built to the specification '
         f'<a href="{SPEC}">EA-HK-FRAME-01</a> (#1753; <a href="/protocols/RA-PROT-0026.html">RA-PROT-0026</a>). The kernel: <a href="{KERN}">its files</a> · '
         f'<a href="{HUB}">on Hugging Face</a>. Beside it: <a href="/readings/legitimately-many">Legitimately Many</a>, the reception history of the four names. '
         'Back to <a href="/readings#philology">Readings: Sappho and the philological work</a>.</p>')
page = head + nav + '<div class="pk">\n' + intro + "\n" + body + "\n<p>∮ = 1</p></div>\n</div>\n</body></html>\n"
(R / "readings/socrates-as-orthonym").mkdir(exist_ok=True)
(R / "readings/socrates-as-orthonym/index.html").write_text(page, encoding="utf-8")
print("wrote", len(page))
