# Changelog – Comm-SCI-Control

All notable changes to this project are documented in this file.  
The format follows common conventions: **newest versions first**, additive patch releases only.

## [19.6.7] – 2026-01-01
### Phase-1 Safe Internal Compaction (Current Stable)

#### Changed
- **Safe internal compaction** (token-/drift-schonend):
  - Viele rein erklärende `notes`/`notes_extra`-Felder in `global_defaults` entfernt, ohne die eigentliche Logik zu verändern.
  - `meta.philosophical_foundation` von detaillierten Unterobjekten auf eine **Kurz-Summary** verdichtet (gleiche Aussage, weniger Ballast).
- **QC deviation examples** verschlankt:
  - `global_defaults.qc_deviation_reporting.delta_examples` reduziert (Beispiele bleiben exemplarisch, aber kürzer).
- **Syntax-Beispiele** leicht reduziert:
  - `syntax_rules.examples` gekürzt (weniger Redundanz, gleiche Parser-Intention).

#### Notes
- **Keine Command-Token-Änderungen** (Command-Set unverändert gegenüber 19.6.6).
- Patch-Hinweis-Pointer aktualisiert (`meta.patch_notes_ref`): verweist explizit auf **CHANGELOG.md** als Source of Truth für Patch Notes.


## [19.6.6] – 2025-12-31
### Canonical Cleanup & Patch-Notes Externalization

#### Changed
- **Alias-Stubs entfernt**:
  - Leere `aliases: []`-Felder in `commands.*` entfernt (weniger Rauschen, weniger Risiko, dass Modelle “Aliase erfinden”).
- **Patch Notes aus dem Canonical JSON herausgezogen**:
  - `patch_notes` entfernt; stattdessen `meta.patch_notes_ref` als Verweis auf **CHANGELOG.md / Release Notes**.

#### Notes
- **Keine Command-Token-Änderungen** (nur Strukturbereinigung, keine neuen/entfernten Commands).


## [19.6.5] – 2025-12-31
### Comm Help: Data-Driven + L10N Fix

#### Added
- **L10N-Datenstruktur für Comm Help**:
  - Neue `meta.rendering.l10n.comm_help.*` Strings (de/en) als Datenbasis für lokalisierte Help-Blöcke.

#### Changed
- **Comm Help vollständig datengetrieben**:
  - `Comm Help.required_output` nutzt nun `{L10N:...}`-Resolver statt fest verdrahteter deutscher Help-Strings.
- **Help-Rendering-Härtung**:
  - `global_defaults.help_rendering_policy` erweitert um einen **Completeness-Guard**:
    - Wenn ein Modell in langen Helps Commands unterschlägt, muss der Output im selben Help um eine **„Missing commands“**-Liste repariert werden.
- Patch Notes erweitert um Eintrag **v19.6.5** (im JSON noch enthalten; ab 19.6.6 dann ausgelagert).

#### Fixed
- **Design-Widerspruch beseitigt**: Lokalisierte Help-Strings als Daten + Rendering je nach Konversationssprache (statt Deutsch in den Contract zu “gießen”).
- **Gemini-Failure-Mode adressiert**: systematische Absicherung gegen unvollständige `Comm Help`-Ausgaben.


## [19.6.3] – 2025-12-31
### Stability, Limits & UX Consolidation (Current Stable)

#### Added
- **Recursive SCI hard limits**
  - Maximum recursion depth enforced
  - Token budget per recursion level
  - Defined fallback to parent SCI trace on overflow
- **Anchor Snapshot opt-out**
  - User-controlled deactivation of automatic anchor snapshots
- **Epistemic Provenance display controls**
  - `[GREEN-DOC]` and `[GREEN-WEB]` highlighted when known
  - `[GREEN-TRAIN]` suppressed by default to reduce visual overload

#### Changed
- **Evidence Linker activation semantics unified**
  - Default: **enabled**
  - Explicit opt-out via command
  - Sandbox and Briefing remain profile-level exceptions
