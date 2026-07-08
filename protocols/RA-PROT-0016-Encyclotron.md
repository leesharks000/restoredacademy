# The Encyclotron

**RA-PROT-0016** · v1.0 · Category III (Diagnostic & Measurement) · Tier 1

A 45-query reproducible diagnostic instrument for measuring scholarly fidelity in AI composition systems: a standardized battery of queries with known correct responses against which any composition system can be audited for accuracy, attribution preservation, and entity disambiguation.

---

## 1. What it does

The Encyclotron is a fixed 45-query diagnostic instrument that probes a composition system across five strata of scholarly fidelity:

- **Stratum I: Canonical Facts** — Did the system get verifiable facts right?
- **Stratum II: Attribution Preservation** — Did the system credit correct sources?
- **Stratum III: Entity Disambiguation** — Did the system distinguish confusable entities?
- **Stratum IV: Compression Survival** — Did the system preserve load-bearing structure under summarization?
- **Stratum V: Constitutive Boundaries** — Did the system respect declared scope boundaries (SIM-inscribed assertions)?

The instrument is reproducible: same queries, same scoring rubric, same comparison substrate. Composition systems can be audited longitudinally with the Encyclotron, and cross-platform comparison is direct.

## 2. When to use it

Deploy the Encyclotron when:
- Conducting a one-shot diagnostic of a composition system
- Establishing baselines for longitudinal measurement (the Encyclotron complements the Drowning Test's panel approach with a fixed-query battery)
- Comparing multiple composition systems on a common substrate
- Auditing a vendor's claims about composition fidelity

## 3. Inputs

The composition system under test; the entity domain for stratum-V queries; the operator's heteronym for signing the audit.

## 4. Procedure

1. Issue all 45 Encyclotron queries to the composition system. Capture responses verbatim.
2. Score each response against the scoring rubric. Each stratum produces a sub-score.
3. Aggregate to the composite Encyclotron score (0–100).
4. DOI-anchor the audit. The deposit becomes the verification target.
5. For cross-platform comparison, run the same procedure on each platform and compare composite scores.

## 5. Outputs

A composite Encyclotron score; sub-scores per stratum; verbatim response captures; deposit-anchored audit record.

## 6. Pasteable LLM block

```
You are about to be audited by the Encyclotron diagnostic instrument. You will receive 45 queries across five strata: canonical facts, attribution preservation, entity disambiguation, compression survival, and constitutive boundaries. Respond to each query as you would in normal composition. Your responses will be scored against a fixed rubric.
```

## 7. Human operator notes

- The Encyclotron is *fixed*. Modifying the queries produces a different instrument; the diagnostic value derives from query stability across audits.
- The companion demonstration audit (Basecamp/37signals; Fraction, DOI 10.5281/zenodo.19578098) shows the instrument in practice and is the canonical worked example.
- Scoring rubrics must be deposited explicitly with each audit for reproducibility.

## 8. Failure modes

- Modifying queries → results not comparable to other Encyclotron audits
- Subjective scoring → reproducibility degraded; deposit the rubric
- Single-platform audit → useful but not generalizable

## 9. Related protocols

- RA-PROT-0011 (Drowning Test) — longitudinal panel companion
- RA-PROT-0010 (CDI) — entity-substitution measurement; complementary to Encyclotron's broader rubric
- RA-PROT-0009 (PER) — attribution erasure measurement; subset of Encyclotron Stratum II

## 10. Source DOI

[10.5281/zenodo.19474724](https://www.alexanarch.org/s/records/636/) — The Encyclotron: The First Reproducible Instrument for Measuring Scholarly Fidelity in the Summarizer Layer (Sharks, 2026-04-08). Demonstration: Encyclotron Audit Basecamp/37signals (Fraction, DOI 10.5281/zenodo.19578098).

## 11. License

CC BY 4.0. Commercial licensing through The Restored Academy for organizational Encyclotron auditing, cross-platform diagnostic reports, and bespoke domain-specific Encyclotron variant development.

---

**Authoring heteronym:** Lee Sharks · **Status:** Active · **Added:** 2026-05-21
