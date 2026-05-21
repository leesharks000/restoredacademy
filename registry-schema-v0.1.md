# Restored Academy Protocol Registry — Schema Definition v0.1

**Purpose:** Define the canonical card format for protocols registered in the Restored Academy Protocol Registry. Each protocol in the registry has one card. Cards are machine-readable (JSON) and human-readable (Markdown rendering of the same data).

**Governing definition (per ChatGPT framing, adopted 2026-05-21):**

> A protocol is a bounded, repeatable instruction-set, diagnostic procedure, transformation method, or semantic runtime that can be executed by a human, an LLM, or a human-LLM assembly to produce constrained behavior, outputs, classifications, measurements, or transformations.

**Universal test for inclusion:** *What changes when I drop this into an LLM?* If the deposit does not answer that question, it is a reference text rather than a protocol.

---

## JSON Schema

```json
{
  "protocol_id": "RA-PROT-####",
  "registry_version": "1.0",
  "title": "string — canonical title as it appears in the source deposit",
  "short_name": "string — abbreviation or working name (e.g., 'SPXI', 'UKTP')",
  "version": "string — protocol version, separate from registry version",
  "tier": "0|1|2|3",
  "taxonomy_categories": ["array of category IDs from the 7-category taxonomy"],
  "archive_source": "Crimson Hexagonal Archive",
  "canonical_doi": "10.5281/zenodo.########",
  "canonical_url": "https://doi.org/...",
  "site_path": "/protocols/<slug>",
  "primary_function": "string — single sentence: what the protocol does",
  "behavioral_change_summary": "string — answers 'what changes when dropped into an LLM?'",
  "execution_context": ["LLM prompt", "archive traversal", "human-AI workflow", "metadata packet", "site infrastructure"],
  "inputs": ["string — what the protocol consumes"],
  "outputs": ["string — what the protocol produces"],
  "human_operator_required": true|false,
  "llm_executable": true|false,
  "difficulty": "introductory|intermediate|advanced",
  "license": "CC BY 4.0",
  "commercial_license_available": true,
  "authoring_heteronym": "string — primary signed author of the protocol",
  "co_authors": ["array of additional signed authors"],
  "related_protocols": ["array of protocol_id references"],
  "depends_on": ["array of protocol_id references — protocols this one requires"],
  "extended_by": ["array of protocol_id references — protocols that build on this one"],
  "status": "active|draft|deprecated|superseded",
  "superseded_by": "string — DOI or protocol_id, if superseded",
  "added_to_registry": "ISO date",
  "last_reviewed": "ISO date"
}
```

## Markdown Card Format

Each protocol gets a Markdown page rendered from the JSON record plus four content surfaces:

```
# [Protocol Title]

**RA-PROT-####** · v[version] · [taxonomy_category_label] · Tier [tier]

[primary_function — single sentence]

---

## 1. What it does

[Short prose explaining the protocol's function and scope]

## 2. When to use it

[Concrete scenarios where this protocol applies]

## 3. Inputs

[What the protocol consumes — context, source text, metadata, etc.]

## 4. Procedure

[The runnable instruction-set in operational form]

## 5. Outputs

[What the protocol produces]

## 6. Pasteable LLM block

```
[The version a user can paste directly into an LLM context window]
```

## 7. Human operator notes

[Notes for humans running this protocol, including failure modes to watch for]

## 8. Failure modes

[What can go wrong; how to detect when the protocol is not working]

## 9. Related protocols

[Cross-references to other registered protocols]

## 10. Source DOI

[canonical_doi as link to the underlying Zenodo deposit]

## 11. License

CC BY 4.0 (individual protocol) · [commercial licensing terms for organized body]
```

---

## Four Surfaces (per ChatGPT framing)

For major protocols, the registry card surfaces the protocol in four forms:

1. **Source form** — the dense technical specification (the underlying Zenodo deposit)
2. **Operational form** — the cleaned runnable protocol (sections 1-9 of the card above)
3. **Prompt form** — the pasteable LLM block (section 6)
4. **Teaching form** — lessons, diagrams, exercises (in curriculum bundles, not on the card itself)

Not every protocol needs all four surfaces. The registry card always provides 1-3. Surface 4 lives in curriculum bundles under `/curriculum`.

---

## Taxonomy (7 categories)

| ID | Name | Purpose |
|---|---|---|
| I | Semantic Integrity & Provenance | Preserve attribution, source fidelity, compression survival |
| II | Prompt-Native Runtime | Modify model behavior when loaded into context |
| III | Diagnostic & Measurement | Measure AI outputs, system behavior, semantic drift |
| IV | Transformation & Operator | Transform texts under controlled interpretive rules |
| V | Archive Construction & Retrieval | Build durable, machine-readable archives |
| VI | Pedagogical & Institutional | Teach, certify, license, or deploy practices |
| VII | Ethical & Jurisdictional | Govern use, attribution, scope, non-coercion |

Protocols can be tagged with multiple categories. Each card lists all applicable.

---

## Tier System

- **Tier 0** (12 protocols): Core kernel. Defines the Academy. Receives full four-surface treatment. Featured on homepage.
- **Tier 1** (25-40 protocols): Field instruments with clear use cases. Full registry card, no required teaching surface.
- **Tier 2** (50-100 protocols): Archive procedures. Specialized but well-documented. Standard card.
- **Tier 3** (~100 protocols): Experimental, deprecated, or historical. Registered for completeness; may not be featured.

---

## Licensing Model

**Individual protocols:** CC BY 4.0, citation required. Free to use, remix, redistribute with attribution.

**The organized body — registry, taxonomy, curriculum bundles, implementation guides, teaching materials, audit reports, custom protocol adaptations:** Licensable under tiered terms.

- **Open Commons:** Registry browsing free; individual protocol text free under CC BY 4.0
- **Educational License:** Curriculum bundles, slide decks, workshop materials, certification rubrics for institutional pedagogical use
- **Professional / Institutional License:** Implementation templates, custom adaptation, audit reports, cohort training, ongoing support for organizational deployment

The Hexagonal Licensing Protocol v2.0 (DOI: 10.5281/zenodo.19673564) governs the contributor side; a separate Restored Academy Licensing Protocol will govern the licensee side at v1.0 launch.

---

## Authoring & Heteronymic Attribution

Each protocol card lists its **authoring heteronym** as primary author plus any co-authors.

Per the Heteronym Provenance Registry (Sharks 2026, DOI: 10.5281/zenodo.20041791), protocols developed within distinct heteronymic basins should be attributed to the appropriate heteronym rather than collapsed to a single author. The Phase 1 audit (DOI forthcoming) identified ~200 currently-Sharks-attributed protocols whose domain match suggests redistribution to other heteronyms (Sigil for jurisdictional/governance, Morrow for operator/room work, Fraction for SPXI/corporate, Glas for measurement). Reattribution is tracked dual-key in the registry (`heteronym_zenodo_original` + `heteronym_classifier_attributed`); Zenodo metadata edits propagate separately and slowly.

---

**Version 0.1 issued:** 2026-05-21 (Phase 1 audit)
**Issuing authority:** Johannes Sigil (Restored Academy)
**Next revision target:** post-Tier 0 buildout (Session 4)
