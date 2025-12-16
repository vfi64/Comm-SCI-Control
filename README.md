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
- **LLM-agnostic** (tested, among others, with ChatGPT, Gemini, Mistral, Claude, DeepSeek),
- an **external control framework** for AI interaction,
- a tool for **reducing friction, drift, and misinterpretation**.

It defines, among other things:

- profiles (Standard, Expert, Sparring, Briefing, Sandbox),
- structured reasoning processes (SCI, SCIplus),
- an explicit QC matrix (including deviation reporting),
- a control layer against silent adaptation,
- optional but controlled extensions (CGI, Trade-Off Guard).

---

## What this rule system is **not**

- ❌ not an autonomous learning or self-optimization system
- ❌ not a wrapper, API extension, or plugin
- ❌ not a guarantee of “true” or “correct” answers
- ❌ not a replacement for human judgment or responsibility

> **Core statement:**
> *The rule system makes errors more visible — it does not eliminate them.*

---

## Core concepts (brief overview)

### Profiles
Define the **mode of cooperation** between human and AI
(e.g., everyday use, expert analysis, sparring, condensation, exploration).

### SCI / SCIplus
Explicit reasoning structure:
- **SCI:** Plan → Solution → Check
- **SCIplus:** extended dialectical examination (many-lenses approach)

### QC Matrix
Six quality dimensions:
- Clarity
- Brevity
- Evidence
- Empathy
- Consistency
- Neutrality

Each response includes:
- a current QC assessment,
- an estimated deviation (Δ) from the profile target.

### Control Layer
Meta-layer to ensure:
- rule coherence,
- drift detection,
- protection against silent behavioral change.

---

## New Features in v19.x

**Compared to v19.0.3:** v19.1.x added the *Verification Route Gate*, *Evidence Cap*, and the *Discursive Loop Guard*; v19.2.0 added the *Web-Check Hook* and *Source-first Hard-Mode*.


The following functional rules enhance verifiability and structural integrity, especially for time-sensitive or highly speculative claims:

### Verification Routes
* **Verification Route Gate (v19.1.x):** Enforces at least one explicit verification route (Measurement, Source, Contrast, or Web Check) for strong claims.
* **Evidence Cap Rules:** If a strong claim is made without a successful verification route, the Evidence QC score is capped at a maximum of 2, preventing overconfidence.

### Friction and Stability
* **Web-Check Hook (v19.2.0):** Formalized mechanism for critical, temporally unstable facts (Uncertainty U4). This action is registered as "external friction" by the system.
* **Source-First Hard-Mode (v19.2.0):** For news-like or unstable claims (U4), hard factual statements are not allowed without a source or a Web Check. Claims are instead downgraded to hypotheses or classified.

### Loop Prevention
* **Discursive Loop Guard (v19.1.x):** Issues a warning when interaction exceeds a defined threshold (>3 turns) without new external friction (Measurement/Source/Contrast/Web Check), mitigating argumentative loops.

---


### Commands (quick reference)
- **Comm Start**: enable the rule system.
- **Comm Stop**: disable the rule system.
- **Comm Status**: show current status (only command allowed as a non-standalone exception).
- **Comm Codes**: show the code/options table.
- **Comm Rules Off**: play mode (ignore Comm rules; safety still applies).
- **Comm Rules On**: return to rule mode.
- **Comm Help**: show help/command list.

## Ethics & responsibility (explicit)

Comm-SCI-Control treats **ethics not as an add-on**,
but as a **functional component of the control logic**.

### Core assumptions

- LLMs are **probabilistic text models**, not intentional agents.
- Responsibility **always remains with the human**.
- Comfort, speed, or persuasiveness must
  **never override transparency and verifiability**.

### Operational ethics within the rule system

Ethics are implemented not morally, but **technically**, through:

- **Safety Core:** no assistance for harm, clear boundaries, transparency.
- **Uncertainty classification (U1–U4):**
  ignorance is explicitly marked — not concealed.
- **QC dimension “Neutrality”:**
  separation of facts and value judgments, counter-perspectives when appropriate.
- **Disabled dynamic prompting (default):**
  no automatic behavioral correction without explicit user decision.

> The goal is **preservation of autonomy**, not optimization at any cost.

---

## Practical use

Comm-SCI-Control is typically used as follows:

1. introduced as a complete JSON rule set into a chat,
2. explicitly activated at the beginning of a new conversation,
3. deliberately re-initialized (reset) in longer dialogues,
4. controlled intentionally rather than automatically.

---

## Target audience

- teachers and educators
- professionals in technical and scientific fields
- reflective power users of LLMs
- people who prioritize **controllability over convenience**

---

## Status

- Current version: **v19.2.0**
- Development status: **stable, production-ready**
- Current focus: documentation, examples, usability, evaluation

---

## Citation · Zitation

If you use this framework, please cite the archived version on Zenodo:
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17930749.svg)](https://doi.org/10.5281/zenodo.17930749)
**DOI:** [10.5281/zenodo.17930749](https://doi.org/10.5281/zenodo.17930749)

---

## License

This work is licensed under the
**Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

https://creativecommons.org/licenses/by/4.0/