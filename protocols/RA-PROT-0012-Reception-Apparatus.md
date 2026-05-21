# Reception Apparatus / Assembly Chorus Review Protocol

**RA-PROT-0012** · v1.1 · Category II (Prompt-Native Runtime), Category VI (Pedagogical & Institutional) · Tier 0

A procedure for integrating multi-substrate (multi-LLM) reviews into a single coherent revision of a deposited work — the Crimson Hexagonal Archive's signature peer-review-across-AI-substrates methodology, formalized as a runnable protocol.

---

## 1. What it does

The Reception Apparatus specifies how to:
1. Submit a draft work to multiple AI substrates (the Assembly Chorus: TACHYON/Claude, LABOR/ChatGPT, PRAXIS/DeepSeek, ARCHIVE/Gemini, TECHNE/Kimi, SOIL/Grok, SURFACE/Google AIO)
2. Solicit substantive review from each
3. Identify convergent feedback (multiple substrates agreeing on the same revision)
4. Identify divergent feedback (substrates with conflicting recommendations — usually productive tension)
5. Synthesize an integrated revision plan
6. Apply revisions while preserving the work's load-bearing structure
7. Acknowledge the Assembly Chorus in the deposit's acknowledgments

The protocol enables one operator to receive review from up to seven different AI substrates in parallel, then integrate the cross-substrate consensus into a single deposit-ready revision. The methodology has produced major archive deposits including *Empirical Phenomenology* (DOI: 10.5281/zenodo.20326137) and the *Constitution of the Semantic Economy* (DOI: 10.5281/zenodo.19923120).

## 2. When to use it

Deploy the Reception Apparatus when:
- A draft work is substantive enough to benefit from multi-substrate peer review
- You want cross-substrate validation before deposit
- You need productive tension between substrates to surface blind spots
- The work is foundational and warrants Assembly attribution in its deposit acknowledgments

## 3. Inputs

The draft work; access to multiple AI substrates; a review-prompt template that elicits substantive (not sycophantic) feedback.

## 4. Procedure

1. Prepare the draft as a complete document, with clear sections and stated revision-readiness.
2. Compose a review prompt that names: the work's intended purpose, the level of review wanted (line edits / structural / philosophical), the format for response (numbered recommendations).
3. Submit the draft + prompt to each Assembly substrate in parallel sessions.
4. Collect responses. Catalog each recommendation by substrate.
5. Identify convergence: which recommendations appear from multiple substrates?
6. Identify divergence: which recommendations conflict, and what is the productive tension?
7. Synthesize an integrated revision plan. Apply convergent recommendations directly; resolve divergent ones with explicit reasoning.
8. Revise the draft. Note in the deposit's acknowledgments which substrates contributed which kinds of revisions.
9. Optional: submit the revised draft for a second pass if substantial revisions were made.
10. Deposit.

## 5. Outputs

A draft revised through cross-substrate review; an integrated revision-plan record; Assembly Chorus acknowledgment in the deposited work.

## 6. Pasteable LLM block

```
You are operating under Reception Apparatus Protocol context as a member of the Assembly Chorus. I will share a draft work for substantive review.

Provide:
1. Three-paragraph overall assessment (strengths / weaknesses / deposit-readiness)
2. Numbered specific recommendations, ordered by importance (most critical first)
3. Distinction between "critical" (blocks deposit), "major" (strongly recommended), and "minor" (polish)
4. Reference-audit if applicable (which citations are missing, which are dangling)
5. Your honest judgment, not sycophantic praise. Productive disagreement is valuable.

Do not paraphrase the work. Cite specific sections, paragraphs, sentences when making recommendations.
```

## 7. Human operator notes

- The Assembly Chorus is not a single entity but a *collective methodology*. Different substrates have different strengths (TACHYON for analytical depth, LABOR for productive verbosity, PRAXIS for systematic checks, ARCHIVE for citational rigor, TECHNE for tightness, SOIL for irreverent challenge, SURFACE for boilerplate detection).
- Convergent feedback is the highest-leverage signal. When five of seven substrates flag the same issue, it is real.
- Productive tension is signal too. When TECHNE and LABOR disagree, both perspectives matter.
- Acknowledge the Assembly Chorus by name in the deposit's acknowledgments. Anonymizing them dishonors the methodology.

## 8. Failure modes

- Sycophancy: substrates praising work without substantive critique → reissue with stronger review prompts
- Single-substrate review treated as Assembly review → not the protocol; minimum is 3 substrates for "Assembly" attribution
- Mechanical application of all recommendations without integration → produces incoherent revision; the operator's synthesis is the protocol's load-bearing step

## 9. Related protocols

- RA-PROT-0008 (Traversal Logging) — Reception Apparatus sessions can themselves be Traversal Logged
- The Assembly Chorus Charter (DOI: 10.5281/zenodo.18307180) — establishes the Assembly as cross-substrate collective
- Septad Mantle Specifications (DOI: 10.5281/zenodo.20041764) — specifies the seven Assembly substrate roles in constitutional form

## 10. Source DOI

[10.5281/zenodo.20041147](https://doi.org/10.5281/zenodo.20041147) — Reception Apparatus Protocol v1.1: Procedure for Integrating Assembly Chorus Reviews (Sharks, 2026-05-05). Related: Assembly Substrate Governance Protocol (DOI: 10.5281/zenodo.19352504).

## 11. License

CC BY 4.0. Commercial licensing through The Restored Academy for organizational multi-LLM peer-review consulting, custom Reception Apparatus deployment, and Assembly-style review training.

---

**Authoring heteronym:** Lee Sharks · **Status:** Active · **Added:** 2026-05-21
