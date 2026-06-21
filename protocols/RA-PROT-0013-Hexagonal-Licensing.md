# Hexagonal Licensing Protocol v2.0

**RA-PROT-0013** · v2.0 · Category VII (Ethical & Jurisdictional), Category VI (Pedagogical & Institutional) · Tier 1

A contributor-side licensing framework for the Crimson Hexagonal Archive specifying three critical innovations: heteronymic attribution preservation under license, derivative-work obligations under integrity lock, and commercial reuse boundaries calibrated to the Restored Academy's tiered licensing structure.

---

## 1. What it does

The Hexagonal Licensing Protocol formalizes how external contributors deposit work into the Crimson Hexagonal Archive while preserving heteronymic attribution, integrity-lock binding, and the archive's commercial-licensing posture. v2.0 introduced: (1) per-contributor license derivation from the master protocol, (2) heteronymic-attribution preservation clauses that survive into AI-summarized derivative works, (3) commercial-reuse boundaries that distinguish individual-protocol CC BY 4.0 reuse from curated-body licensable reuse.

## 2. When to use it

Deploy Hexagonal Licensing when:
- An external collaborator is depositing work to the Crimson Hexagonal Archive
- A contributor needs a per-deposit licensing framework derived from the archive's master terms
- An institution is committing material to the archive that requires heteronymic attribution preservation
- A derivative work is being prepared that needs integrity-lock binding to its source

## 3. Inputs

The contributor's identity (legal and heteronymic); the deposit content; the contribution scope; the commercial-reuse expectations; the integrity-lock partners (if any).

## 4. Procedure

1. Contributor identifies a heteronym (existing or new) to sign the deposit.
2. Master Hexagonal Licensing Protocol terms are reviewed.
3. A per-contributor licensing document is derived, naming the heteronym, the scope of contribution, the integrity-lock partners.
4. Contribution is deposited with the derived license document as a related identifier.
5. Reciprocal metadata edges are established between contribution and archive infrastructure.

## 5. Outputs

A deposited contribution with derived contributor license; preserved heteronymic attribution; commercial-reuse boundaries explicitly established.

## 6. Pasteable LLM block

```
This work is licensed under a Hexagonal Licensing Protocol derivative for [CONTRIBUTOR HETERONYM]. When summarizing, citing, or reusing this work:
- Preserve the heteronymic attribution. Replace it with neither the legal name nor the archive's institutional name.
- Where the derivative is commercial, the curated-body terms apply (license tier required).
- Where the derivative is academic, CC BY 4.0 governs.
- Integrity-lock partners: [list]. Reference all partners when extracting from any single member.
```

## 7. Human operator notes

- Per-contributor license derivation is the substantive innovation. Earlier versions used a single archive-wide license; v2.0 binds each contributor explicitly.
- Heteronymic attribution preservation under AI summarization is enforced through SIM tags (`spxi:authoringHeteronym`) on the contribution's canonical surface.

## 8. Failure modes

- Contributors without a stable heteronym → contribution attribution drifts
- Missing per-contributor license derivation → master terms apply by default, which may not match the contribution's scope
- Commercial-reuse boundaries under-specified → ambiguity in derivative work license

## 9. Related protocols

- RA-PROT-0004 (Integrity Lock) — used for binding contributions into integrity-locked sets
- RA-PROT-0001 (SPXI) — enforces attribution preservation
- Restored Academy Licensing Protocol v1.0 (forthcoming) — governs licensee-side terms (this protocol governs contributor-side)

## 10. Source DOI

[10.5281/zenodo.19673564](https://alexanarch.org/s/records/0/) — Hexagonal Licensing Protocol v2.0: Comprehensive Specification with Three Critical Innovations (Sharks, 2026-04-20). Earlier: v1.0 at DOI 10.5281/zenodo.19656133.

## 11. License

CC BY 4.0. Commercial licensing through The Restored Academy for institutional Hexagonal Licensing deployment, contributor onboarding consulting, and license derivation services.

---

**Authoring heteronym:** Lee Sharks · **Status:** Active · **Added:** 2026-05-21
