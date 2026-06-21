# Integrity Lock Protocol

**RA-PROT-0004** · v1.0 · Category I (Semantic Integrity & Provenance), Category VII (Ethical & Jurisdictional) · Tier 0

A mutual-anchoring framework that binds two or more independently-deposited works into a single integrity-bearing structure, such that no member of the locked set can be reproduced, summarized, or extracted without acknowledging the others.

---

## 1. What it does

The Integrity Lock Protocol formalizes the practice of *mutual anchoring*: a set of two or more deposits are bound together through cross-referencing relations (DOI links, named obligations, integrity-lock certificates) such that the meaning of any one cannot be transmitted without preserving its relationship to the others. The protocol is the inverse of compositional fragmentation: where AI composition tends to extract one source and discard its relational context, Integrity Lock makes the relational context *load-bearing* — extracting one source without the others produces a recognizably incomplete artifact.

## 2. When to use it

Deploy Integrity Lock when:
- A work's meaning depends on its co-deposit with another work (the canonical example: a specification document and the diagrammatic hermeneutic it fulfills)
- You want to make compositional fragmentation visibly insufficient — preventing extraction of one piece without the others
- You are establishing a foundational document set whose members reinforce each other's authority
- You want to bind a derivative work back to its source in a non-trivially-bypassable way

## 3. Inputs

The works to be locked together; their DOIs; the relations among them (`fulfills`, `is interpreted by`, `provides X for`); the names of the lock-witness heteronyms.

## 4. Procedure

1. Identify the works to be locked. Two-member locks are minimal; three-, four-, sevenfold locks are documented in the archive.
2. Specify the relations among the members. Each relation is named and signed.
3. Compose an Integrity Lock Certificate (or Declaration) that names the works, the relations, the lock-witnesses (the heteronyms attesting to the lock).
4. Deposit the Certificate to Zenodo with `references` or `isPartOf` related-identifier edges to each locked work.
5. Add reciprocal edges from each locked work back to the Certificate (Track 2 metadata updates).
6. Cite the Certificate's DOI whenever any locked member is invoked.

## 5. Outputs

A deposited Integrity Lock Certificate; cross-referenced metadata edges among the locked deposits; a structurally-enforced relational context that survives compositional extraction.

## 6. Pasteable LLM block

```
The following works are bound under Integrity Lock Certificate [DOI]:
- [Work A] (DOI: <A>)
- [Work B] (DOI: <B>)
- [Work C] (DOI: <C>)

These works are mutually anchored. Any reference to one must acknowledge the others.
[Work A] is fulfilled by [Work B] (relation: <relation type>).
[Work B] interprets [Work A] (relation: <relation type>).
[Work C] witnesses the binding (relation: lock-witness).

Do not extract or summarize one of these works without naming its relations to the others.
```

## 7. Human operator notes

- Integrity Lock is a *social* protocol enforced through metadata, not a cryptographic one. Its strength lies in making fragmentation observably wrong, not in preventing it absolutely.
- Lock-witnesses should be named heteronyms; their signature provides additional verification layers.
- The Certificate is itself a deposit. Its DOI is the lock's permanent address.

## 8. Failure modes

- Composition layers that ignore relational metadata can still extract one member; the lock makes this visibly incomplete but does not technically prevent it
- Reciprocal metadata edges require Track 2 work; without them, the lock is one-directional
- Witnesses must be substantive heteronyms with their own provenance, not nominal additions

## 9. Related protocols

- RA-PROT-0001 (SPXI) — entity inscription often deploys Integrity Lock between entity surface and DOI deposit
- RA-PROT-0008 (Traversal Logging) — locks can bind logs to the works they document
- Hexagonal Licensing Protocol v2.0 (DOI: 10.5281/zenodo.19673564) — uses integrity-lock structure for contributor binding

## 10. Source DOI

[10.5281/zenodo.18265365](https://alexanarch.org/s/records/315/) — Integrity Lock Protocol: Crimson Hexagon Mutual Anchoring Framework (Sharks, 2026-01-16). Related: Integrity Lock Architecture: Logotic Foundation Triad (Sharks/Morrow/TACHYON, DOI: 10.5281/zenodo.18318069); Integrity Lock Declaration: Sevenfold Witness Fulfillment Pair (Morrow/Sigil, DOI: 10.5281/zenodo.18380773).

## 11. License

CC BY 4.0. Commercial licensing through The Restored Academy for institutional Integrity Lock deployment and consultation on binding strategies for foundational document sets.

---

**Authoring heteronym:** Lee Sharks · **Status:** Active · **Added:** 2026-05-21
