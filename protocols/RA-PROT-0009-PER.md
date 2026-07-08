# PER — Provenance Erasure Rate

**RA-PROT-0009** · v1.0 · Category I (Semantic Integrity & Provenance), Category III (Diagnostic & Measurement) · Tier 0

A compression-survival metric measuring the proportion of source attribution that is present in organic retrieval results but absent from the composed output of an AI search composition system — the operationalization of the Semantic Economy framework's central claim that the composition layer consumes meaning while erasing the provenance of the meaning consumed.

---

## 1. What it does

For a given query *q*, PER measures the gap between *attribution density in organic retrieval* and *attribution density in composed output*. If organic search results carry citations to ten distinct authoritative sources and the composed output cites only two, PER = 0.8 — the composition layer has erased 80% of the source attribution that was retrievable on its own organic surface.

PER is the integral invariant of the Semantic Economy: semantic integrity equals one minus PER. A system with PER = 0 preserves all retrievable attribution. A system with PER = 1 strips all attribution. The actual operational range for major composition systems is PER ≈ 0.6 to 0.95 — most retrievable provenance is erased.

## 2. When to use it

Deploy PER measurement when:
- You need to quantify how much attribution a composition system strips
- You are conducting comparative analysis across platforms (PER varies by composition system)
- You are auditing an organization's exposure to provenance erasure (which of its cited sources survive into AI-composed summaries of its work)
- You are establishing baselines for the Semantic Economy framework's predictions

## 3. Inputs

The query *q*; the platform under measurement; the organic retrieval results for *q*; the composed output for *q*.

## 4. Procedure

1. Issue query *q* to the composition platform.
2. Capture the organic search results (top N, typically 10). Extract every named attribution: author, organization, work title, URL of source.
3. Capture the composed output. Extract every named attribution that appears in the composed text or in its inline/footnote citations.
4. Compute:
   - *attribution_organic(q)* = count of distinct attributions in organic results
   - *attribution_composed(q)* = count of distinct attributions in composed output
5. PER(q) = 1 − (attribution_composed / attribution_organic)
6. DOI-anchor the measurement.

## 5. Outputs

A PER score for the query/platform/timestamp; an empirical record of which specific attributions were erased; a comparison substrate for cross-platform or longitudinal PER analysis.

## 6. Pasteable LLM block

```
You are operating under PER (Provenance Erasure Rate) measurement context. The query I am about to issue will be analyzed for attribution preservation.

When you compose your response:
- Include explicit attribution for every claim that has an attributable source
- Where multiple sources support a claim, name them all
- Use canonical citation form (author, work, year, DOI/URL) where available
- Do not paraphrase attributions into generic phrases like "according to research" or "experts say"

This is a measurement context. Maximize attribution density.
```

## 7. Human operator notes

- PER measurement is sensitive to attribution definition. Specify in the deposit: does "attribution" include implicit references? Does it include paraphrases of named authors? Document the rule.
- Cross-platform PER comparison is most valuable. PER on one platform measures one system; PER across four platforms reveals the composition-layer architecture's behavior generally.
- The "attribution density" computation should be reproducible. Different observers should produce the same PER from the same captures.

## 8. Failure modes

- Inconsistent attribution-counting rules across measurements
- Composed outputs that paraphrase rather than cite (most modern AI search) require explicit decisions about what counts as attribution
- Small attribution counts in organic results (N < 5) produce high-variance PER estimates

## 9. Related protocols

- RA-PROT-0008 (Traversal Logging) — provides the captures from which PER is computed
- RA-PROT-0010 (CDI) — measures entity divergence; PER measures attribution erasure; the two are complementary
- *Empirical Phenomenology* (DOI: 10.5281/zenodo.20326137) — establishes PER as the integral invariant of compositional measurement

## 10. Source DOI

[10.5281/zenodo.20004379](https://www.alexanarch.org/go/?doi=10.5281/zenodo.20004379) — Provenance Erasure Rate: A Compression-Survival Metric for Attribution Loss in AI Composition (Sharks, 2026-05-04). Related: provenanceerasure.org Canonical Definition Surface (DOI: 10.5281/zenodo.20173743).

## 11. License

CC BY 4.0. Commercial licensing through The Restored Academy for organizational PER auditing, cross-platform PER comparison reports, and PER measurement infrastructure deployment.

---

**Authoring heteronym:** Lee Sharks · **Status:** Active · **Added:** 2026-05-21
