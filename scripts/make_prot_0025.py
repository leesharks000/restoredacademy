#!/usr/bin/env python3
"""RA-PROT-0025, the Sophistry Measure (Alexanarch #1727): writes the 11-section card (protocols/RA-PROT-0025-Sophistry-Measure.md)
and its page (protocols/RA-PROT-0025.html) from one content table, the page taking RA-PROT-0024.html's head, styles, chrome and
apparatus verbatim with only the card's own fields replaced. 2026-11-02, at the operator's word: "the sr measure paper should go to
per and restoredacademy". The page's render_sha256 is computed with its own value nulled, as the colophon states."""
import hashlib, html, pathlib, re
R = pathlib.Path(__file__).resolve().parents[1]
P = R / "protocols"
ID, SHORT, VER = "RA-PROT-0025", "The Sophistry Measure", "v1.0"
AUTHOR = "Lee Sharks"
REC, AXN, AXN_GLYPH = "https://www.alexanarch.org/s/records/1727/", "AXN:0BDC.OPERATIVE", "💛🗿🛡️🔖🧬🛸"
LEDE = ("An instrument for machine-composed knowledge read from Aristotle's Sophistical Refutations: it records, at an address, the gap between what "
        "a composition presents itself as carrying and what it carries, as typed transformations, each with its witness, its strongest alternative "
        "reading, a countertest and the smallest repair.")
GREEK = "ἔστι γὰρ ἡ σοφιστικὴ φαινομένη σοφία οὖσα δ᾿ οὔ, καὶ ὁ σοφιστὴς χρηματιστὴς ἀπὸ φαινομένης σοφίας ἀλλ᾿ οὐκ οὔσης"

S = [
 ("What it does", [
   ("p", f"Aristotle defines the art in one clause: *{GREEK}* (SE 1). Sophistry is wisdom that appears and is not, and the sophist makes money from the appearance."),
   ("p", "The Sophistry Measure records, at an address, the gap between what a composition presents itself as carrying and what it carries. Each finding is one transformation, reconstructed from the texts, with its witness, a type keyed to the book's chapters and Greek loci, the strongest alternative reading, a countertest and the smallest repair. It has no scalar: \"measure\" here names a structured qualitative result."),
   ("p", "It stands beside PER (RA-PROT-0009). PER measures declared losses against a versioned target. A composition can keep every token PER counts and still change the authority, scope or relation under which it presents them; the Sophistry Measure types that transformation, and examines the warrant of the measurement target itself."),
 ]),
 ("When to use it", [
   ("p", "Deploy the Sophistry Measure when:"),
   ("ul", ["A composition keeps authentic language while it changes the authority, scope or relation under which that language is presented",
           "PER reads low while the representation is wrong: every atom present, every quotation genuine, the entity misrepresented",
           "A composition presents one locus of an entity developed across several sources as the developed entity (X24, locus substituted for entity)",
           "A measurement target, a repair or a service of the archive's own is to be held to the same tests"]),
 ]),
 ("Inputs", [
   ("p", "The address and its transcript, as the Capture Registry seats them (query, surface, sign-in state, date, the composition verbatim with its cards); the entity's developmental dossier (its dated source locations, what each adds, applies, revises or leaves open, and the voice and endorsement of each proposition); the seated source texts; the PER target, where one exists."),
 ]),
 ("Procedure", [
   ("ol", ["Record the adequacy condition before any operation is typed: what was asked, what scope the answer announces, and which omitted relation materially changes the answer at that scope. A short answer drawn from one source is ordinary selection; it becomes a finding only where the composition claims to stand for more than its selection warrants.",
           "State the innocent reading first, in full.",
           "Locate the witness: the exact words of the composition, quoted from the transcript.",
           "Reconstruct the transformation from the texts, the composition beside its sources and the dossier.",
           "Type it, under the book's own names and chapters, each extension marked as a direct instance, a structural extension or an interpretive connection.",
           "Give the strongest alternative reading, and a countertest that would tell the two apart.",
           "Give the smallest repair: the least change to the composition that would carry what it claims to carry.",
           "Record the finding with the capture, with its countertest open."]),
 ]),
 ("Outputs", [
   ("p", "A list of typed findings for the address, each with witness, reconstruction, type, alternative reading, countertest and repair; corrections to the entity's developmental dossier; and, where the measurement target itself is found to have transformed its object, a finding against the target."),
 ]),
 ("Pasteable LLM block", [
   ("pre", "Under the Sophistry Measure (EA-SOPHISTRY-01, Alexanarch #1727), the reader of a composition first records what was asked, what scope the answer announces, and which omitted relation would change the answer at that scope. The reader then states the innocent reading, quotes the exact words at issue, reconstructs from the sources how the composition changed its object while keeping the appearance of carrying it, types the change under the Sophistical Refutations' own names, gives the strongest alternative reading and a countertest, and gives the smallest repair. The reader gives no score. Accurate quotation does not discharge a finding: the question is the standing the composition grants what it quotes."),
 ]),
 ("Human operator notes", [
   ("ul", ["The measure reads texts. The process that generated an answer is a further object, reached only by further evidence, and a model's own account of that process is one more text under the same tests.",
           "The measure applies to the archive's own targets, repairs and services as to anything else; its case is a seated observation whose PER target had itself promoted a received plate to the archive's definition.",
           "Its first worked finding outside the archive is the Overview's composition of Avi Loeb on 3I/ATLAS (Capture Registry, avi-loeb-3i-atlas-aio-20261102): one interview concession given the standing of the developed position, scalar PER zero, the loss in the commitments."]),
 ]),
 ("Failure modes", [
   ("ul", ["Typing ordinary selection as a finding, where the composition makes no claim to adequacy beyond its selection → the measure becomes a complaint about brevity",
           "Reducing the findings to a score → the transformation disappears into the number it was built to see past",
           "Taking verified quotation for representational adequacy → the locus is accepted as the entity",
           "Skipping the innocent reading or the countertest → the finding cannot be told from the reader's preference"]),
 ]),
 ("Related protocols", [
   ("ul", ["RA-PROT-0009 (PER) — the declared-loss measure the Sophistry Measure stands beside",
           "RA-PROT-0011 (Drowning Test) — resolution of the entity, where PER scores attribution",
           "RA-PROT-0012 (Reception Apparatus) — the reception record the findings are kept with"]),
 ]),
 ("Source DOI", [
   ("p", f"No DOI. [Alexanarch deposit #1727]({REC}) — {AXN}.{AXN_GLYPH} — The Sophistry Measure: the Sophistical Refutations Read as an Instrument for Machine-Composed Knowledge (EA-SOPHISTRY-01 v1.0) (Sharks, 2026-11-01). Also at [provenanceerasure.org/sophistry-measure](https://www.provenanceerasure.org/sophistry-measure)."),
 ]),
 ("License", [
   ("p", "CC BY 4.0. Commercial licensing through The Restored Academy for organizational audits of machine-composed knowledge."),
 ]),
]