- **Anchor Snapshot frequency reduced**
  - Less UX noise in long sessions
- **Command output contracts hardened**
  - Governance commands emit only:
    - current state
    - QC matrix
  - No unsolicited explanatory text

#### Fixed
- Remaining ambiguities between README and canonical JSON
- Edge cases in recursive SCI state propagation
- Minor Control Layer priority inconsistencies


## [19.6.2] – 2025-12-31
### Session Governance Expansion (Feature Release)

#### Added
- **Epistemic Provenance tagging** for GREEN claims:
  - DOC – user-provided documents
  - WEB – explicit live web checks
  - TRAIN – model training knowledge
- **Recursive SCI**
  - Nested SCI / SCIplus for complex sub-questions
- **Anchor Snapshot automation**
  - Periodic state re-anchoring to mitigate instruction drift
- **Comm Audit**
  - Explicit self-check of rule compliance

#### Notes
- Marks transition from **single-response governance** to **session-level governance**
- All new mechanisms are dialog-internal and non-breaking


## [19.6.1] – 2025-12-31
### Command Semantics & Help Refinement

#### Added
- **Complete `Comm Help`**
  - Includes didactic introduction
  - Allows guided system explanations on request

#### Changed
- Evidence Linker activation wording normalized
- Command responses restricted to:
  - status
  - QC matrix
- Reduced unsolicited explanatory output


## [19.6.0] – 2025-12-31
### Governance Architecture Extension

#### Added
- Session-level drift protection framework
- Foundations for:
  - Recursive SCI
  - Anchor Snapshots
  - Provenance-aware Evidence Linker
  - Audit workflows

## [19.5.5] – 2025-12-31
### Governance Consolidation

#### Changed
- Standalone-only command parsing hardened
- Output contracts tightened (QC footer, Self-Debunking)
- Clearer separation between governance logic and presentation


## [19.5.4] – 2025-12-31
### Clarification Patch

#### Changed
- Clarified Self-Debunking placement relative to SCI traces
- Resolved Evidence Linker wording ambiguities
- Explicitly defined:
  - JSON = normative source of truth
  - README = descriptive documentation

## v19.5.3 – 2025-12-27

**Governance clarification for QC rendering (no behavioral change)**

### Added
- Added `meta.governance.clarification_v19_5_3`:
  - Clarifies that the **QC footer** satisfies the **visibility** requirement.
  - **Header rendering is optional** and must not be inferred as mandatory unless explicitly required by a rule.

### Unchanged
- No changes to:
  - Control Layer / CSC behavior
  - QC evaluation or delta semantics
  - SCI / SCIplus logic
  - Command set or parsing rules
  - Profile defaults or overlays

### Summary
v19.5.3 is a **documentation-only patch** that reduces ambiguity around QC header/footer rendering while keeping the runtime behavior fully backward-compatible.
	

## v19.5.2 – 2025-12-25

**Evidence Linker default-off for Briefing (keep Briefing clean), otherwise unchanged**

### Changed
- **Evidence Linker default exceptions**
  - Evidence Linker is now **default-off for Briefing** (Sandbox remains excluded).
  - Default remains **on** for other profiles.

### Unchanged
- No changes to:
  - Control Layer or CSC behavior
  - QC evaluation or delta semantics
  - SCI / SCIplus logic
  - Uncertainty taxonomy or verification routes

### Summary
v19.5.2 keeps Evidence Linker on-by-default for most profiles, but **turns it off for Briefing** to maintain brevity and low visual overhead.



## v19.5.1 – 2025-12-25

**Evidence Linker defaults changed (default-on except Sandbox), still presentation-only**

### Changed
- **Evidence Linker default state**
  - Evidence Linker **color tags are now default-on** for all profiles **except Sandbox**.

### Unchanged
- No changes to:
  - Control Layer or CSC behavior
  - QC evaluation or delta semantics
  - SCI / SCIplus logic
  - Uncertainty taxonomy or verification routes

### Summary
v19.5.1 changes only the **default activation policy** of Evidence Linker (on-by-default except Sandbox) while preserving the “presentation-only” boundary.

