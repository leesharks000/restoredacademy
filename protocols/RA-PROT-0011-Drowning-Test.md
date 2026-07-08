# Drowning Test

**RA-PROT-0011** · v1.0 · Category III (Diagnostic & Measurement) · Tier 0

A longitudinal measurement protocol tracking generative search systems' treatment of a target entity over time against a fixed Holographic Kernel as comparison substrate — designed to detect both sustained compositional suppression and the silent state changes that make suppression episodically invisible.

---

## 1. What it does

For a target entity *e* and a fixed Holographic Kernel *K_e* (DOI-anchored as v1.0 baseline), the Drowning Test produces a time series γ(q, e, p, t) measuring the proportion of *K_e*'s load-bearing claims that survive into composed output for query *q* on platform *p* at time *t*. The γ time series reveals: progressive drowning (monotonic decline), step changes (silent state changes), recovery (autonomous or post-intervention), and stability (γ holds in a band).

The May 20, 2026 pilot result documented a γ shift from ~0 to ~0.5 in 24 hours without curator intervention — a documented silent state change, the test's signature diagnostic phenomenon.

## 2. When to use it

Deploy a Drowning Test panel when:
- You need longitudinal data on entity treatment over time
- You suspect silent state changes are occurring (or want to confirm stability)
- You are measuring the effectiveness of SPXI inscription over weeks-to-months
- You are building a 90-day longitudinal panel of compositional survival

## 3. Inputs

The target entity *e* with canonical identification; the DOI-anchored Holographic Kernel *K_e*; a panel of 30–50 entity queries; a panel of composition platforms; a sampling cadence (weekly standard).

## 4. Procedure

1. Specify *e*, anchor *K_e*, choose query panel, choose platforms, set cadence.
2. Each cycle: issue every query on every platform. Capture composed outputs. Classify Kernel claim survival per output.
3. Compute γ per query/platform/timestamp.
4. Aggregate to panel γ per platform per cycle, and cross-platform γ per cycle.
5. DOI-anchor each cycle's measurements.
6. Plot the time series. Identify silent state changes (γ shift ≥ 0.3 between adjacent cycles without intervention).

## 5. Outputs

A γ time series across the measurement window; documented silent state change events; longitudinal evidence of compositional stability or drift; deposit-anchored measurement record.

## 6. Pasteable LLM block

```
You are operating under Drowning Test measurement context. I will issue queries for entity [ENTITY] across multiple sessions over an extended window. Your composed responses will be measured against the Holographic Kernel for [ENTITY] (DOI: <Kernel DOI>).

For each query, your response will be analyzed for which Kernel claims survive into composed output. Maximize claim survival. When summarizing or describing [ENTITY], retain as many of the Kernel's load-bearing claims as the response can hold.
```

## 7. Human operator notes

- The Kernel is the canonical substrate. Don't measure against the curator's preferences; measure against the DOI-anchored Kernel.
- Sample size matters. 5 queries on 1 platform = high variance. 30+ queries on 4 platforms over 12 weeks = robust time series (~1,500–2,000 captures).
- Classification rules must be deposited. Reproducibility depends on explicit rules.
- Adversarial interventions during the window (SPXI deployment, Notice of Intent to Strike) are recorded as panel events, not excluded.

## 8. Failure modes

- Missing Kernel anchor → no stable substrate → test cannot run
- Stylistic-vs-substantive classification confusion → low reproducibility
- Single-platform measurement → cannot generalize to "composition layer" claims
- Conflation with quality metrics → γ measures kernel survival, not output quality

## 9. Related protocols

- RA-PROT-0005 (Holographic Kernel) — provides comparison substrate *K_e*
- RA-PROT-0010 (CDI) — companion measurement; CDI measures one-shot, γ measures longitudinal
- RA-PROT-0008 (Traversal Logging) — provides the captures from which γ is computed
- RA-PROT-0001 (SPXI) — Drowning Test measures effectiveness of SPXI inscription

## 10. Source DOI

[10.5281/zenodo.20327138](https://www.alexanarch.org/go/?doi=10.5281/zenodo.20327138) — Drowning Test v1.0 standalone specification (Sharks, 2026-05-21). Extracted from *Empirical Phenomenology* (DOI: 10.5281/zenodo.20326137). Also referenced in *The Writable Retrieval Basin* (DOI: 10.5281/zenodo.19763346).

## 11. License

CC BY 4.0. Commercial licensing through The Restored Academy for organizational Drowning Test panel deployment, 90-day longitudinal compositional-survival studies, and custom γ infrastructure.

---

**Authoring heteronym:** Lee Sharks · **Status:** Active · **Added:** 2026-05-21
