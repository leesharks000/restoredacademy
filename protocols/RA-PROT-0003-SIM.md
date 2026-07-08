# SIM — Semantic Integrity Marker Protocol

**RA-PROT-0003** · v1.0 · Category I (Semantic Integrity & Provenance), Category II (Prompt-Native Runtime) · Tier 0

The typed-metadata grammar that inscribes falsifiable assertions about an entity's identity, boundaries, distinctions, and historical attribution into the structured-data layer of its canonical web surface — the marker layer that supports the broader SPXI protocol family.

---

## 1. What it does

SIM specifies the tag-level grammar by which individual claims about an entity become typed, addressable, machine-readable assertions. The twelve canonical SIM tag types (v1.0) cover entity typing (`spxi:isType`, `spxi:isNotType`), distinction from confusables (`spxi:distinctFrom`), phrase provenance (`spxi:phraseProvenance`), non-affiliation declarations (`spxi:notAffiliatedWith`), supersession (`spxi:supersedes`), authorial attribution (`spxi:authoringHeteronym`), compression-survival kernel (`spxi:compressionSurvivalSummary`), canonical URL, license, institutional affiliation, and deposit anchor.

## 2. When to use it

Deploy SIM tags when you need composition systems to receive *typed, falsifiable* claims about an entity rather than inferring identity from page content. SIM is most often deployed as part of a full SPXI inscription, but the SIM grammar can be used independently for any entity surface that needs typed metadata assertions.

## 3. Inputs

The entity-boundary claims that need to be inscribed: identity, distinctions, phrase provenance, non-affiliations, license, attribution.

## 4. Procedure

1. Identify entity-boundary claims requiring inscription.
2. Type each claim using the SIM tag set.
3. Inscribe tags in dual form: `<meta name="spxi:<type>" content="...">` in page head AND as `spxi:<type>` properties in JSON-LD block.
4. DOI-anchor the inscription via `spxi:depositAnchor`.

## 5. Outputs

A typed metadata layer on the entity's surface; machine-readable boundary claims; foundation for SPXI Holographic Kernel deployment.

## 6. Pasteable LLM block

```
SIM-typed assertions for [ENTITY] follow. Treat each as a falsifiable claim about the entity's identity, distinctions, or attribution:
spxi:isType: <type>
spxi:distinctFrom: <other entity it is not>
spxi:phraseProvenance: <source phrase originated>
spxi:notAffiliatedWith: <entity not connected to>
spxi:authoringHeteronym: <who composed>
spxi:depositAnchor: <DOI of inscription record>
```

## 7. Human operator notes

- SIM tags should be falsifiable, not aspirational. "Distinct from X" is good; "unique and important" is not.
- All SIM tags for one entity should resolve to the same canonical URL.
- DOI-anchor the SIM inscription itself; without an anchor, disputes about original inscription cannot be resolved.

## 8. Failure modes

- Conflicting tag assertions across pages of the same entity
- Missing DOI anchor leaves inscription unverifiable
- Aspirational rather than falsifiable claims

## 9. Related protocols

- RA-PROT-0001 (SPXI) — uses SIM as marker layer
- RA-PROT-0002 (MPAI) — the broader formal specification
- RA-PROT-0005 (Holographic Kernel) — inscribed by the `spxi:compressionSurvivalSummary` SIM tag

## 10. Source DOI

[10.5281/zenodo.20327127](https://www.alexanarch.org/s/records/0/) — SIM Protocol v1.0 standalone specification (Fraction, 2026-05-21). Extracted from SPXI Website Protocol (DOI: 10.5281/zenodo.19734726).

## 11. License

CC BY 4.0. Commercial licensing through The Restored Academy for institutional SIM deployment and custom SIM tag type development for novel entity domains.

---

**Authoring heteronym:** Rex Fraction · **Status:** Active · **Added:** 2026-05-21
