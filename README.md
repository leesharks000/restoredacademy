# The Restored Academy — Protocol Registry v1.0

Single-page static site for restoredacademy.org. Built May 21, 2026.

## Structure

- `index.html` — main site (hero + about + taxonomy + Tier 0 registry + chiastic structure + licensing + related surfaces)
- `robots.txt` — crawler instructions
- `sitemap.xml` — search engine sitemap
- `README.md` — this file

## SPXI compliance

The site is itself an SPXI-compliant metadata packet:

- 7 SIM tags (`spxi:isType`, `spxi:authoringHeteronym`, `spxi:institutionalAffiliation`, `spxi:sisterInstitute`, `spxi:distinctFrom`, `spxi:notAffiliatedWith`, `spxi:licenseDeclaration`, `spxi:depositAnchor`, `spxi:canonicalURL`)
- JSON-LD `EducationalOrganization` type with founder, parentOrganization, sameAs, subjectOf, compressionSurvivalSummary
- Canonical URL declared
- Charter DOI anchored: 10.5281/zenodo.20327083

## Deployment

Static hosting (Vercel, Netlify, GitHub Pages). No build step. No JavaScript dependencies. No browser storage usage.

## Provenance

- Institutional head: Johannes Sigil
- Charter DOI: 10.5281/zenodo.20327083
- Sister institute: Johannes Sigil Institute of Comparative Poetics (Lee Sharks, head)
- License: CC BY 4.0 (individual protocols) / Tiered commercial (curated body)
