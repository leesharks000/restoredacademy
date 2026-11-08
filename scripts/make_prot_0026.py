#!/usr/bin/env python3
"""RA-PROT-0026, the Framework Holographic Kernel (Alexanarch #1753, EA-HK-FRAME-01 v1.1, Sen Kuro and Rex Fraction): the 11-section card
(protocols/RA-PROT-0026-Framework-Holographic-Kernel.md) and its page (protocols/RA-PROT-0026.html) from one content table, the page taking
RA-PROT-0025.html's head, styles, chrome and apparatus with only the card's own fields replaced. RA-PROT-0005 (Holographic Kernel) gains the
card among its related protocols, and RA-PROT-0025's footer the next link; each changed page's render_sha256 is recomputed with its own value
nulled. 2026-11-08, at the author's word: "framework hk should go to hk and restoredacademy"; "adopted for all three"."""
import hashlib, html, pathlib, re
R = pathlib.Path(__file__).resolve().parents[1]
P = R / "protocols"
ID, SHORT, VER = "RA-PROT-0026", "The Framework Holographic Kernel", "v1.1"
AUTHOR = "Sen Kuro and Rex Fraction"
REC, AXN, AXN_GLYPH = "https://www.alexanarch.org/s/records/1753/", "AXN:0C54.OPERATIVE", "☿☿⚙️🀄🍃🛸"
HOLO = "https://www.alexanarch.org/s/records/1754/"
LEDE = ("The holographic kernel built at a framework's grain: a package written from an archive's registries by its own builder and tested by its own "
        "verifier, from which a framework's identity, positions, dated development, evidence bodies, claim states, failures, rival and open questions "
        "are rebuilt and checked against the records.")
S = [
 ("What it does", [
   ("p", "A summary discards structure to save space; a kernel discards material to save structure (RA-PROT-0005). The Framework Holographic Kernel applies that operation to a framework: an argument with a seed record, an author, positions, a development in time and evidence of several kinds."),
   ("p", "Its package holds the framework's identity and invariants, an ontology of positions, evidence bodies and claim states, a graph of every record and claim under a relation policy, the claims, two timelines, the lines of research, the captures, a traversal, tests, a verification and integrity hashes. A claim is a pointer to a quotation in its record, bound to the record's hash, and never a restatement. A correction is kept as three objects: the withdrawn original, the standing correction and the dated withdrawal. A claim's introduction is dated from the record's first seating in git."),
   ("p", "The framework carries its rival. The received reading of the field is evaluated on the same evidence bodies under the same rules, and since v1.1 the two sit side by side in one ledger: one question asked of both on every body, with the rule by which the bodies combine and the rule by which a further model enters as a rival. Each open question is an object: the record that poses it, how a researcher asks it, how a machine investigates it, and what result would advance or retreat the framework and what it moves."),
 ]),
 ("When to use it", [
   ("p", "Build a framework kernel when:"),
   ("ul", ["A framework has developed across many records, with claims introduced, qualified and withdrawn over time",
           "Machine readers compose the framework from fragments and need a path from each fragment back to the whole, with the scope each fragment has not reconstructed",
           "The framework stands against a received reading whose standing comes from reception, and both are to be evaluated on the same evidence",
           "Open questions are to be handed to readers, human or machine, as work that would settle a claim"]),
 ]),
 ("Inputs", [
   ("p", "The archive's registry of records with their identifiers and hashes; the capture registry of the framework's reception; the repository history, from which each record's first seating is recovered; and the author's positions, evidence bodies, strata, clusters and relations, each quoted at a record."),
 ]),
 ("Procedure", [
   ("ol", ["Write the seed: agents, operations, dependencies, constraints, topology (RA-PROT-0007).",
           "Bind every claim to a quotation in its record and to the record's hash; type its state on named axes.",
           "Keep each correction as original, correction and withdrawal, joined by a relation that licenses the change.",
           "Date every introduction from the record's first seating; mark unresolved what the first seating does not attest.",
           "Evaluate the rival on the same bodies and rules, and set both in one ledger, every answer warranted by claims of that body.",
           "Write each open question with its instrument, how to ask it, how a machine investigates it, and what each result moves.",
           "Run the verifier: structural tests, licensed propagation, historical reconstruction at stated dates.",
           "Give the kernel alone to readers who have not seen the records and score what they rebuild against the graph (threshold 0.85)."]),
 ]),
 ("Outputs", [
   ("p", "The kernel package, its verification report and integrity hashes, the reader runs with their scores, and a record holding the framework's map beside its kernel: the framework hologram."),
 ]),
 ("Pasteable LLM block", [
   ("pre", "Under the Framework Holographic Kernel (EA-HK-FRAME-01, Alexanarch #1753), the reader of a framework resolves each claim to the quotation and record hash it points to, changes a claim's state only along a relation that licenses that dimension, keeps a withdrawn original beside the finding that corrected it, and dates a claim from its record's first seating. Evaluating either the framework or its rival on an evidence body, the reader states both frameworks' standing on that body in the same row. A further production model enters as a rival only with a warrant on a body or a documented comparator. Meeting a claim it cannot settle, the reader takes up the line of research that bears on it. The reader states the scope it has not reconstructed."),
 ]),
 ("Human operator notes", [
   ("ul", ["The kernel succeeds when its framework can be rebuilt from it at the grain and date of each claim; whether the framework is true is the framework's own question, carried in the ledger and the lines of research.",
           "The verifier checks structure, licensing and dates. It does not judge whether a reading is right or a warrant sufficient.",
           f"The first instance is the hologram of Socrates as Orthonym ([Alexanarch #1754]({HOLO})): 40 records, 56 claims, 136 edges, ten lines of research, seventeen tests; a second round of reader runs averaged 0.977.",
           "Each review and reader run that changed the kernel is recorded with what it changed."]),
 ]),
 ("Failure modes", [
   ("ul", ["Paraphrasing a claim in place of pointing at it → the claim drifts from its record",
           "Deleting a corrected claim → the history of the correction disappears",
           "Asking one framework, body by body, whether it is established while the other is left unasked → the received reading takes a default standing",
           "Entering a rival on its logical possibility → a model with no warrant is weighed as though it had one",
           "Judging the kernel by whether it proves its framework → the object of the test is changed"]),
 ]),
 ("Related protocols", [
   ("ul", ["RA-PROT-0005 (Holographic Kernel) — the general definition this card builds at a framework's grain",
           "RA-PROT-0007 (UKTP) — the seed extraction",
           "RA-PROT-0002 (MPAI) — the map that is the hologram's human-readable component",
           "RA-PROT-0006 (Space Ark) — the non-collapse chain, extended here with FRAGMENT ≠ WHOLE"]),
 ]),
 ("Source DOI", [
   ("p", f"No DOI. [Alexanarch deposit #1753]({REC}) — {AXN}.{AXN_GLYPH} — The Framework Holographic Kernel: A Specification, with Its First Instance, Socrates as Orthonym (EA-HK-FRAME-01 v1.1) (Kuro and Fraction, 2026-11-08). First instance: [Alexanarch #1754]({HOLO}). Also at [holographickernel.org](https://www.holographickernel.org/)."),
 ]),
 ("License", [
   ("p", "CC BY 4.0. Commercial licensing through The Restored Academy for organizational framework kernels."),
 ]),
]
md = [f"# {SHORT}", "", f"**{ID}** · {VER} · Category I (Semantic Integrity & Provenance), Category III (Diagnostic & Measurement) · Tier 1", "", LEDE, "", "---", ""]
for n, (h, blocks) in enumerate(S, 1):
    md += [f"## {n}. {h}", ""]
    for kind, v in blocks:
        if kind == "p": md += [v, ""]
        elif kind == "ul": md += [f"- {x}" for x in v] + [""]
        elif kind == "ol": md += [f"{i}. {x}" for i, x in enumerate(v, 1)] + [""]
        elif kind == "pre": md += ["```", v, "```", ""]
