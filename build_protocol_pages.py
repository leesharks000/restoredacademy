#!/usr/bin/env python3
"""Generate per-protocol HTML pages from /protocols/*.md cards.

Each card uses the 11-section schema:
  Header (h1 with title)
  Meta line (ID, version, categories, tier)
  Sections 1-11 numbered as h2 / # headings
Output: /protocols/RA-PROT-NNNN.html
"""
import re
from pathlib import Path

PROTOCOLS_DIR = Path('/home/claude/ra-v2/protocols')
OUT_DIR = Path('/home/claude/ra-v2/protocols')

HEAD_TPL = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>{prot_id} {prot_short} — The Restored Academy Protocol Registry</title>
  <link rel="canonical" href="https://restoredacademy.org/protocols/{prot_id}.html">
  <link rel="icon" type="image/svg+xml" href="/img/favicon.svg">
  <meta name="description" content="{prot_id} — {prot_short}. {tagline}">

  <!-- SPXI compliance -->
  <meta name="spxi:isType" content="protocol card · operative method specification">
  <meta name="spxi:authoringHeteronym" content="{author}">
  <meta name="spxi:institutionalAffiliation" content="The Restored Academy · Crimson Hexagonal Archive">
  <meta name="spxi:licenseDeclaration" content="CC BY 4.0 · tiered commercial licensing for curated body">
  <meta name="spxi:depositAnchor" content="{source_doi}">
  <meta name="spxi:canonicalURL" content="https://restoredacademy.org/protocols/{prot_id}.html">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "@id": "https://restoredacademy.org/protocols/{prot_id}.html",
    "name": "{prot_id}: {prot_short}",
    "headline": "{prot_id} — {prot_short}",
    "url": "https://restoredacademy.org/protocols/{prot_id}.html",
    "isPartOf": {{
      "@type": "Collection",
      "name": "Restored Academy Protocol Registry",
      "url": "https://restoredacademy.org/"
    }},
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "author": {{ "@type": "Person", "name": "{author}" }},
    "sameAs": "{source_doi_url}"
  }}
  </script>

  <style>
    :root {{
      --ink: #1a1816; --ink-soft: #4a4540; --ink-faint: #8a8580;
      --paper: #f5f1e8; --paper-soft: #ebe6db; --paper-warm: #f9f5ec;
      --crimson: #8b1d1d; --crimson-deep: #5c1010;
      --gold: #a08438; --rule: #c8c2b3;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      font-family: 'Iowan Old Style', 'Palatino', 'Palatino Linotype', Georgia, serif;
      background: var(--paper); color: var(--ink); line-height: 1.7; font-size: 17px;
    }}
    a {{ color: var(--crimson); text-decoration: none; border-bottom: 1px solid rgba(139,29,29,0.3); }}
    a:hover {{ color: var(--crimson-deep); border-bottom-color: var(--crimson-deep); }}

    /* Top bar */
    nav.topbar {{
      background: var(--paper-warm); border-bottom: 1px solid var(--rule);
      padding: 14px 32px; position: sticky; top: 0; z-index: 100;
      display: flex; gap: 22px; align-items: center; font-size: 14px;
    }}
    nav.topbar .seal-link {{ display: inline-flex; align-items: center; gap: 8px; border: none; color: var(--ink); font-weight: 600; letter-spacing: 0.03em; }}
    nav.topbar .seal-link img {{ width: 26px; height: 26px; }}
    nav.topbar a {{ border: none; color: var(--ink-soft); font-weight: 500; }}
    nav.topbar a:hover {{ color: var(--crimson); }}
    nav.topbar .spacer {{ flex: 1; }}

    /* Layout */
    .container {{
      max-width: 1180px; margin: 0 auto; padding: 50px 32px;
      display: grid; grid-template-columns: 220px 1fr; gap: 50px;
    }}
    @media (max-width: 880px) {{
      .container {{ grid-template-columns: 1fr; gap: 28px; padding: 30px 22px; }}
      aside.toc {{ position: static !important; }}
    }}

    /* TOC sidebar */
    aside.toc {{
      position: sticky; top: 90px; align-self: start;
      font-size: 13px; line-height: 1.6;
    }}
    aside.toc h4 {{ font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--ink-faint); margin-bottom: 12px; padding-bottom: 8px; border-bottom: 1px solid var(--rule); }}
    aside.toc ol {{ list-style: none; padding: 0; counter-reset: toc; }}
    aside.toc li {{ counter-increment: toc; padding: 3px 0; }}
    aside.toc li::before {{ content: counter(toc) ". "; color: var(--gold); font-variant: small-caps; }}
    aside.toc a {{ border: none; color: var(--ink-soft); }}
    aside.toc a:hover {{ color: var(--crimson); }}

    /* Main */
    article {{ max-width: 720px; }}
    article header.prot-head {{ margin-bottom: 36px; padding-bottom: 24px; border-bottom: 2px solid var(--rule); }}
    .breadcrumb {{ font-size: 13px; color: var(--ink-faint); margin-bottom: 18px; letter-spacing: 0.04em; }}
    .breadcrumb a {{ border: none; color: var(--ink-soft); }}
    .prot-id {{ font-family: 'SF Mono', Menlo, Consolas, monospace; font-size: 13px; color: var(--gold); letter-spacing: 0.06em; }}
    h1.prot-title {{
      font-size: 38px; line-height: 1.15; font-weight: 600; letter-spacing: -0.01em;
      margin: 14px 0 16px; color: var(--ink);
    }}
    .meta-row {{
      display: flex; gap: 18px; flex-wrap: wrap; font-size: 13px; color: var(--ink-faint);
      padding-top: 12px;
    }}
    .meta-row .badge {{
      background: rgba(160,132,56,0.12); color: var(--gold);
      padding: 3px 10px; border-radius: 3px; font-size: 11px;
      letter-spacing: 0.04em; font-weight: 600;
    }}
    .meta-row .badge-tier {{ background: rgba(139,29,29,0.08); color: var(--crimson); }}
    .meta-row strong {{ color: var(--ink-soft); font-weight: 600; }}

    /* Section content */
    article h2 {{
      font-size: 22px; font-weight: 600; margin: 42px 0 14px;
      padding-bottom: 8px; border-bottom: 1px solid var(--rule);
      letter-spacing: -0.005em; scroll-margin-top: 90px;
    }}
    article h2::before {{
      content: attr(data-num) ". "; color: var(--gold); font-variant: small-caps;
      font-size: 18px;
    }}
    article p {{ margin-bottom: 16px; }}
    article ul, article ol {{ margin: 12px 0 18px 28px; }}
    article li {{ margin-bottom: 6px; }}

    /* Code blocks (the pasteable LLM blocks) */
    pre {{
      background: #f9f5ec; border-left: 3px solid var(--crimson);
      padding: 18px 22px; margin: 18px 0; border-radius: 0 3px 3px 0;
      font-family: 'SF Mono', Menlo, Consolas, monospace; font-size: 13px;
      line-height: 1.55; overflow-x: auto; position: relative;
    }}
    pre code {{ font-family: inherit; color: var(--ink); }}
    .copy-btn {{
      position: absolute; top: 8px; right: 8px;
      background: var(--paper); border: 1px solid var(--rule);
      color: var(--ink-soft); padding: 4px 10px; font-size: 11px;
      font-family: inherit; cursor: pointer; border-radius: 2px;
      letter-spacing: 0.04em;
    }}
    .copy-btn:hover {{ background: var(--gold); color: var(--paper); border-color: var(--gold); }}
    .copy-btn.copied {{ background: var(--crimson); color: var(--paper); border-color: var(--crimson); }}

    /* Inline code */
    code {{ background: rgba(160,132,56,0.10); padding: 1px 6px; border-radius: 2px; font-family: 'SF Mono', Menlo, Consolas, monospace; font-size: 0.9em; }}
    pre code {{ background: none; padding: 0; }}

    /* Related navigation */
    .footer-nav {{
      margin-top: 60px; padding-top: 24px; border-top: 1px solid var(--rule);
      display: flex; justify-content: space-between; gap: 18px; flex-wrap: wrap;
      font-size: 14px;
    }}
    .footer-nav a {{ border: none; }}
    .footer-nav .prev::before {{ content: "← "; color: var(--ink-faint); }}
    .footer-nav .next::after {{ content: " →"; color: var(--ink-faint); }}

    /* Footer */
    footer.site {{
      background: var(--paper-warm); border-top: 1px solid var(--rule);
      padding: 32px; margin-top: 80px; text-align: center;
      font-size: 13px; color: var(--ink-faint);
    }}
    footer.site .integral {{ font-family: 'STIX Two Math', 'Cambria Math', serif; color: var(--crimson); }}

    blockquote {{
      border-left: 3px solid var(--gold);
      padding: 8px 0 8px 18px; margin: 16px 0;
      color: var(--ink-soft); font-style: italic;
    }}

    strong {{ color: var(--ink); font-weight: 600; }}

    table {{
      border-collapse: collapse; margin: 14px 0 18px; width: 100%;
      font-size: 14px;
    }}
    th {{ background: var(--paper-warm); padding: 8px 10px; border-bottom: 2px solid var(--rule); text-align: left; font-weight: 600; }}
    td {{ padding: 8px 10px; border-bottom: 1px solid var(--rule); vertical-align: top; }}
  </style>