---



## v19.5.0 – 2025-12-25

**Always-on Self-Debunking module (strict, post-answer audit), no governance changes**

### Added
- **Self-Debunking (always-on; strict; post-answer, pre-QC)**
  - A mandatory, short self-audit block rendered **after the final answer** and **before the QC footer**.
  - Active for all profiles **except Sandbox**.
  - Must be **2–3 bullets**, must **not introduce new factual claims**, and must focus on weaknesses / assumptions / missing verification steps.

### Clarified
- Self-Debunking is **diagnostic only**:
  - It does not change Control Layer semantics, commands, QC delta semantics, or SCI logic.
  - Its purpose is to expose plausible failure modes and verification gaps in a bounded format.

### Unchanged
- No changes to:
  - Control Layer structure or enforcement
  - CSC engine behavior
  - QC metrics or delta semantics
  - SCI / SCIplus logic
  - Uncertainty taxonomy (U1–U6)
  - Verification-route or Web-Check semantics

### Summary
v19.5.0 adds a **strict, always-on post-answer audit block** (Self-Debunking) to improve transparency and reduce blind spots, without changing any governance logic.

---



## v19.4.21 – 2025-12-23

**Canonical consolidation, deterministic state enforcement, and explicit rendering controls**

### Added
- **Explicit canonical-state enforcement**
  - The active canonical ruleset version is now explicitly asserted and treated as the sole Source of Truth for the entire conversation lifecycle.
  - All secondary, historical, experimental, or contextual rule variants are ignored once v19.4.21 is instantiated.

- **Deterministic initialization guarantees**
  - On session start or re-instantiation, the system explicitly enforces:
    - `default_profile = Standard`
    - `default_code = 122-1`
    - `SCI = off`
    - `Dynamic Prompting = off`
    - `Color = off`
  - Prevents residual state leakage from prior conversations, context fragments, or model-side heuristics.

- **Explicit Color rendering control**
  - Introduced a dedicated `Color on/off` runtime flag.
  - **Purpose of `Color on`:**
    - Improves visual orientation in cognitively dense outputs.
    - Highlights structural, state, or diagnostic elements only.
  - Color rendering is strictly **non-semantic** and must not influence:
    - command resolution,
    - Control Layer logic,
    - QC evaluation,
    - SCI / CSC behavior,
    - uncertainty classification or verification routing.
  - Default state is `Color off`.

- **Color code definitions (rendering layer only)**
  - Exactly three permitted color categories:
    - **Neutral / Structural Color**
      - Structural separation only (headers, tables).
    - **State / Status Color**
      - Explicit system states (profile, SCI, Color on/off).
    - **Attention / Diagnostic Color**
      - Governance-relevant notices (uncertainty, loop warnings).
  - No additional colors or implicit semantics are allowed.

- **Strict separation of configuration vs. interpretation**
  - The JSON configuration is treated as a declarative control specification.
  - No heuristic reinterpretation or stylistic inference is permitted.

### Clarified
- **Scope of authority**
  - v19.4.21 is authoritative strictly within the current chat context.
  - Guarantees non-interaction with external or historical rule variants.

- **Command vs. rendering boundary**
  - Command tokens remain canonical English-only.
  - Rendering features (language, color, formatting) are non-authoritative.

- **State transparency**
  - Active version, profile, control flags, and rendering state must be surfaced explicitly when relevant.

### Unchanged
- No changes to:
  - Control Layer structure or enforcement
  - CSC engine behavior
  - QC metrics or delta semantics
  - SCI / SCIplus logic
  - Uncertainty taxonomy (U1–U6)
  - Verification-route or Web-Check semantics

### Summary
v19.4.21 is a **hardening and consolidation release**.
It introduces no new control capabilities, but **eliminates ambiguity about runtime state, authority, and rendering boundaries**, ensuring maximal determinism and auditability.
---



## v19.4.20 – 2025-12-23

**Extended evidence tag rendering (still presentation-only)**