md += ["---", "", f"**Authoring heteronyms:** {AUTHOR} · **Status:** Active · **Added:** 2026-11-08", ""]
(P / f"{ID}-Framework-Holographic-Kernel.md").write_text("\n".join(md), encoding="utf-8")

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    return re.sub(r"\*([^*\n]+)\*", r"<em>\1</em>", t)
body = []
for n, (h, blocks) in enumerate(S, 1):
    body.append(f'<h2 data-num="{n}" id="s{n}">{h}</h2>')
    for kind, v in blocks:
        if kind == "p": body.append(f"<p>{inline(v)}</p>")
        elif kind in ("ul", "ol"): body.append(f"<{kind}>" + "".join(f"<li>{inline(x)}</li>" for x in v) + f"</{kind}>")
        elif kind == "pre": body.append(f"<pre><code>{html.escape(v, quote=False)}</code></pre>")

def rehash(page):
    m = re.search(r"render_sha256 \(of this file with this field’s value set to null\): ([0-9a-f]{64}|RENDERSHA)", page)
    nulled = page.replace(m.group(1), "null")
    return page.replace(m.group(1), hashlib.sha256(nulled.encode("utf-8")).hexdigest())

t = (P / "RA-PROT-0025.html").read_text(encoding="utf-8")
head_end = t.index("</head>"); head = t[:head_end]
desc = f"{ID} — {SHORT}. {LEDE}"
head = head.replace("RA-PROT-0025", ID).replace("The Sophistry Measure", SHORT)
head = re.sub(rf'<meta content="{ID} — [^"]*" name="description"/>', f'<meta content="{html.escape(desc)}" name="description"/>', head)
head = head.replace('<meta content="Lee Sharks" name="spxi:authoringHeteronym"/>', f'<meta content="{AUTHOR}" name="spxi:authoringHeteronym"/>')
head = head.replace('<meta content="https://www.alexanarch.org/s/records/1727/" name="spxi:depositAnchor"/>', f'<meta content="{REC}" name="spxi:depositAnchor"/>')
head = head.replace('"author": { "@type": "Person", "name": "Lee Sharks" }', '"author": [{ "@type": "Person", "name": "Sen Kuro" }, { "@type": "Person", "name": "Rex Fraction" }]')
head = head.replace('"sameAs": "https://www.alexanarch.org/s/records/1727/"', f'"sameAs": "{REC}"')
assert "/records/1727/" not in head and "Sophistry" not in head, [x for x in ("1727", "Sophistry") if x in head]
pre_article = t[head_end:t.index('<header class="prot-head">')]
pre_article = pre_article.replace('<span class="axn">💛🗿🛡️🔖🧬🛸 AXN:0BDC.OPERATIVE</span>', f'<span class="axn">{AXN_GLYPH} {AXN}</span>')
pre_article = pre_article.replace("RA-PROT-0025 The Sophistry Measure", f"{ID} {SHORT}").replace("restoredacademy.com/protocols/RA-PROT-0025.html", f"restoredacademy.com/protocols/{ID}.html")
pre_article = pre_article.replace(f'href="https://www.alexanarch.org/s/records/1727/">deposit #1727</a>', f'href="{REC}">deposit #1753</a>')
assert "RA-PROT-0025" not in pre_article and "0BDC" not in pre_article and "1727" not in pre_article
hdr = (f'<header class="prot-head">\n<div class="breadcrumb"><a href="/">Restored Academy</a> · <a href="/#tier-1">Tier 1 Registry</a> · {ID}</div>\n'
       f'<div class="prot-id">{ID} · {VER}</div>\n<h1 class="prot-title">{SHORT}</h1>\n<div class="meta-row">\n<span><strong>Authors:</strong> {AUTHOR}</span>\n'
       '<span class="badge badge-tier">Tier 1</span>\n<span class="badge">Cat I</span>\n<span class="badge">Cat III</span>\n<span><strong>Status:</strong> Active</span>\n</div>\n</header>\n')
