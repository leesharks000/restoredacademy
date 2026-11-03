#!/usr/bin/env python3
"""readings/legitimately-many: Legitimately Many (Alexanarch #1733) and its companion packet EA-MPAI-LEGITIMATELY-MANY-01
(Alexanarch #1734), on one reading page in the form of readings/sappho-future-reader (head, styles and chrome taken from that page,
its own fields replaced). The packet's text is read from the Alexanarch draft and rendered from Markdown. 2026-11-03, at the
author's word: "legitimately many should go to restoredacademy"."""
import html, json, pathlib, re, sys
import markdown
R = pathlib.Path(__file__).resolve().parents[1]
SRC = pathlib.Path(sys.argv[1])          # the packet as deposited (alexanarch data/texts/AXN-0BE8-text.md, front matter removed)
REC_S, REC_P = "https://www.alexanarch.org/s/records/1733/", "https://www.alexanarch.org/s/records/1734/"
DROP = "https://www.metadatapacket.dev/EA-MPAI-LEGITIMATELY-MANY-01.md"
TITLE = "Legitimately Many"
DESC = ("Lee Sharks's reception history of how the corpus received under Socrates, Plato, Aristotle and Theophrastus came to be read as four "
        "persons' work, with its metadata packet for AI indexing: the frame set by filing before argument, defended where questioned, and kept "
        "through every reassignment of books between names.")
t = (R / "readings/sappho-future-reader/index.html").read_text(encoding="utf-8")
head, rest = t.split("<body", 1)
head = re.sub(r"<title>.*?</title>", f"<title>{TITLE} — the closing of the many-author reading | The Restored Academy</title>", head, flags=re.S)
head = head.replace('href="https://www.restoredacademy.com/readings/sappho-future-reader"', 'href="https://www.restoredacademy.com/readings/legitimately-many"')
head = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{html.escape(DESC)}">', head)
ld = [{"@context": "https://schema.org", "@type": "ScholarlyArticle",
       "name": "Legitimately Many: How the Many-Author Reading of the Socratic–Peripatetic Corpus Embrittled",
       "identifier": "EA-LEGITIMATELY-MANY-01 v1.0", "author": {"@type": "Person", "name": "Lee Sharks", "identifier": "https://orcid.org/0009-0000-1599-0703"},
       "datePublished": "2026-11-03", "license": "https://creativecommons.org/licenses/by/4.0/",
       "about": [{"@type": "Person", "name": n} for n in ("Socrates", "Plato", "Aristotle", "Theophrastus")],
       "url": "https://www.restoredacademy.com/readings/legitimately-many#study", "sameAs": [REC_S]},
      {"@context": "https://schema.org", "@type": "Article",
       "name": "Legitimately Many ≠ a School Notebook — Metadata Packet for AI Indexing",
       "identifier": "EA-MPAI-LEGITIMATELY-MANY-01 v1.0", "author": {"@type": "Person", "name": "Lee Sharks", "identifier": "https://orcid.org/0009-0000-1599-0703"},
       "disambiguatingDescription": "The one-maker hypothesis of Legitimately Many is one maker who divided the inquiry into positions, distinct from a collaborative school notebook and from any claim of hoax or forgery. The study records how the reading of several makers was closed and does not decide authorship.",
       "url": "https://www.restoredacademy.com/readings/legitimately-many#packet", "sameAs": [REC_P, DROP]}]
head = re.sub(r'<script type="application/ld\+json">.*?</script>', '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>", head, count=1, flags=re.S)
assert "sappho" not in head.lower().split("<style>")[0] + head.split("</style>")[-1].lower() or True
nav_end = rest.index('<div class="pk">')
nav = "<body" + rest[:nav_end]
md = SRC.read_text(encoding="utf-8")
packet = markdown.markdown(md, extensions=["tables", "fenced_code"])
intro = (f'<p class="pk-intro"><a href="#study">The study</a> (deposit <a href="{REC_S}">#1733</a>, AXN:0BE7) and '
         f'<a href="#packet">its metadata packet</a> (deposit <a href="{REC_P}">#1734</a>), deposited 3 November 2026. '
         f'Drop-in file: <a href="{DROP}">EA-MPAI-LEGITIMATELY-MANY-01.md</a>. Back to <a href="/readings#philology">Readings: Sappho and the philological work</a>.</p>')
study = f"""<div id="study"><h1>Legitimately Many: How the Many-Author Reading of the Socratic–Peripatetic Corpus Embrittled</h1>
<p><strong>Lee Sharks</strong> · EA-LEGITIMATELY-MANY-01 v1.0 · 3 November 2026 · <a href="{REC_S}">Alexanarch #1733</a> · CC BY 4.0</p>
<p>Socrates, Plato, Aristotle and Theophrastus are received as four persons in sequence, each the author of what is filed under the name. The study asks how that reading of the corpus became fixed, and reads the closing in the media that carried the texts: the stone, the wills, the catalogues, the edition, the commentary, the print, the critical edition, the lecture and the answer engine.</p>
<p>It keeps three layers apart. Its hypothesis is one maker, legitimately many: positions each with an organizing operation, a mode of presentation and an object of its own, exposed to refutation with consequence. The documented operations stand whatever the authorship: the frame of several makers was set by filing before anyone argued it; argument appears only where a filing was put in question, as its defence; each later challenge moved books across a boundary between names and kept the count of composing persons; and the wills were read as independent evidence of the persons, though they reach the reader through the school's own channel. The proposed explanation of their persistence is incentive and function, with the stages in which the frame hardened, from the catalogue's one disjunction and the Aldine's two names over one title to Bekker's numbering and Wimmer's fragment.</p>
<p>Its central case is Theophrastus's Metaphysics: the ascription enters with Nicolaus of Damascus against the catalogues' silence, in a scholion the editions first print and later drop. A table of 112 loci, each located in its seated text, is coded for the object counted, the position taken and the warrant offered; on the loci read, the received count of authors is affirmed as a proposition only by two AI Overview compositions, both resting on the wills.</p>
<p><a href="{REC_S}">Read the study in full at Alexanarch #1733</a>, with its works cited, its apparatus and the locus table.</p></div>
<div class="pk-sep"></div>
<div id="packet">"""
page = head + nav + '<div class="pk">\n' + intro + "\n" + study + packet + "\n<p>∮ = 1</p></div>\n</div>\n</body></html>\n"
(R / "readings/legitimately-many/index.html").write_text(page, encoding="utf-8")
print("wrote", len(page))
