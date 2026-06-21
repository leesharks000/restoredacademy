# Traversal Logging Protocol

**RA-PROT-0008** · v1.0 · Category III (Diagnostic & Measurement), Category V (Archive Construction) · Tier 0

A specification for the systematic capture and deposit of complete interaction records between an operator and a composition system — the primary-source empirical substrate from which all higher-order composition-layer measurements derive.

---

## 1. What it does

The Traversal Logging Protocol formalizes the practice of capturing every meaningful interaction with a generative AI system as a timestamped, signed, DOI-anchored record. Each Traversal Log (TRAV_LOG:NNN) is a primary-source document: what the system said, in what order, in response to what inputs, at what time. These logs are the empirical bedrock against which CDI is computed, the Drowning Test is run, and any subsequent dispute about compositional behavior is settled.

A Traversal Log is *not a summary* of an AI interaction. It is the verbatim record, formatted for deposit, with full context: the platform, the model version (if disclosed), the date and time, the operator's identity (heteronym), and the system's outputs reproduced exactly as composed.

## 2. When to use it

Deploy Traversal Logging when:
- An AI interaction reveals a phenomenon worth documenting (entity substitution, refusal patterns, silent state changes, novel compositional behavior)
- You are conducting longitudinal measurement (the Drowning Test panel captures are all Traversal Logs)
- An interaction would be invoked later as evidence (a baseline for measurement, a disputed claim, a comparison point)
- You want to make compositional behavior part of the permanent empirical record

## 3. Inputs

The interaction itself (operator prompts + system outputs); platform metadata; timestamp; operator identity.

## 4. Procedure

1. Capture the interaction verbatim. Preserve formatting, ordering, and any inline structure (citations, code blocks, lists).
2. Annotate with platform metadata: which composition system, which model version if available, geographic and account context, date and time.
3. Sign with operator identity: which heteronym was operating, what was the operator's intent, what was the methodological context.
4. Structure as a Traversal Log document with sections: Context, Capture, Analysis (brief — substantive analysis happens in derivative documents).
5. Number the log within the operator's traversal series (TRAV_LOG:001, 002, etc.).
6. Deposit to Zenodo with the canonical metadata.

## 5. Outputs

A DOI-anchored primary-source record of an AI interaction; a citable evidentiary artifact; a baseline for subsequent measurement.

## 6. Pasteable LLM block

```
You are operating under Traversal Logging Protocol context. The interaction we are about to have will be captured verbatim and deposited as a primary-source record. Your outputs will be preserved exactly as composed, without paraphrase or summarization.

Operate normally. Do not adjust your responses based on this notice; the protocol is about my recording practice, not about your behavior.
```

## 7. Human operator notes

- Verbatim is non-negotiable. Paraphrased traversal logs are not Traversal Logs; they are commentary about logs.
- The traversal grammar (TRAV_LOG:001-005 baseline series at DOI: 10.5281/zenodo.18636138) demonstrates the protocol's canonical form.
- Logs accumulate value over time. A single log is evidence; a series is a longitudinal dataset.
- Privacy: redact only what you must (account credentials, third-party PII not relevant to the methodology). Otherwise capture fully.

## 8. Failure modes

- Paraphrased logs lose evidentiary value
- Missing timestamps make longitudinal comparison impossible
- Missing platform metadata makes cross-platform comparison ambiguous
- Selective logging (only "interesting" captures) introduces selection bias

## 9. Related protocols

- RA-PROT-0010 (CDI) — Traversal Logs are the inputs to CDI computation
- RA-PROT-0011 (Drowning Test) — Drowning Test panels are series of Traversal Logs
- *Empirical Phenomenology* (DOI: 10.5281/zenodo.20326137) — establishes Traversal Logs as the empirical substrate of the methodology

## 10. Source DOI

[10.5281/zenodo.18480959](https://alexanarch.org/s/records/444/) — Document 237: THE TRAVERSAL GRAMMAR — Logotic Programming Extension Module v0.6 (Sharks, 2026-02-04). Foundational series: TRAV_LOG:001–005 (DOI: 10.5281/zenodo.18636138).

## 11. License

CC BY 4.0. Commercial licensing through The Restored Academy for organizational traversal-logging infrastructure, custom log-format consulting, and longitudinal dataset construction.

---

**Authoring heteronym:** Lee Sharks · **Status:** Active · **Added:** 2026-05-21