</head>
<body>

<nav class="topbar">
  <a href="/" class="seal-link">
    <img src="/img/favicon.svg" alt=""/>
    <span>The Restored Academy</span>
  </a>
  <span class="spacer"></span>
  <a href="/#taxonomy">Taxonomy</a>
  <a href="/#tier-0">Tier 0</a>
  <a href="/#tier-1">Tier 1</a>
  <a href="/search.html">Search</a>
  <a href="/license.html">License</a>
</nav>

<div class="container">

<aside class="toc">
  <h4>Card Sections</h4>
  <ol>
    <li><a href="#s1">What it does</a></li>
    <li><a href="#s2">When to use it</a></li>
    <li><a href="#s3">Inputs</a></li>
    <li><a href="#s4">Procedure</a></li>
    <li><a href="#s5">Outputs</a></li>
    <li><a href="#s6">Pasteable LLM block</a></li>
    <li><a href="#s7">Operator notes</a></li>
    <li><a href="#s8">Failure modes</a></li>
    <li><a href="#s9">Related protocols</a></li>
    <li><a href="#s10">Source DOI</a></li>
    <li><a href="#s11">License</a></li>
  </ol>
</aside>

<article>

<header class="prot-head">
  <div class="breadcrumb"><a href="/">Restored Academy</a> · <a href="/#tier-{tier_anchor}">Tier {tier_num} Registry</a> · {prot_id}</div>
  <div class="prot-id">{prot_id} · v{version}</div>
  <h1 class="prot-title">{prot_full_title}</h1>
  <div class="meta-row">
    <span><strong>Author:</strong> {author}</span>
    <span class="badge badge-tier">Tier {tier_num}</span>
{cat_badges}
    <span><strong>Status:</strong> Active</span>
  </div>