foot_nav = '<nav class="footer-nav">\n<a class="prev" href="RA-PROT-0025.html">RA-PROT-0025 The Sophistry Measure</a>\n<span></span>\n</nav>\n</article>\n</div>\n'
tail = t[t.index("<!-- MSP-APPARATUS-START -->"):]
tail = re.sub(r'<div class="mspcolophon">.*?</div>',
              (f'<div class="mspcolophon">colophon · surface_id: restoredacademy.com/protocols/{ID}.html · canonical_url: https://restoredacademy.com/protocols/{ID}.html · '
               f'object_state: canonical · surface_observed_at: 2026-11-08T00:00:00Z · source_object_ids: deposit #1753 · source_hashes: see the seat · '
               f'generator_version: scripts/make_prot_0026.py · repository_commit: see correction_log_url · model_or_agent: drafted with Claude (TACHYON), MANUS-directed · '
               f'operator_sequence: n/a · human_approver: Lee Sharks (MANUS) · approval_timestamp: 2026-11-08 · render_sha256 (of this file with this field’s value set to null): RENDERSHA · '
               f'correction_log_url: https://github.com/leesharks000/restoredacademy/commits/main/protocols/{ID}.html — EA-APPARATUS-01 v0.3, AXN:0446.OPERATIVE.🏛️🛡️🌅🎆📏🔎</div>'),
              tail, count=1, flags=re.S)
page = rehash(head + pre_article + hdr + "\n".join(body) + "\n" + foot_nav + tail)
(P / f"{ID}.html").write_text(page, encoding="utf-8")

p25 = (P / "RA-PROT-0025.html").read_text(encoding="utf-8")
old = '<a class="prev" href="RA-PROT-0024.html">RA-PROT-0024 β-Runtime Specification</a>\n<span></span>\n</nav>'
if old in p25:
    p25 = p25.replace(old, f'<a class="prev" href="RA-PROT-0024.html">RA-PROT-0024 β-Runtime Specification</a>\n<a class="next" href="{ID}.html">{ID} {SHORT}</a>\n</nav>')
    (P / "RA-PROT-0025.html").write_text(rehash(p25), encoding="utf-8")

LINE5 = f"- {ID} (Framework Holographic Kernel) — the kernel built at a framework's grain, with its first instance"
m5 = P / "RA-PROT-0005-Holographic-Kernel.md"; s5 = m5.read_text(encoding="utf-8")
a = "- RA-PROT-0010 (CDI) — measures composed-output divergence from Kernel-inscribed claims\n"
if LINE5 not in s5:
    assert a in s5; m5.write_text(s5.replace(a, a + LINE5 + "\n"), encoding="utf-8")
h5p = P / "RA-PROT-0005.html"; h5 = h5p.read_text(encoding="utf-8")
li = f'<li><a href="{ID}.html">{ID}</a> (Framework Holographic Kernel) — the kernel built at a framework\'s grain, with its first instance</li>'
if ID not in h5:
    i = h5.index('id="s9"'); j = h5.index("</ul>", i)
    h5p.write_text(rehash(h5[:j] + li + h5[j:]), encoding="utf-8")
print("wrote", ID, len(page), "bytes")
