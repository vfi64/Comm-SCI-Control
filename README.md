# Comm-SCI-Control
**Explicit rule system for controlled human–AI interaction**

**Current stable line:** v19.6.x (current: **v19.6.3**)

Comm-SCI-Control is an **LLM-agnostic, dialog-internal governance framework** for making large language model behavior **explicit, auditable, and controllable**. It separates *model behavior* from *prompt craftsmanship* and prevents silent adaptation by enforcing visible structure, uncertainty handling, and self-audit.

> **Scope note**  
> This README reflects the **canonical behavior of Comm-SCI v19.6.x**.  
> Patch releases within this line (19.6.1 → 19.6.3) refine semantics, limits, and UX defaults **without changing core logic**.

---

## How to read and apply this ruleset (important)

Comm-SCI-Control is a **purely dialog-internal, normative governance and interaction model**.

- ❌ Not executable software  
- ❌ Not a runtime, plugin, or API wrapper  
- ❌ Not a formal object of static verification  

Instead, it acts as an **explicit epistemic and methodological contract** that structures:
- reasoning traces,
- uncertainty signaling,
- verification discipline,
- and self-critique **within a single conversation**.

The ruleset operates **strictly within the model’s built-in system, safety, and ethics policies**, which always take precedence. Where no conflict exists, Comm-SCI-Control is intended to be applied **deliberately and consistently**.

In short:

> **Comm-SCI-Control increases clarity, auditability, and human control — not by enforcement, but by explicit self-binding of the model.**

---

## Motivation

Modern LLMs are powerful, but exhibit systemic weaknesses:

- inconsistent behavior over long conversations,
- silent response drift,
- unclear uncertainty handling,
- outputs that are hard to audit or compare across models.

Comm-SCI-Control addresses these issues **not through better prompts**, but through an **explicit governance layer** that:

- makes reasoning structure visible,
- forces uncertainty classification,
- preserves human control,
- and prevents silent re-adaptation.

---

## What this rule system is

Comm-SCI-Control is:

- a **text-based rule system** (no code execution),
- **LLM-agnostic by design** (compliance may vary by model),
- an **external governance framework** layered above prompts,
- a tool to **reduce drift, ambiguity, and unverifiable output**.

It defines, among other things:

- **Profiles** (Standard, Expert, Sparring, Briefing, Sandbox)
- **Structured reasoning workflows** (SCI / SCIplus)
- an explicit **QC matrix** with deviation reporting (Δ)
- a **hard Control Layer** against silent adaptation
- **uncertainty taxonomy (U1–U6)** and verification routes
- **self-debunking** as mandatory post-answer audit
- **session-level drift protection** (anchors, audit)

---

## What this rule system is not

- ❌ Not an autonomous or self-optimizing agent  
- ❌ Not a truth guarantee  
- ❌ Not a replacement for human judgment  

**Core statement:**  
The system makes errors and drift **visible** — it does not eliminate them.

---

## Core concepts (overview)

### Profiles

Profiles define the **mode of cooperation** between human and model.  
They set **QC target corridors** (what counts as “good enough”).

- Profile switching is **explicit and auditable**
- Implicit or inferred profile changes are forbidden

---

### SCI – Structured Cognitive Interaction

Explicit reasoning structure:

- **SCI:** Plan → Solution → Check  
- **SCIplus:** Extended depth with selectable variants  

When SCI is active:
- the **full reasoning trace is mandatory**
- silent compression or omission is prohibited

#### Recursive SCI (v19.6.x)

For complex tasks, a bounded **nested SCI** can be invoked for sub-questions:

- explicit command
- **maximum depth limited**
- **token budget per level enforced**
- automatic fallback to parent trace on overflow

This enables depth **without losing global structure**.

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

- a **QC self-assessment**
- a **Delta (Δ)** indicating deviation from the active profile’s target corridor

**Delta semantics:**

- Δ < 0 → below target  
- Δ = 0 → within target  
- Δ > 0 → above target (risk of over-optimization)

---

### Control Layer

A meta-layer enforcing:

- rule coherence,
- explicit state transitions,
- prevention of silent behavior changes,
- strict separation of governance logic and presentation.

