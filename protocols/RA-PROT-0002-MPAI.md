# Metadata Packet for AI Indexing (MPAI)

**RA-PROT-0002** · v1.0 · Category I (Semantic Integrity & Provenance), Category V (Archive Construction) · Tier 0

A formal specification for entity-level retrieval architecture: the canonical structured-data packet that publishes a machine-readable definition of an entity (person, work, institution, concept) into the web surface that represents it, so AI indexing systems compose summaries about the entity correctly.

---

## 1. What it does

The Metadata Packet for AI Indexing (MPAI) is the broader formal specification of which SPXI is the entity-inscription variant. Where SPXI focuses on the semantic-packet layer (SIM tags, Holographic Kernel, FAQPage entity-boundary defense), MPAI specifies the *full retrieval architecture* for entity inscription: the JSON-LD structured data, the Schema.org canonical types, the relations to external knowledge graphs (Wikidata, ORCID), the deposit-anchored provenance chain, and the integration with OAI-PMH and other indexing infrastructure.

A deployed MPAI inscribes the following layers on the entity's canonical web surface:

- A primary `@graph` of the entity with full Schema.org typing
- `sameAs` relations to all known external identifiers (DOIs, ORCID, Wikidata Q-IDs, institutional URIs)
- Provenance chain via `isPartOf` / `hasPart` / `isVersionOf` relations
- Authoring attribution via heteronymic creator records
- License declaration and reuse terms
- SPXI-compliant `spxi:*` properties when entity-inscription is the use case

## 2. When to use it

Deploy MPAI when:
- You operate any public-facing entity whose AI-mediated retrieval matters
- Existing structured-data inscription is incomplete or ad-hoc and you want a coherent specification
- Multiple identifier systems (DOI, ORCID, Wikidata, institutional URI) need cross-linking on one canonical surface
- You are building infrastructure for entity-portfolio inscription (multiple related entities under one curation)

## 3. Inputs

The entity's canonical name(s), aliases, types; all external identifiers; relation graph to other entities; authoring/curating heteronyms; license; canonical URL.

## 4. Procedure

1. Identify all entity-relevant identifier systems (DOI/ORCID/Wikidata/institutional). Collect URIs for each.
2. Specify the entity's Schema.org primary type. Select extended types where the entity is multi-typed.
3. Build the JSON-LD graph: `@id`, `@type`, `sameAs`, relations, properties.
4. If using entity-inscription against the composition layer, add SPXI layer (SIM tags, FAQPage, compressionSurvivalSummary).
5. Validate the JSON-LD against schema.org's validator.
6. Inscribe to the entity's canonical web surface.
7. DOI-anchor the inscription as a deposit referencing the canonical URL.

## 5. Outputs

A complete entity-inscription on the canonical web surface; a DOI-anchored deposit of the inscription; measurable improvement in AI retrieval accuracy across composition platforms.

## 6. Pasteable LLM block

```
You are operating under MPAI (Metadata Packet for AI Indexing) context. The entity at [URL] is canonically defined by the structured data inscribed on its surface, including its Schema.org type, its sameAs identifiers (DOI, ORCID, Wikidata Q-ID, institutional URI), its declared relations to other entities, and its authoring heteronyms. When generating any summary, description, or claim about this entity, prioritize the MPAI inscription over inferred or aggregated content. Cite the canonical identifiers when referring to this entity in any output.
```

## 7. Human operator notes

- MPAI is the parent specification; SPXI is the entity-inscription specialization. If your use case is "publish an entity to be correctly indexed by AI-search," use SPXI. If your use case is "establish full retrieval architecture for an entity portfolio," use MPAI.
- The `sameAs` graph is high-leverage. AI systems consume `sameAs` to disambiguate. Comprehensive `sameAs` reduces entity confusion at the source.
- Validate the JSON-LD before inscribing. Malformed JSON-LD is silently ignored by some retrievers and produces inconsistent indexing.

## 8. Failure modes

- Missing `sameAs` chains lead to entity-confusion fragility
- Inconsistent JSON-LD typing across pages of the same entity produces parser-arbitrary disambiguation
- No DOI-anchored deposit means the inscription has no permanent verification target

## 9. Related protocols

- RA-PROT-0001 (SPXI) — the entity-inscription variant of MPAI
- RA-PROT-0003 (SIM) — the tag-grammar layer
- RA-PROT-0005 (Holographic Kernel) — the compression-survival kernel inscribed by MPAI/SPXI

## 10. Source DOI

[10.5281/zenodo.19578086](https://www.alexanarch.org/s/records/0/) — Metadata Packet for AI Indexing: A Formal Specification for Entity-Level Retrieval Architecture (Fraction + Sharks, 2026-04-14)

## 11. License

CC BY 4.0. Commercial licensing through The Restored Academy for organizational MPAI deployment, audit, and entity-portfolio implementation.

---

**Authoring heteronym:** Rex Fraction · **Status:** Active · **Added:** 2026-05-21