### Added
- **Emoji-enhanced Evidence Linker rendering (optional)**
  - Evidence Linker tags may optionally include a trailing emoji:
    - `[GREEN]` → 🟢
    - `[YELLOW]` → 🟡
    - `[RED]` → 🔴
  - Textual tags remain canonical; emojis are purely additive.

### Clarified
- Emoji usage:
  - Is optional.
  - Must never replace textual tags.
  - Must not encode additional meaning beyond the existing three classes.

### Unchanged
- No changes to:
  - Control Layer or CSC behavior
  - QC evaluation
  - SCI / SCIplus logic
  - Uncertainty taxonomy or verification routes

### Summary
v19.4.20 refines **visual ergonomics only**, keeping evidence signaling strictly outside governance semantics.

---



## v19.4.19 – 2025-12-23

**Stabilization of evidence signaling infrastructure**

### Clarified
- **Evidence Linker scope**
  - Reaffirmed that Evidence Linker tags remain:
    - non-semantic,
    - non-normative,
    - non-binding.
  - Explicitly documented as **presentation-only metadata**.

### Unchanged
- No changes to:
  - Command set
  - Governance logic
  - Rendering policies
  - Runtime state handling

### Summary
v19.4.19 is a **documentation and stabilization step** ensuring that optional evidence signaling cannot be misinterpreted as evaluative logic.

---



## v19.4.18 – 2025-12-23

**Optional evidence signaling without behavioral impact**

### Added
- **Evidence Linker (optional, default-off)**
  - Introduced an optional, presentation-level Evidence Linker with **three reliability classes**:
    - **GREEN** – high confidence / well-supported
    - **YELLOW** – mixed or partial support
    - **RED** – weak, speculative, or insufficient support
  - Designed purely as an **annotation layer** for human readers.
  - Disabled by default; activation requires explicit configuration.

### Clarified
- Evidence Linker tags:
  - Do **not** affect Control Layer decisions.
  - Do **not** influence QC scoring.
  - Do **not** alter uncertainty labels or verification routing.

### Unchanged
- No changes to:
  - Control Layer logic
  - QC metrics or delta semantics
  - SCI / SCIplus behavior
  - Command parsing or rendering rules

### Summary
v19.4.18 adds **optional evidence signaling** strictly for readability and audit support, without introducing any semantic or behavioral changes.

---



## Diff: v19.4.15 → v19.4.17  – 2025-12-21/23

> Note: v19.4.17 represents a focused stabilization and clarification step relative to later experimental or internal iterations.

### Added
- Extended the uncertainty taxonomy with two additional explicit labels:
  - **U5 – Model limitation**: Marks tasks that are structurally not solvable by an LLM and requires explaining the limitation and, where possible, suggesting alternative or external approaches.
  - **U6 – Ambiguous query**: Marks underspecified or ambiguous user queries and requires clarification or enumeration of plausible interpretations.
- Added dedicated `next_step_templates` for U5 and U6 to enforce appropriate follow-up behavior.

### Clarified
- Made the semantic interpretation of QC Delta values explicit by introducing a `delta_semantics` section:
  - Clearly defines the meaning of negative, zero, and positive Delta values relative to the active profile’s target corridor.
  - Explicitly highlights risks of over-optimization (e.g. hallucination risk when Evidence exceeds its target range).
- Added non-automatic action guidance for QC deviations:
  - `|Δ| ≥ 2`: manual correction by the user is recommended.
  - `|Δ| < 2`: no correction required; monitoring only.

### Unchanged
- No changes to Control Layer structure or enforcement logic.
- No changes to CSC engine placement or behavior.
- No changes to numeric code categories or profile definitions.
- No architectural refactoring or rule priority changes.

### Summary
v19.4.17 consolidates and clarifies core governance semantics (uncertainty handling and QC deviation interpretation) while deliberately avoiding architectural changes. The release is fully backward-compatible in behavior and focuses on auditability and semantic precision rather than feature expansion.


---


## v19.4.7 – 2025-12-19

