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
- **LLM-agnostic by design** (used with multiple LLMs; behavior can vary by model compliance),
- an **external control framework** for AI interaction,
- a tool for **reducing friction, drift, and misinterpretation**.

It defines, among other things:

- profiles (Standard, Expert, Sparring, Briefing, Sandbox),
- structured reasoning processes (SCI; extended dialectical depth via variant selection—formerly referred to as “SCIplus”),
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
> *The rule system can make errors and drift more visible — it does not eliminate them.*

---

## Core concepts (brief overview)

### Profiles
Define the **mode of cooperation** between human and AI
(e.g., everyday use, expert analysis, sparring, condensation, exploration).

### SCI (with variants; former “SCIplus” via variant selection)
Explicit reasoning structure:
- **SCI:** Plan → Solution → Check.
- **Extended dialectical depth (formerly “SCIplus”):** enabled via **SCI on** followed by selecting the corresponding SCI variant (e.g., the deep-dive/dialectics++ option in the A–H menu).

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

## New features in v19.x

The v19 line focuses on **verifiability**, **drift control**, and **auditability**—without claiming correctness.

### Verification and evidence discipline
- **Verification Route Gate (v19.1.x):** strong claims require at least one explicit verification route (Measurement / Source / Contrast / Web-Check).
- **Evidence Cap rules (v19.1.x+):** if a strong claim is made without a successful verification route, the Evidence score must not be reported as “3”.

### Friction and stability for time-unstable topics
- **Web-Check Hook + Source-first Hard-Mode (v19.2.0):** for temporally unstable or news-like claims (U4), hard factual statements require a source or a web/live check; otherwise they must be downgraded and labeled.

### Auditability hardening (v19.4.x)
- **SCI trace enforcement (v19.4.2):** if SCI is active, a visible step trace is mandatory (no silent compression/omission).
- **SCI variant menu enforcement (v19.4.3):** when SCI selection is pending, the ruleset requires the A–H menu to be rendered (no silent omission; omissions should be repaired/flagged).
- **Dialog-language UI rendering (v19.4.4):** explanatory/help/status/error/menu text must be rendered in the current conversation language (when supported), while command tokens stay canonical English.
- **Comm Start initialization guard (v19.4.6):** prevents inferred profile switching on activation; profile changes require explicit standalone commands.
- **Edge-case patches (v19.4.7):** CSC refinement marker is required to be user-visible when applied; discursive loop guard adds a marked hypothetical-analysis exit after 3 turns without external friction (when no web/live check is available); translation-gap U1 triggers a concise bilingual key-point summary; SCI variant selection can persist one additional turn for contextual SCI-method questions.


---


### Commands (quick reference)

**Important:** Commands are recognized **only** when sent as a **standalone prompt** (one line, nothing else).

- **Comm Start**: enable the rule system (initialize default profile).
- **Comm Stop**: disable the rule system.
- **Comm Status** *(alias: Comm State)*: show current status.
- **Comm Config** *(alias: Config)*: show a compact configuration view (for audits / debugging).
- **Comm Help**: show the command list and usage notes.

- **Profile Standard | Expert | Sparring | Briefing | Sandbox**: switch profile (standalone only).
- **SCI on / SCI off**: enable/disable SCI (standalone only). If SCI is enabled and a variant selection is pending, the ruleset requires the A–H menu to be rendered (and the Control Layer is expected to repair omissions). **There is no separate “SCIplus” command; the former SCIplus pipeline is accessed via SCI + variant selection.**
- **Strict on / Strict off**: toggle strict mode.
- **Explore on / Explore off**: toggle exploration mode.
- **Dynamic one-shot on**: enable Dynamic Prompting for the next answer only (then auto-resets).



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

- Current version: **v19.4.7**
- Development status: **stable**
- Source of Truth: the **canonical JSON ruleset** (README is descriptive, not normative)

- Current focus: documentation, examples, usability, evaluation


## Citation · Zitation

If you use this framework, please cite the archived version on Zenodo:
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17930749.svg)](https://doi.org/10.5281/zenodo.17930749)
**DOI:** [10.5281/zenodo.17930749](https://doi.org/10.5281/zenodo.17930749)

---

## License

This work is licensed under the
**Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

https://creativecommons.org/licenses/by/4.0/