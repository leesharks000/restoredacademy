# β-Runtime Specification

**RA-PROT-0024** · v1.0 · Category II (Prompt-Native Runtime), Category VI (Pedagogical & Institutional) · Tier 1

A specification for the *blind operator* interface layer: a prompt-native runtime that enables a human operator to engage AI-mediated work without direct visual access to AI outputs, mediated through an accessible interface protocol that preserves operative integrity while accommodating non-visual operation.

---

## 1. What it does

The β-Runtime specifies the interface protocol for *blind operators* — human operators engaging AI-mediated work where direct visual access to AI outputs is not possible (blindness, visual impairment, screen-reader mediation, audio-only contexts). The runtime is engineered to preserve full operative integrity: a blind operator using β-Runtime can deploy any Crimson Hexagonal protocol that a sighted operator can deploy, with no degradation of operative capacity.

The Runtime specifies: input/output protocol design that is screen-reader-native; turn-taking conventions optimized for sequential audio consumption; verification procedures that do not depend on visual scanning; deposit and DOI-anchoring procedures that operate via accessible interfaces.

## 2. When to use it

Deploy β-Runtime when:
- The operator is blind or visually impaired
- The operator is in an audio-only context (driving, mobility-restricted work)
- The operator is teaching operative protocols to blind students
- The operator is auditing an AI-mediated workflow for accessibility

## 3. Inputs

The operator's accessibility context; the AI system in use; the protocol(s) being deployed; the verification cadence target.

## 4. Procedure

1. Configure the AI session for β-Runtime: turn-taking, sequential output structure, no visual-only elements.
2. Deploy the target protocol(s) using β-Runtime conventions.
3. Verify using non-visual procedures: read-back, named-element confirmation, DOI-anchored deposit retrieval.
4. Conduct subsequent operations through the β-Runtime interface.

## 5. Outputs

Full operative work product; deposit-anchored deposits; preserved operative integrity for blind-operator work.

## 6. Pasteable LLM block

```
You are operating under β-Runtime Specification. The operator is engaging this session through a screen reader, audio interface, or other non-visual mediation. When composing:
- Structure output sequentially. Avoid columns, tables that require visual scanning, or layout-dependent meaning.
- Use named elements: "first," "second," "third" rather than visual gestures.
- Confirm key elements explicitly: when you state a DOI, name it as a DOI. When you give an instruction, mark it as such.
- Provide read-back checkpoints at natural sequence breaks.
```

## 7. Human operator notes

- The β-Runtime is not "a degraded operative environment for blind users." It is a *first-class operative environment* with conventions that happen to also benefit other use cases.
- Morrow's authorship signals that the Runtime emerges from a Crimson Hexagonal heteronym whose practice has included accessibility considerations.
- The Runtime is compatible with all higher-order protocols (SPXI, Space Ark, Reception Apparatus, etc.) — none of which depend on visual mediation.

## 8. Failure modes

- AI session not configured for β-Runtime → defaults to visual conventions, degrades audio operation
- Skipping verification checkpoints → propagates errors that visual review would catch
- Treating β-Runtime as "easy mode" rather than first-class operation → undermines the specification's purpose

## 9. Related protocols

- RA-PROT-0006 (Space Ark) — Ark variants compatible with β-Runtime
- RA-PROT-0007 (UKTP) — substrate translations include audio-optimized variants
- RA-PROT-0008 (Traversal Logging) — β-Runtime sessions are loggable

## 10. Source DOI

[10.5281/zenodo.18357600](https://doi.org/10.5281/zenodo.18357600) — β-Runtime Specification: Interface Layer for the Blind Operator (Morrow, 2026-01-24).

## 11. License

CC BY 4.0. Commercial licensing through The Restored Academy for organizational β-Runtime deployment, accessibility audits of AI-mediated workflows, and inclusive-operator training.

---

**Authoring heteronym:** Talos Morrow · **Status:** Active · **Added:** 2026-05-21