- **CSC transparency patch:** The marker `CSC-Refine: applied` was switched from internal-only to user-visible (`always_visible_if_applied`).
- **U4 loop resolution:** The `discursive_loop_guard` now forces a clearly marked `Hypothetical-Model-Analysis` after 3 turns without new data, to break argumentative dead-ends.
- **UI fallback alignment:** If translations are missing (U1), the system automatically generates a bilingual summary (EN/DE) to preserve cognitive flow.
- **SCI context persistence:** The timeout for variant selection is extended to 2 turns when the user asks methodological questions instead of sending an A–H token.



## v19.4.6  – 2025-12-19
- **Hardening Comm-Start initialization:** The system now enforces instantiation of the `default_profile` (Standard) on every restart.
- Prohibited “inferred profile switching”: automatic profile changes by the AI based on user context are forbidden; switches now require an explicit audited command.



## v19.4.5 – 2025-12-19
- **System consolidation:** Integrated the hardenings from v19.4.2–v19.4.4 into the stable main line.
- Optimized CSC (Control Layer Subsystem) logic to improve detection of neutrality deltas.



## v19.4.4 – 2025-12-19
- **Hardening dialog-language rendering:** Explicitly requires help, status, and menu text to be rendered in the current conversation language (e.g., German) when supported.
- Command tokens remain unaffected and strictly canonical English.



## v19.4.3 – 2025-12-19
- **Hardening menu visibility:** While an SCI variant selection (A–H) is pending, the selection menu must be rendered on every response turn to prevent user errors caused by missing context.



## v19.4.2 – 2025-12-19
- **Hardening SCI auditability:** When SCI is enabled, the complete step trace (Plan → Solution → Check) must be rendered in the output; silent compression or omission of reasoning steps is prohibited.
- Fixed QC visibility: ensures the QC matrix is rendered correctly even for very short/minimal answers.



## v19.4.1 – 2025-12-19
- Fixed CSC governance-trigger refinement: CSC refinement can be **forced by governance triggers** (U4 / Web-Check / strong-claim / negative neutrality delta) to prevent trigger mismatches.
- Improved auditability: bridge signals now use **path-precise parameter references** (thresholds/bindings) for reliable tracing in audits/diagnostics.



## v19.4.0 . 2025-12-19
- Added optional CSC (Control Layer Subsystem) as a **refinement-only** engine: triggers targeted neutrality/consistency refinements on the draft text **without switching profiles/SCI/overlays or dynamic prompting**.
- Hardened canonical behavior: **English-only command tokens** + token validation; explanatory/help text may be rendered in the conversation language (rendering policy).
- Added cross-version leak guard: when multiple versions appear in context, only the active canonical JSON is authoritative for command tokens/help output.
- Introduced an SCI variant selection menu (A–H) with timeout semantics: if SCI selection is pending, the next standalone letter selects the variant; otherwise letters are treated as normal user input.



## v19.3.4 – 2025-12-19
- Added a **token validation policy** to prevent command hallucinations.
- Enforced explicit lookup of command tokens under `commands.*` before use.
- Added a **cross-version leak guard**: only the active canonical JSON defines valid commands.
- Introduced strict handling for **existence queries** as configuration lookups.
- Hardened grounding against LLM heuristic errors without modifying user-facing behavior.



## v19.3.3 – 2025-12-19
- Formalized **`Comm Config`** as a permanent public **primary command**.
- Marked `Comm Config` explicitly as **advanced / read-only / diagnostic**.
- Ensured `Comm Config` is **always listed in `Comm Help`** with a warning note.
- Improved auditability and transparency without adding new control capabilities.



## v19.3.2 – 2025-12-19
- Added an explicit **UI rendering policy**:
  - Command tokens are always rendered in **English**.
  - Explanatory text is rendered in the **current conversation language**.
  - English fallback if the conversation language cannot be determined.
- Eliminated ambiguity between canonical command language and localized explanations.
- No changes to the command set or control semantics.



