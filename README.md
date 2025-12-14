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
- **LLM-agnostic** (tested, among others, with ChatGPT, Gemini, Mistral, DeepSeek),
- an **external control framework** for AI interaction,
- a tool for **reducing friction, drift, and misinterpretation**.

It defines, among other things:

- profiles (Standard, Expert, Sparring, Briefing, Sandbox),
- structured reasoning processes (SCI, SCIplus),
- an explicit QC matrix (including deviation reporting),
- a control layer against silent adaptation,
- optional but controlled extensions (CGI, trade-off guard).

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

- Current version: **v19.0**
- Development status: **stable, production-ready**
- Current focus: documentation, examples, usability, evaluation

---

## License

This work is licensed under the  
**Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

https://creativecommons.org/licenses/by/4.0/