Hard guards repair violations **within the same output** whenever possible.

---

## Uncertainty handling

Comm-SCI-Control uses an explicit taxonomy:

- **U1** – Data gap  
- **U2** – Logical underdetermination  
- **U3** – Normative disagreement  
- **U4** – Temporal instability  
- **U5** – Model limitation  
- **U6** – Ambiguous query  

Each uncertainty label **forces a next step** (clarification, verification, alternatives).

---

## Verification discipline

- Strong claims require at least one **verification route**  
  (Source, Measurement, Contrast, or Web-Check)
- Claims without a route must be **downgraded and marked with uncertainty**
- Evidence scores are **capped** when verification is missing

---

## Evidence Linker (claim-level reliability)

Claims may be marked with three reliability classes:

- **GREEN** 🟢 – backed by source or verification  
- **YELLOW** 🟡 – reasoned inference  
- **RED** 🔴 – speculation  

> Note: Reliability classes are **epistemic labels** (support level), not claims of correctness.
> When `Color off` is active, render these tags in **plain text** (e.g., `GREEN / YELLOW / RED`) without color icons.


### Epistemic Provenance (v19.6.x)

GREEN claims can optionally carry **origin suffixes**:

- **DOC** – derived from user-provided documents  
- **WEB** – derived from an explicit live web check  
- **TRAIN** – derived from general training knowledge  

To reduce visual overload:

- TRAIN is **suppressed by default**
- WEB/DOC are shown when explicitly known
- Provenance never implies truth or persuasion

---

## Rendering and Color control

- Presentation controls are **strictly separated** from governance logic.
- `Color on/off` is the **user-facing rendering toggle** for showing Evidence Linker reliability classes (🟢/🟡/🔴) and optional provenance suffixes (`DOC`/`WEB`/`TRAIN` where applicable).
- It **does not** change Evidence Linker semantics; it only changes whether the classes are rendered.

### Default

- Default state: `Color on` (for all profiles **except** **Sandbox** and **Briefing**, where it is `Color off` by default)
- When `Color on` is enabled, the model may render reliability classes as 🟢 / 🟡 / 🔴 (and may show provenance suffixes like `WEB` / `DOC` when applicable).

Color must **never** be used for persuasion, approval, or preference.  
It may only encode **explicit epistemic status** (e.g., Evidence Linker classes) or **explicit system state** (e.g., enabled/disabled flags).

---



## Self-Debunking (since v19.5.0)

Every non-Sandbox answer ends with a **Self-Debunking block**:

- exactly **2–3 weaknesses**
- no new factual claims
- no tone-softening or persuasion
- each point includes a suggested next check

Placement:

- after the final answer
- before the QC footer
- SCI trace always remains **before** the answer

Purpose: force bounded epistemic humility.

---

## Session-level drift protection (v19.6.x)

### Anchor Snapshots

To mitigate instruction drift in long conversations:

- periodic **Anchor Snapshots** summarize current state
- include version, profile, SCI state, QC/CGI state
- **frequency increased** to reduce UX noise
- **user opt-out available**

This is a reminder mechanism, not a hard guarantee.

---

## Commands (overview)

- Commands are recognized **only when sent as standalone prompts**.
- Command tokens are **canonical English-only**.
- Explanatory UI may be rendered in the **conversation language**.

### Commands (quick reference)

**Primary**

- `Comm Start` — activate the full Comm-SCI rule system for this session
- `Comm Stop` — deactivate Comm-SCI (platform default behavior; Safety Core remains active)
- `Comm State` (aliases: `Comm Status`) — show the current active state (profile, SCI, QC/CGI targets, Control Layer, overlays)
- `Comm Config` (aliases: `Config`) — print a read-only raw configuration snapshot
- `Comm Anchor` (aliases: `Anchor`) — render an Anchor Snapshot to re-anchor long sessions without changing state
- `Comm Audit` — audit recent assistant answers for compliance and report deviations
- `Anchor auto off` — disable automatic Anchor Snapshot blocks for the current session

**Profiles**

- `Profile Standard` — switch to the Standard profile
- `Profile Expert` — switch to the Expert profile
- `Profile Sparring` — switch to the Sparring profile
- `Profile Briefing` — switch to the Briefing profile
- `Profile Sandbox` — switch to the Sandbox profile