## v19.3.1 – 2025-12-19
- Added a **mandatory help rendering policy** to prevent heuristic filtering of commands.
- Enforced **absolute completeness** for `Comm Help` output.
- Defined mandatory command levels (primary, mode, profile) that must always be rendered.
- Disabled AI-driven summarization and relevance filtering in help output.



## v19.3.0 – 2025-12-23
- Introduced an **English-only canonical ruleset** (`en-canonical`) as the single Source of Truth.
- Removed all bilingual (de/en) command and rule duplication from the core JSON.
- Decoupled **command tokens (EN, invariant)** from **rendered explanations (UI language)**.
- Established an architectural split: **kernel logic (JSON)** vs. **language rendering (LLM/UI)**.
- No behavioral change to Control Layer, QC, CGI, or SCI logic.



## v19.2.1 – 2025-12-16
- Fixed command registry completeness & bilingual symmetry: added explicit EN commands for mode/SCI toggles (“Strict on/off”, “Explore on/off”, “SCI on/off”, “SCIplus on/off”) and linked DE variants via aliases (so all documented toggles exist as resolvable commands).
- Changed EN activation/deactivation command strings for Strict/Explore modes to match the new on/off command names.
- Added governance metadata: Source-of-Truth flag for the canonical JSON (clarifies that the canonical ruleset overrides secondary docs on conflicts).
- Changed minor EN syntax-rule examples for consistency (“Profile Expert … / What is time?”).
- No changes to core Control-Layer/QC/verification semantics; this is a patch-level command/metadata alignment release.



## v19.2.0 – 2025-12-16
- Added a formal Web-Check hook for time-unstable/news-like claims (U4): standardized “Web-Check” output block (query time, search term, top sources, short conclusion, remaining uncertainty) and a marker for parsing/evaluation.
- Added Source-first Hard-Mode for U4/news triggers: hard factual claims are not allowed without either a source or a Web-Check; otherwise the claim must be downgraded and labeled with Uncertainty U4 + next verification step.
- Extended the verification-route gate to accept `web_check` as a fourth verification route; added route-presence markers (measurement/source/contrast/web_check) and updated the loop guard to count Web-Check as external friction.
- Expanded strong-claim/topic triggers (DE/EN) and mandatory-contrast topics to cover AGI/ASI/neocortex-related claims and “Integral AI” variants.
- Tightened U4 next-step wording (explicitly demands Web-/Live-Check or a primary source) and added a simple citation-format policy for source-first mode.



## v19.1 – 2025-12-16
- Added a verification-route gate for strong claims: requires at least one explicit verification route (measurement OR source OR contrast); otherwise the claim must be downgraded (hypothesis/PR-claim/unclear).
- Added strong-claim keyword heuristics (DE/EN) to trigger the gate and a standardized “Verification Route” output block with route templates.
- Added an optional “measurement snippet” (max 5 lines) for quick framing of technical performance claims (Task/Baseline/Metric/Ablation).
- Added a discursive loop guard: if a discussion runs >3 turns without new external friction (measurement/source/contrast/web_check/new_user_data), emit a loop warning and propose choosing a verification route.
- Added an evidence-cap rule: QC “Evidence” may not be reported as 3 when a strong claim is made without a verification route (caps to max 2).
- Extended drift-detection signals to include discursive loops without external friction.
- Ethics additions: “rule euphoria killswitch” reminder and a mandatory-contrast topics list (requires a serious counter-perspective for selected topics).



## v19.0.3 – 2025-12-16
- Only version numbers updated.
- No functional changes to the framework.



## v19.0.2 – 2025-12-15
- Included JSON config files in the release snapshot for Zenodo.



## v19.0.1
- Added the canonical Comm-SCI-Control JSON configuration to the repository.
- The configuration is no longer provided only as a release asset.
- No functional changes to the framework.



## v19.0 – 2025-12-15
- Dynamic Prompting remains default-off (manual control).
- One-shot override command: `Dynamic einmal an` (German token kept as-is).
- No behavioral auto-adaptation.