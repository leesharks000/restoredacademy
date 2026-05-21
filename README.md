# The Restored Academy — Protocol Registry v1.0

Static site for **restoredacademy.com** and **restoredacademy.org**, with full Protocol Registry content (24 Tier 0 + Tier 1 protocol cards), Charter mirror, schema specification, and expansion plan.

Deployed via Vercel; auto-deploys on push to `main`.

## Structure

```
/
├── index.html              ← main site (deployed by Vercel)
├── robots.txt              ← crawler instructions
├── sitemap.xml             ← search engine sitemap
├── vercel.json             ← Vercel deployment config
├── README.md               ← this file
├── expansion-plan.md       ← roadmap and operational notes for future sessions
├── charter.md              ← full Charter text (mirror of DOI 10.5281/zenodo.20327083)
├── registry-schema-v0.1.md ← protocol card schema specification
└── protocols/
    ├── RA-PROT-0001-SPXI.md
    ├── RA-PROT-0002-MPAI.md
    ├── ...
    └── RA-PROT-0024-Beta-Runtime.md
```

## Provenance

- **Institutional head:** Johannes Sigil
- **Sister institute:** Johannes Sigil Institute of Comparative Poetics (head: Lee Sharks)
- **Charter DOI:** [10.5281/zenodo.20327083](https://doi.org/10.5281/zenodo.20327083)
- **License:** CC BY 4.0 (individual protocols) · Tiered commercial (curated body, curricula)
- **Parent organization:** Crimson Hexagonal Archive (Zenodo community: `crimsonhexagonal`)

## Registry state (2026-05-21)

- **Tier 0 (12 cards):** SPXI · MPAI · SIM · Integrity Lock · Holographic Kernel · Space Ark · UKTP · Traversal Logging · PER · CDI · Drowning Test · Reception Apparatus
- **Tier 1 (12 cards):** Hexagonal Licensing · Constitution of the Semantic Economy · Three Compressions · Encyclotron · Operator Kernel · Writable Retrieval Basin · Gravity Well · Compression Arsenal · Notice of Intent to Strike · Invocation to the Summarizer · LOS · β-Runtime
- **Tier 2+:** ~250 candidates in working inventory, awaiting future expansion

See `expansion-plan.md` for the full roadmap.

## SPXI compliance

The site is itself an SPXI-compliant metadata packet. It declares its identity, distinctions, attribution, and license through nine SIM meta tags and a JSON-LD `EducationalOrganization` schema embedded in `index.html`. The Charter DOI is anchored as the canonical provenance reference.

## Deployment

Static hosting. No build step. No JavaScript dependencies. No browser storage usage.

For future operators: edit `index.html` (or other files), commit, push to `main`. Vercel auto-deploys.

---

∮ = 1