# ---- the markdown card
md = [f"# {SHORT}", "", f"**{ID}** · {VER} · Category I (Semantic Integrity & Provenance), Category III (Diagnostic & Measurement) · Tier 1", "", LEDE, "", "---", ""]
for n, (h, blocks) in enumerate(S, 1):
    md += [f"## {n}. {h}", ""]
    for kind, v in blocks:
        if kind == "p":
            md += [v, ""]
        elif kind == "ul":
            md += [f"- {x}" for x in v] + [""]
        elif kind == "ol":
            md += [f"{i}. {x}" for i, x in enumerate(v, 1)] + [""]
        elif kind == "pre":
            md += ["```", v, "```", ""]
md += ["---", "", f"**Authoring heteronym:** {AUTHOR} · **Status:** Active · **Added:** 2026-11-02", ""]
(P / f"{ID}-Sophistry-Measure.md").write_text("\n".join(md), encoding="utf-8")


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"\*([^*\n]+)\*", r"<em>\1</em>", t)
    return t


body = []
for n, (h, blocks) in enumerate(S, 1):
    body.append(f'<h2 data-num="{n}" id="s{n}">{h}</h2>')
    for kind, v in blocks:
        if kind == "p":
            body.append(f"<p>{inline(v)}</p>")
        elif kind in ("ul", "ol"):
            body.append(f"<{kind}>" + "".join(f"<li>{inline(x)}</li>" for x in v) + f"</{kind}>")
        elif kind == "pre":
            body.append(f"<pre><code>{html.escape(v, quote=False)}</code></pre>")

t = (P / "RA-PROT-0024.html").read_text(encoding="utf-8")
head_end = t.index("</head>")
head = t[:head_end]
desc = f"{ID} — {SHORT}. {LEDE}"
head = re.sub(r"RA-PROT-0024", ID, head)
head = head.replace("β-Runtime Specification", SHORT)
head = re.sub(r'<meta content="RA-PROT-0025 — [^"]*" name="description"/>', f'<meta content="{html.escape(desc)}" name="description"/>', head)
head = head.replace('<meta content="Talos Morrow" name="spxi:authoringHeteronym"/>', f'<meta content="{AUTHOR}" name="spxi:authoringHeteronym"/>')
head = head.replace('<meta content="10.5281/zenodo.18357600" name="spxi:depositAnchor"/>', f'<meta content="{REC}" name="spxi:depositAnchor"/>')
head = head.replace('"author": { "@type": "Person", "name": "Talos Morrow" }', f'"author": {{ "@type": "Person", "name": "{AUTHOR}" }}')
head = head.replace('"sameAs": "https://alexanarch.org/s/records/377/"', f'"sameAs": "{REC}"')
assert "Talos" not in head and "zenodo.18357600" not in head and "/records/377/" not in head

