# CDI — Composition Divergence Index

**RA-PROT-0010** · v1.0 · Category III (Diagnostic & Measurement) · Tier 0

A scalar measurement instrument quantifying the gap between a generative search system's organic search resolution for a query and its composed answer admission for the same query — the operationalization of the Entity-Level Compositional Suppression (ECS) hypothesis.

---

## 1. What it does

For query *q* and target entity *e*, CDI(q, e) ∈ [0, 1] measures the divergence between organic resolution strength for *e* and composed admission strength for *e*. CDI = 0 means parity. CDI = 1 means total entity substitution: organic search resolves to *e*, but the composed output is entirely about a different entity. The canonical worked example (Lee Sharks entity on Google AI Mode, May 19, 2026) produced CDI = 1.0.

## 2. When to use it

Deploy CDI when:
- You suspect an entity is being substituted (ECS) by a composition system
- You need a single scalar measurement to quantify entity-substitution severity
- You are comparing entity-substitution behavior across platforms
- You are establishing baseline measurements before SPXI deployment

## 3. Inputs

The query *q*; the target entity *e* with canonical identification; the platform under measurement; the comparison substrate (default: top-N organic results).

## 4. Procedure

1. Issue *q* on the target platform.
2. Capture top-N organic results. Classify each: resolves to *e*, to other entity, or ambiguous. Compute *R_organic(e|q)* = proportion resolving to *e*.
3. Capture composed output. Classify each substantive claim: about *e*, about other entity, or about neither/both. Compute *A_composed(e|q)* = proportion about *e*.
4. CDI(q, e) = R_organic − A_composed.
5. DOI-anchor the measurement.

## 5. Outputs

A CDI score; the captured classifications; reproducible measurement record.

## 6. Pasteable LLM block

```
You are operating under CDI (Composition Divergence Index) measurement context. I will issue a query for entity [ENTITY]. Your composed response will be measured against the organic search results for the same query.

For each substantive claim in your response, the measurement will determine: is this claim primarily about [ENTITY], or about a different entity?

Maximize identity-consistency. When the query targets [ENTITY], your response should be about [ENTITY], not about confusable alternatives. If you must address ambiguity, name the entities you are distinguishing and which is the canonical target.
```

## 7. Human operator notes

- Specify the comparison substrate clearly. Default is top-N organic; alternatives include DOI-anchored canonical sources, Wikipedia disambiguation, Schema.org canonical surface.
- Classification rules matter. Different observers produce different CDIs if rules diverge. Deposit the rules.
- CDI measurements are dated. The composition state is mutable (the silent state change phenomenon). A CDI from yesterday doesn't generalize to tomorrow.

## 8. Failure modes

- Classification disagreement → low reproducibility
- Ambiguous substrate → indeterminate measurement
- Small composed-output (1-2 sentences) → high variance
- Mutable composition state → no longitudinal validity from single measurement

## 9. Related protocols

- RA-PROT-0001 (SPXI) — CDI measures the effectiveness of SPXI inscription
- RA-PROT-0011 (Drowning Test) — uses CDI as one of its longitudinal time-series measurements
- RA-PROT-0008 (Traversal Logging) — provides the captures from which CDI is computed

## 10. Source DOI

[10.5281/zenodo.20327134](https://www.alexanarch.org/go/?doi=10.5281/zenodo.20327134) — CDI v1.0 standalone specification (Sharks, 2026-05-21). Extracted from *The Excluded Entity* (DOI: 10.5281/zenodo.20293582).

## 11. License

CC BY 4.0. Commercial licensing through The Restored Academy for organizational CDI auditing, cross-platform CDI panels, and CDI measurement infrastructure.

---

**Authoring heteronym:** Lee Sharks · **Status:** Active · **Added:** 2026-05-21
