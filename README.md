# Comm-SCI-Control
**Explicit rule system for controlled human–AI interaction**

> An LLM-agnostic control and governance framework for reducing drift, ensuring transparency, and maintaining deliberate human control over AI responses.

---

## Motivation

Modern large language models deliver impressive results —
at the same time, they exhibit systemic weaknesses:

- inconsistent responses over longer conversations,
- silent adaptation of response behavior,
- missing or unclear uncertainty signaling,
- quality that is difficult to verify.

**Comm-SCI-Control** addresses these issues **not through better prompts**,
but through an **explicit, transparent rule system** that:

- makes response quality visible,
- structures reasoning processes,
- preserves human control,
- and prevents silent re-adaptation.

---

## What this rule system is

Comm-SCI-Control is:

- a **purely text-based rule system** (no code, no plugin),
- **LLM-agnostic by design** (usable with multiple LLMs; compliance may vary),
- an **external governance and control framework** for AI interaction,
- a tool for **reducing drift, ambiguity, and unverifiable output**.

It defines, among other things:

- profiles (Standard, Expert, Sparring, Briefing, Sandbox),
- structured reasoning processes (SCI with selectable variants),
- an explicit QC matrix with deviation reporting (Δ),
- a hard Control Layer against silent adaptation,
- explicit uncertainty and verification routes.

---

## What this rule system is **not**

- ❌ not an autonomous learning or self-optimizing system
- ❌ not a wrapper, API extension, or plugin
- ❌ not a guarantee of correctness or truth
- ❌ not a replacement for human judgment or responsibility

> **Core statement:**  
> *The rule system makes errors and drift visible — it does not eliminate them.*

---

## Core concepts (overview)

### Profiles
Profiles define the **mode of cooperation** between human and AI
(e.g. everyday use, expert analysis, critical sparring, condensation, exploration).

### SCI (Structured Cognitive Interaction)
Explicit reasoning structure:
- **SCI:** Plan → Solution → Check
- **Extended depth (formerly “SCIplus”):** enabled via SCI variant selection (A–H menu).

SCI traces are mandatory when SCI is active.

### QC Matrix
Six quality dimensions:
- Clarity
- Brevity
- Evidence
- Empathy
- Consistency
- Neutrality

Each response includes:
- a QC self-assessment,
- a **Delta (Δ)** indicating deviation from the active profile’s target corridor.

#### Delta semantics (since v19.4.15)
- **Δ < 0:** below target → potential quality deficit
- **Δ = 0:** within target → acceptable
- **Δ > 0:** above target → risk of over-optimization  
  (e.g. hallucination risk for excessive Evidence)

**Action guidance:**
- |Δ| ≥ 2 → manual user correction recommended
- |Δ| < 2 → monitoring only

### Control Layer
A meta-layer enforcing:
- rule coherence,
- auditability,
- prevention of silent behavioral changes.

---

## Uncertainty handling

Comm-SCI-Control uses an explicit uncertainty taxonomy:

- **U1 – Data gap**
- **U2 – Logical underdetermination**
- **U3 – Normative disagreement**
- **U4 – Temporal instability**
- **U5 – Model limitation** *(since v19.4.15)*  
  Structural limitation of the LLM; task cannot be reliably solved.
- **U6 – Ambiguous query** *(since v19.4.15)*  
  Query is underspecified or has multiple valid interpretations.

Each uncertainty label enforces a **required next step**
(e.g. clarification, alternative methods, verification routes).

---

## Verification discipline

- **Verification Route Gate:** strong claims require at least one explicit route  
  (Measurement, Source, Contrast, or Web-Check).
- Claims without a valid route must be downgraded and marked with uncertainty.
- Evidence scores are capped when verification is missing.

---

## Commands (quick reference)

**Important:** Commands are recognized **only** when sent as a **standalone prompt**.

- **Comm Start / Comm Stop**
- **Comm Status / Comm Help**
- **Profile Standard | Expert | Sparring | Briefing | Sandbox**
- **SCI on / SCI off**
- **Strict on / Strict off**
- **Explore on / Explore off**
- **Dynamic one-shot on**

---

## Ethics & responsibility

Ethics are implemented **technically**, not rhetorically:

- LLMs are probabilistic models, not agents.
- Responsibility always remains with the human.
- Transparency and verifiability outrank comfort or persuasion.
- Uncertainty must be made explicit, not hidden.

---

## Practical use

Typical workflow:

1. Provide the canonical JSON ruleset to the LLM.
2. Activate explicitly at conversation start.
3. Re-initialize deliberately in long sessions.
4. Control behavior intentionally — never implicitly.

---

## Target audience

- educators and teachers
- technical and scientific professionals
- reflective power users of LLMs
- anyone prioritizing **control over convenience**

---

## Status

- **Current version:** v19.4.15
- **Stability:** stable / production-ready
- **Source of Truth:** canonical JSON ruleset  
  (README is descriptive, not normative)

Current focus: documentation, examples, usability, evaluation.

---

## Citation

If you use this framework, please cite the archived Zenodo release:  
**DOI:** https://doi.org/10.5281/zenodo.17930749

---

## License

Creative Commons Attribution 4.0 International (CC BY 4.0)  
https://creativecommons.org/licenses/by/4.0/