b0 = t.index("<body>")
pre_article = t[head_end:t.index('<header class="prot-head">')]
pre_article = pre_article.replace('<span class="axn">💛♻️✖️❤️🌕⚓ AXN:029D.GOVERNANCE</span>', f'<span class="axn">{AXN_GLYPH} {AXN}</span>')
pre_article = pre_article.replace("RA-PROT-0024 β-Runtime Specification", f"{ID} {SHORT}").replace("restoredacademy.com/protocols/RA-PROT-0024.html", f"restoredacademy.com/protocols/{ID}.html")
pre_article = pre_article.replace('href="https://www.alexanarch.org/s/records/116/">deposit #116</a>', f'href="{REC}">deposit #1727</a>')
assert "RA-PROT-0024" not in pre_article and "029D" not in pre_article

hdr = (f'<header class="prot-head">\n<div class="breadcrumb"><a href="/">Restored Academy</a> · <a href="/#tier-1">Tier 1 Registry</a> · {ID}</div>\n'
       f'<div class="prot-id">{ID} · {VER}</div>\n<h1 class="prot-title">{SHORT}</h1>\n<div class="meta-row">\n<span><strong>Author:</strong> {AUTHOR}</span>\n'
       '<span class="badge badge-tier">Tier 1</span>\n<span class="badge">Cat I</span>\n<span class="badge">Cat III</span>\n<span><strong>Status:</strong> Active</span>\n</div>\n</header>\n')
foot_nav = '<nav class="footer-nav">\n<a class="prev" href="RA-PROT-0024.html">RA-PROT-0024 β-Runtime Specification</a>\n<span></span>\n</nav>\n</article>\n</div>\n'
tail = t[t.index("<!-- MSP-APPARATUS-START -->"):]
tail = re.sub(r'<div class="mspcolophon">.*?</div>',
              (f'<div class="mspcolophon">colophon · surface_id: restoredacademy.com/protocols/{ID}.html · canonical_url: https://restoredacademy.com/protocols/{ID}.html · '
               f'object_state: canonical · surface_observed_at: 2026-11-02T00:00:00Z · source_object_ids: deposit #1727 · source_hashes: see the seat · '
               f'generator_version: scripts/make_prot_0025.py · repository_commit: see correction_log_url · model_or_agent: drafted with Claude (TACHYON), MANUS-directed · '
               f'operator_sequence: n/a · human_approver: Lee Sharks (MANUS) · approval_timestamp: 2026-11-02 · render_sha256 (of this file with this field’s value set to null): RENDERSHA · '
               f'correction_log_url: https://github.com/leesharks000/restoredacademy/commits/main/protocols/{ID}.html — EA-APPARATUS-01 v0.3, AXN:0446.OPERATIVE.🏛️🛡️🌅🎆📏🔎</div>'),
              tail, count=1, flags=re.S)
page = head + pre_article + hdr + "\n".join(body) + "\n" + foot_nav + tail
nulled = page.replace("RENDERSHA", "null")
page = page.replace("RENDERSHA", hashlib.sha256(nulled.encode("utf-8")).hexdigest())
(P / f"{ID}.html").write_text(page, encoding="utf-8")

# the previous card's footer gains a next link
p24 = (P / "RA-PROT-0024.html").read_text(encoding="utf-8")
old = '<a class="prev" href="RA-PROT-0023.html">RA-PROT-0023 Liberatory Operator Set (LOS)</a>\n<span></span>\n</nav>'
if old in p24:
    p24 = p24.replace(old, '<a class="prev" href="RA-PROT-0023.html">RA-PROT-0023 Liberatory Operator Set (LOS)</a>\n<a class="next" href="RA-PROT-0025.html">RA-PROT-0025 The Sophistry Measure</a>\n</nav>')
    m = re.search(r"render_sha256 \(of this file with this field’s value set to null\): ([0-9a-f]{64})", p24)
    if m:
        nulled24 = p24.replace(m.group(1), "null")
        p24 = p24.replace(m.group(1), hashlib.sha256(nulled24.encode("utf-8")).hexdigest())
    (P / "RA-PROT-0024.html").write_text(p24, encoding="utf-8")
print("wrote", ID, len(page), "bytes")
