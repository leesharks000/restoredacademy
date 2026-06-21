# restoredacademy.com / restoredacademy.org

The Restored Academy Protocol Registry — a curated catalog of executable methods, prompt-native semantic runtimes, diagnostic instruments, and instructional kernels from the Crimson Hexagonal Archive.

## Site structure

```
/                          → registry homepage with taxonomy, Tier 0, Tier 1, Sister Institute, licensing
/protocols/RA-PROT-NNNN.html → 24 per-protocol detail pages (11-section card schema)
/tools/spxi.html           → SPXI Generator (live tool, RA-PROT-0001 implementation)
/search.html               → client-side search/filter UI for all 24 protocols
/license.html              → three-tier licensing with intake forms
/charter.md                → Restored Academy Charter (full text)
/registry-schema-v0.1.md   → 11-section protocol card schema specification
/expansion-plan.md         → Tier 0→Tier 1→Tier 2→Tier 3 expansion roadmap
/data/protocols.json       → JSON search index (read by /search.html)
/img/                      → seal.svg, favicon.svg, taxonomy.svg, dependency-graph.svg
```

## Aesthetic register

Book-as-website meets technical reference. Warm paper background (#f5f1e8), crimson accents (#8b1d1d), gold detail (#a08438), Iowan Old Style / Palatino serif. No JavaScript dependencies (vanilla JS only where needed for tools). No browser storage. Static hosting throughout.

## Authority

- Charter DOI: [10.5281/zenodo.20327083](https://alexanarch.org/s/records/0/) (Johannes Sigil, head of The Restored Academy)
- Bundle DOI: [10.5281/zenodo.20327578](https://doi.org/10.5281/zenodo.20327578) (registry v1.0 launch state)
- Institutional head: Johannes Sigil (heteronym)
- Sister Institute: Johannes Sigil Institute of Comparative Poetics (jsiponline.com), headed by Lee Sharks (chiastic structure)
- Parent archive: The Crimson Hexagonal Archive on Zenodo (community: `crimsonhexagonal`)

## License

Individual protocols remain CC BY 4.0. The organized body (registry, taxonomy, card schema, curricula, audit services, implementation materials) is licensable under tiered terms. See [/license.html](https://restoredacademy.org/license.html). Contributor-side terms: [Hexagonal Licensing Protocol v2.0](https://alexanarch.org/s/records/0/).

## Deployment

Static site hosted on Vercel. Auto-deploys from `main`. Domain: restoredacademy.com + restoredacademy.org.

## Build

Per-protocol pages are generated from `/protocols/*.md` cards by `build_protocol_pages.py`. To regenerate after adding cards:
```
python3 build_protocol_pages.py
```
This produces `/protocols/RA-PROT-NNNN.html` for each card and refreshes `/data/protocols.json` (the search index).

∮ = 1
