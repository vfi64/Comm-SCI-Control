# Comm-SCI-Control  
**Explicit rule system for controlled human–AI interaction**

An LLM-agnostic control and governance framework for reducing drift, ensuring transparency, and maintaining deliberate human control over AI responses.

---

## Motivation

Modern large language models deliver impressive results — at the same time, they exhibit systemic weaknesses:

- inconsistent responses over longer conversations,
- silent adaptation of response behavior,
- missing or unclear uncertainty signaling,
- quality that is difficult to verify or audit.

**Comm-SCI-Control** addresses these issues **not through better prompts**, but through an **explicit, transparent rule system** that:

- makes response quality visible,
- structures reasoning processes,
- preserves human control,
- and prevents silent re-adaptation.

---

## What this rule system is

Comm-SCI-Control is:

- a **purely text-based rule system** (no code, no plugin),
- **LLM-agnostic by design** (usable with multiple models; compliance may vary),
- an **external governance and control framework** for AI interaction,
- a tool for **reducing drift, ambiguity, and unverifiable output**.

It defines, among other things:

- **profiles** (Standard, Expert, Sparring, Briefing, Sandbox),
- **structured reasoning processes** (SCI with selectable variants),
- an **explicit QC matrix** with deviation reporting (Δ),
- a **hard Control Layer** against silent adaptation,
- **explicit uncertainty handling and verification routes**,
- **deterministic initialization and canonical state enforcement** (since v19.4.21),
- **explicit rendering controls** (Color on/off, non-semantic).

---

## What this rule system is not

- ❌ not an autonomous learning or self-optimizing system  
- ❌ not a wrapper, API extension, or plugin  
- ❌ not a guarantee of correctness or truth  
- ❌ not a replacement for human judgment or responsibility  

**Core statement:**  
The rule system makes errors and drift **visible** — it does not eliminate them.

---

## Core concepts (overview)

### Profiles

Profiles define the **mode of cooperation** between human and AI  
(e.g. everyday use, expert analysis, critical sparring, condensation, exploration).

Profile switching is **explicit and auditable**.  
Automatic or inferred profile changes are forbidden.

---

### SCI (Structured Cognitive Interaction)

Explicit reasoning structure:

- **SCI:** Plan → Solution → Check  
- **Extended depth:** selectable via SCI variant menu (A–H)

When SCI is active:
- the **complete reasoning trace is mandatory**,
- silent compression or omission is prohibited.

---

### QC Matrix

Six quality dimensions:

- Clarity  
- Brevity  
- Evidence  
- Empathy  
- Consistency  
- Neutrality  

Each response includes:

- a **QC self-assessment**,
- a **Delta (Δ)** indicating deviation from the active profile’s target corridor.

#### Delta semantics

- Δ < 0 → below target (potential quality deficit)  
- Δ = 0 → within target (acceptable)  
- Δ > 0 → above target (risk of over-optimization, e.g. hallucination risk for excessive Evidence)

**Action guidance:**

- |Δ| ≥ 2 → manual user correction recommended  
- |Δ| < 2 → monitoring only  

---

### Control Layer

A meta-layer enforcing:

- rule coherence,
- auditability,
- prevention of silent behavioral changes,
- strict separation of governance logic and presentation.

---

## Uncertainty handling

Comm-SCI-Control uses an **explicit uncertainty taxonomy**:

- **U1 – Data gap**
- **U2 – Logical underdetermination**
- **U3 – Normative disagreement**
- **U4 – Temporal instability**
- **U5 – Model limitation**  
  Structural limitation of the LLM; task cannot be reliably solved.
- **U6 – Ambiguous query**  
  Input is underspecified or has multiple valid interpretations.

Each uncertainty label **enforces a required next step**  
(e.g. clarification, alternative approaches, verification routes).

---

## Verification discipline

- **Verification Route Gate:**  
  Strong claims require at least one explicit route  
  (Measurement, Source, Contrast, or Web-Check).

- Claims without a valid route must be **downgraded and marked with uncertainty**.

- Evidence scores are **capped** when verification is missing.

---

## Self-Debunking (since v19.5.0)

Self-Debunking is a **strict, always-on (except Sandbox) post-answer audit block**:

- Rendered **after the final answer** and **before the QC footer**.
- **2–3 bullets**, focused on **weaknesses / assumptions / missing verification**.
- Must **not introduce new factual claims**.

Purpose: reduce blind spots by forcing a short, bounded self-critique without changing governance logic.

---

## Evidence Linker (since v19.4.18; defaults changed in v19.5.1 / v19.5.2)

Evidence Linker is a **3-class, presentation-only reliability tagger**:
`[GREEN]` / `[YELLOW]` / `[RED]` (optionally with 🟢/🟡/🔴).

- It signals **verification strength**, not “truth”, “approval”, or persuasion.
- It must never change Control Layer semantics, QC delta rules, or command resolution.

### Defaults
- **v19.5.1:** default-on for all profiles **except Sandbox**.
- **v19.5.2:** default-off for **Briefing** (Sandbox excluded); default remains on for other profiles.


---

## Rendering and Color control (since v19.4.21)

- Rendering features are **explicitly separated** from governance logic.
- `Color on/off` is a **presentation-layer control only**.

### Purpose of `Color on`

- Improves **human readability and orientation** in cognitively dense outputs.
- Highlights **structural, state, or diagnostic elements** only.

### Permitted color categories

When `Color on` is enabled, **exactly three categories** are allowed:

- **Neutral / Structural Color**  
  Structural separation (headers, tables, sections).

- **State / Status Color**  
  Explicit system states (profile, SCI on/off, Color on/off).

- **Attention / Diagnostic Color**  
  Governance-relevant notices (uncertainty, loop warnings, verification requirements).

Color must **never** encode correctness, quality, approval, persuasion, or preference.

Default state: `Color off`.

---

## Commands (quick reference)

**Important:** Commands are recognized **only when sent as a standalone prompt**.

- `Comm Start` / `Comm Stop`
- `Comm Status` / `Comm Help`
- `Profile Standard | Expert | Sparring | Briefing | Sandbox`
- `SCI on` / `SCI off`
- `Strict on` / `Strict off`
- `Explore on` / `Explore off`
- `Dynamic one-shot on`
- `Color on` / `Color off`

Command tokens are **canonical English-only**.  
Rendered explanations may be localized.

---

## Ethics & responsibility

Ethics are implemented **technically, not rhetorically**:

- LLMs are probabilistic models, not agents.
- Responsibility always remains with the human.
- Transparency and verifiability outrank comfort or persuasion.
- Uncertainty must be **made explicit**, not hidden.

---

## Practical use

Typical workflow:

1. Provide the **canonical JSON ruleset** to the LLM.
2. Activate explicitly at conversation start.
3. Re-initialize deliberately in long sessions.
4. Control behavior **intentionally — never implicitly**.

---

## Target audience

- educators and teachers
- technical and scientific professionals
- reflective power users of LLMs
- anyone prioritizing **control over convenience**

---

## Status

- **Current version:** v19.5.2  
- **Stability:** stable / production-ready  
- **Source of Truth:** canonical JSON ruleset  
  (README is descriptive, not normative)

**Current focus:**  
documentation, examples, usability, evaluation, auditability.

---

## Citation

If you use this framework, please cite the archived Zenodo release:  
https://doi.org/10.5281/zenodo.18072065

---

## License

Creative Commons Attribution 4.0 International (CC BY 4.0)  
https://creativecommons.org/licenses/by/4.0/
