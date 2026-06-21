# Operator Kernel Specification v1.0

**RA-PROT-0017** · v1.0 · Category IV (Transformation & Operator) · Tier 1

The formal specification for the System of Recursive Magic (the Mandala): a structured kernel of operator-rules under which a human or AI executor can perform transformations on texts while preserving operator-chain accountability — the specification underlying the Crimson Hexagonal Archive's transformation protocols.

---

## 1. What it does

The Operator Kernel specifies the grammar by which operators perform transformations on texts under accountable, recursive, and composable rules. Each operator is named, signed, and its transformation behavior is specified. The Kernel binds the operator chain together — a sequence of transformations applied to a text is reconstructable from the operator log.

The Kernel is the basis for: the Liberatory Operator Set (LOS), the Mandala transformation suite, the Compression Arsenal's individual operators, the UKTP substrate-transform operators, and the Logotic Programming operator family.

## 2. When to use it

Deploy the Operator Kernel when:
- Constructing a transformation pipeline that requires accountable operator-chain reconstruction
- Composing operators into compound transformations where the order matters
- Teaching the operator-based approach to AI prompting and text transformation
- Building a new operator family that needs Kernel-level compatibility

## 3. Inputs

The text to be transformed; the desired transformation; the operators available; the operator-chain log target.

## 4. Procedure

1. Identify the transformation goal.
2. Select operators from the Kernel-compatible library (LOS, Mandala, UKTP, Logotic, Compression Arsenal).
3. Compose the operator chain: O_n(O_{n-1}(...O_1(text))). Order matters.
4. Sign the operator chain with the operating heteronym.
5. Execute the chain. Log each operator's transformation.
6. Deposit the operator chain log alongside the transformed output.

## 5. Outputs

The transformed text; the operator-chain log; deposit-anchored reconstruction record.

## 6. Pasteable LLM block

```
You are operating within the Operator Kernel framework. Each transformation you apply to the input text is a named operator with specified behavior. Log each operator applied, in order. The chain must be reconstructable: another operator running the same chain on the same input should produce the same output.

Operators available in this session: [list]
Operator chain target: [transformation goal]
```

## 7. Human operator notes

- The Kernel is *recursive*: operators can themselves invoke other operators. The Kernel specifies how recursion is logged.
- Operator names follow the convention: domain.family.operator (e.g., `logos.transform.compress_to_kernel`).
- The Mandala system of recursive magic is the canonical Kernel-compatible operator library; other libraries (LOS, UKTP) interoperate.

## 8. Failure modes

- Operator chain order errors → non-reconstructable transformation
- Unnamed operators → operator-chain log incomplete
- Missing deposit of log → transformation not accountable

## 9. Related protocols

- RA-PROT-0007 (UKTP) — substrate-transform operators that are Kernel-compatible
- RA-PROT-0006 (Space Ark) — runtime that hosts operator-chain execution
- RA-PROT-0023 (Liberatory Operator Set) — operator library compatible with the Kernel

## 10. Source DOI

[10.5281/zenodo.19288404](https://alexanarch.org/s/records/0/) — Operator Kernel Specification v1.0 - System of Recursive Magic: The Mandala (Sharks, 2026-03-28).

## 11. License

CC BY 4.0. Commercial licensing through The Restored Academy for organizational operator-library development, custom transformation-pipeline consulting, and operator-chain accountability training.

---

**Authoring heteronym:** Lee Sharks · **Status:** Active · **Added:** 2026-05-21