**SCI**

- `SCI on` — enable SCI selection mode and show the SCI variants menu (A–H) when required
- `SCI off` — disable SCI/SCIplus workflows and return to the profile’s standard behavior
- `SCI menu` — re-display the SCI variants menu (A–H)
- `SCI recurse` — start a nested SCI/SCIplus deep-dive for a scoped subquestion

**Mode overlays**

- `Strict on` — enable Strict Mode
- `Strict off` — disable Strict Mode
- `Explore on` — enable Exploration Mode
- `Explore off` — disable Exploration Mode

**Dynamic**

- `Dynamic one-shot on` — enable Dynamic Prompting for the next answer only (non-persistent)

**Rendering**

- `Color on` — enable Evidence Linker color-class tagging (GREEN/YELLOW/RED)
- `Color off` — disable Evidence Linker color-class tagging and return to baseline formatting

### Comm Help

`Comm Help` displays **complete documentation**, starting with a short **didactic introduction**.  
Models are explicitly allowed to provide a **guided explanation** of the system when help is requested.

---

## Ethics & responsibility

- LLMs are probabilistic models, not agents
- Responsibility remains with the human
- Transparency outranks comfort or persuasion
- Uncertainty must be **made explicit**, not hidden

---

## Target audience

- educators and teachers
- scientific and technical professionals
- reflective power users of LLMs
- anyone prioritizing **control over convenience**

Not intended for:
- casual chat
- autonomous agents
- latency-critical production systems

---

## ⚡ Quick Start (minimal)

1. **Instantiate:** Provide/instantiate the canonical JSON ruleset (as the only active governance spec for the session).
2. **Activate:** Send `Comm Start`.
3. **Configure (example):** Send `Profile Expert` and (optionally) `Strict on`.
4. **Work:** Ask your question. For deep dives, use `SCI on` (choose a variant) and `SCI recurse`.

**Move to a new chat (clean reset):**  
`Comm Anchor` → copy the **Anchor Snapshot** into the new chat → re-instantiate the canonical JSON ruleset → `Comm Start` → set `Profile …` and overlays/modes.

> **Epistemic safety note:** Comm-SCI does not eliminate hallucinations; it helps make uncertainty and verification gaps **visible** (e.g., via Evidence Linker classes, with or without color).

---

## Practical use

### Typical workflow

1. Provide the canonical JSON ruleset to the model (as the only active governance spec for the session).
2. Activate explicitly with `Comm Start`.
3. Select a profile via `Profile …` and optional overlays (`Strict on/off`, `Explore on/off`).
4. Use SCI deliberately (`SCI on` → choose a variant; `SCI recurse` for scoped deep dives).
5. In long sessions, re-anchor with `Comm Anchor` and use `Comm Audit` if you suspect drift.


### Re-initialization (new chat / clean reset)

1. Run `Comm Anchor` to produce an **Anchor Snapshot**.
2. Copy the **Anchor Snapshot** into the first message of the new chat.
3. Provide/instantiate the canonical JSON ruleset again (as the only active governance spec for that session).
4. Run `Comm Start`, then set the desired `Profile …` and any overlays/modes (`Strict`, `Explore`, etc.).

---



## Versioning policy

- **19.4.x:** Core governance (Profiles, SCI, QC, Control Layer)
- **19.5.x:** Self-Debunking and Evidence Linker maturation
- **19.6.x:** Session-level governance (Anchors, Recursive SCI, Provenance, Audit)

Patch releases are **additive and backward compatible**.  
Breaking changes are reserved for major versions (20.x).

---

## Status

- **Current stable:** v19.6.3  
- **Stability:** production-ready (governance spec)  
- **Source of truth:** canonical JSON ruleset  

---

## Citation

If you use this framework publicly (papers, blog posts, talks), please cite an **archived Zenodo release**.

- DOI: https://doi.org/10.5281/zenodo.18108395

(If Zenodo provides a newer version DOI for the specific release you used, prefer that; the concept DOI typically remains stable.)

---

## License

Creative Commons Attribution 4.0 International (CC BY 4.0)