</header>

{body}

<nav class="footer-nav">
{prev_link}
{next_link}
</nav>

</article>

</div>

<footer class="site">
  <p><a href="/">← Return to Restored Academy</a> · <span class="integral">∮ = 1</span> · CC BY 4.0 individual protocol · Tiered commercial licensing for curated body</p>
</footer>

<script>
  // Copy-to-clipboard for pre blocks
  document.querySelectorAll('pre').forEach(pre => {{
    if (pre.querySelector('.copy-btn')) return;
    const btn = document.createElement('button');
    btn.className = 'copy-btn';
    btn.textContent = 'COPY';
    btn.addEventListener('click', () => {{
      const code = pre.querySelector('code') || pre;
      const text = code.innerText.replace(/^COPY\\s*/, '').trim();
      navigator.clipboard.writeText(text).then(() => {{
        btn.textContent = 'COPIED';
        btn.classList.add('copied');
        setTimeout(() => {{ btn.textContent = 'COPY'; btn.classList.remove('copied'); }}, 1600);
      }});
    }});
    pre.appendChild(btn);
  }});
</script>

</body>
</html>
"""

# Section numbering pattern: ## 1. What it does, ## 2. When to use, etc.
SECTION_PATTERN = re.compile(r'^## (\d+)\.\s+(.+)$', re.MULTILINE)

# Convert numbered ## sections into <h2 id="sN" data-num="N">title</h2>
def md_to_html_body(md_text: str) -> str:
    # Extract the main content (after the meta block, before final --- separator)
    # Find first ## section
    first_h2 = md_text.find('## 1.')
    if first_h2 == -1:
        first_h2 = 0
    
    # Find last --- before footer
    body = md_text[first_h2:]
    # Remove final --- and footer
    body = re.split(r'\n---\n', body)[0]
    
    # Convert ## N. Title to <h2 id="sN" data-num="N">Title</h2>
    body = SECTION_PATTERN.sub(
        lambda m: f'<h2 id="s{m.group(1)}" data-num="{m.group(1)}">{m.group(2).strip()}</h2>',
        body
    )
    
    # Code blocks: ```lang ... ``` → <pre><code>...</code></pre>
    body = re.sub(
        r'```(\w*)\n(.*?)```',
        lambda m: f'<pre><code>{escape_html(m.group(2))}</code></pre>',
        body,
        flags=re.DOTALL
    )
    
    # Convert markdown links [text](url) → <a href="url">text</a>
    body = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', body)
    
    # Bold **text** → <strong>text</strong>
    body = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', body)
    
    # Italic *text* → <em>text</em> (careful not to clobber within already-rendered)
    body = re.sub(r'(?<![\*a-zA-Z])\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', body)
    
    # Tables (basic GFM): | a | b |\n|---|---|\n| 1 | 2 |
    body = convert_tables(body)
    
    # Bullet lists: lines starting with - 
    body = convert_lists(body)
    
    # Paragraphs: split by blank lines, wrap non-block content in <p>
    blocks = re.split(r'\n\s*\n', body)
    out = []
    for b in blocks:
        b = b.strip()
        if not b:
            continue
        if b.startswith(('<h2', '<pre', '<ul', '<ol', '<table', '<blockquote')):
            out.append(b)
        else:
            # Skip blockquote markers > 
            if b.startswith('> '):
                quoted = re.sub(r'^> ', '', b, flags=re.MULTILINE)
                out.append(f'<blockquote>{quoted}</blockquote>')
            else:
                out.append(f'<p>{b}</p>')
    
    return '\n\n'.join(out)

def convert_tables(text):
    lines = text.split('\n')
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Detect table start: a line with | and the next line has |---|
        if '|' in line and i + 1 < len(lines) and re.match(r'^\s*\|[\s\-:|]+\|\s*$', lines[i+1]):
            # Parse table
            header = [c.strip() for c in line.strip().strip('|').split('|')]
            i += 2
            rows = []
            while i < len(lines) and '|' in lines[i]:
                row = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                rows.append(row)
                i += 1
            tbl = '<table><thead><tr>' + ''.join(f'<th>{c}</th>' for c in header) + '</tr></thead><tbody>'
            for r in rows:
                tbl += '<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>'
            tbl += '</tbody></table>'
            out.append(tbl)
        else:
            out.append(line)
            i += 1
    return '\n'.join(out)

def convert_lists(text):
    lines = text.split('\n')
    out = []
    in_list = False
    for line in lines:
        m_ul = re.match(r'^- (.+)$', line)
        m_ol = re.match(r'^\d+\.\s+(.+)$', line)
        if m_ul:
            if not in_list:
                out.append('<ul>')
                in_list = 'ul'
            out.append(f'<li>{m_ul.group(1)}</li>')
        elif m_ol:
            if not in_list:
                out.append('<ol>')
                in_list = 'ol'
            out.append(f'<li>{m_ol.group(1)}</li>')
        else:
            if in_list:
                out.append(f'</{in_list}>')
                in_list = False
            out.append(line)
    if in_list:
        out.append(f'</{in_list}>')
    return '\n'.join(out)

def escape_html(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

# Parse a card's metadata from its content
def parse_card(path: Path):
    text = path.read_text()
    
    # Title: first line after the # heading
    title_match = re.search(r'^# (.+)$', text, re.MULTILINE)
    full_title = title_match.group(1) if title_match else path.stem
    
    # Meta line: **RA-PROT-NNNN** · vX.Y · Category I (...) · Tier N
    meta_match = re.search(r'\*\*(RA-PROT-\d+)\*\*\s*·\s*v?([\d.]+)\s*·\s*(.+?)·\s*Tier\s+(\d+)', text)
    if meta_match:
        prot_id = meta_match.group(1)
        version = meta_match.group(2)
        cats_str = meta_match.group(3)
        tier_num = meta_match.group(4)
    else:
        prot_id = path.stem.split('-')[0:2]
        prot_id = '-'.join(prot_id) if isinstance(prot_id, list) else prot_id
        version = '1.0'
        cats_str = ''
        tier_num = '0'
    
    # Categories: parse Category I, Category II, etc.
    cats = re.findall(r'Category\s+(\w+)\s*\(([^)]+)\)', cats_str)
    cat_badges = ''
    for roman, name in cats:
        cat_badges += f'    <span class="badge">Cat {roman}</span>\n'
    
    # Author / heteronym (from "**Authoring heteronym:**" line near end)
    author_match = re.search(r'\*\*Authoring heteronym:\*\*\s*([^·\n]+)', text)
    author = author_match.group(1).strip() if author_match else 'Lee Sharks'
    
    # Source DOI from section 10
    doi_match = re.search(r'\[10\.5281/zenodo\.(\d+)\]', text)
    source_doi = f'10.5281/zenodo.{doi_match.group(1)}' if doi_match else ''
    source_doi_url = f'https://doi.org/{source_doi}' if source_doi else ''
    
    # Short name = title before the first colon, or the part after the dash
    prot_short = full_title
    # Tagline = first sentence of "## 1. What it does" section
    s1_match = re.search(r'## 1\.\s+What it does\s*\n+(.+?)(?=\n\n|\n##)', text, re.DOTALL)
    tagline = ''
    if s1_match:
        first = s1_match.group(1).strip().split('.')[0]
        tagline = first[:200]
    
    return {
        'prot_id': prot_id,
        'version': version,
        'tier_num': tier_num,
        'tier_anchor': tier_num,
        'cat_badges': cat_badges.rstrip(),
        'author': author,
        'source_doi': source_doi,
        'source_doi_url': source_doi_url,
        'prot_short': prot_short,
        'prot_full_title': full_title,
        'tagline': tagline,
        'body': md_to_html_body(text),
    }

# Generate all pages
cards = sorted(PROTOCOLS_DIR.glob('RA-PROT-*.md'))
all_meta = []
for path in cards:
    meta = parse_card(path)
    meta['source_path'] = path
    all_meta.append(meta)

# Build prev/next links
for i, meta in enumerate(all_meta):
    if i > 0:
        p = all_meta[i-1]
        meta['prev_link'] = f'<a class="prev" href="{p["prot_id"]}.html">{p["prot_id"]} {p["prot_short"][:60]}</a>'
    else:
        meta['prev_link'] = '<span></span>'
    if i < len(all_meta) - 1:
        n = all_meta[i+1]
        meta['next_link'] = f'<a class="next" href="{n["prot_id"]}.html">{n["prot_id"]} {n["prot_short"][:60]}</a>'
    else:
        meta['next_link'] = '<span></span>'

# Render each
for meta in all_meta:
    html = HEAD_TPL.format(**meta)
    out_path = OUT_DIR / f"{meta['prot_id']}.html"
    out_path.write_text(html)

print(f"Generated {len(all_meta)} protocol pages.")
for m in all_meta:
    print(f"  {m['prot_id']} · {m['prot_short'][:50]}")

# Also generate a JSON index for search
import json
index = []
for m in all_meta:
    body_text = re.sub(r'<[^>]+>', ' ', m['body'])
    body_text = re.sub(r'\s+', ' ', body_text).strip()
    index.append({
        'id': m['prot_id'],
        'title': m['prot_short'],
        'tier': m['tier_num'],
        'author': m['author'],
        'doi': m['source_doi'],
        'tagline': m['tagline'],
        'text': body_text[:1500],
        'cats': re.findall(r'Cat (\w+)', m['cat_badges']),
    })

(Path('/home/claude/ra-v2/data') / 'protocols.json').write_text(json.dumps(index, indent=2))
print(f"\nSearch index: data/protocols.json ({len(index)} entries)")
