## v19.0
- Dynamic Prompting remains default-off (manual control).
- One-shot override command: `Dynamic einmal an` (German token kept as-is).
- No behavioral auto-adaptation.

## v19.0.1
- Added the canonical Comm-SCI-Control JSON configuration to the repository.
- The configuration is no longer provided only as a release asset.
- No functional changes to the framework.

## v19.0.2
- Included JSON config files in the release snapshot for Zenodo.

## v19.0.3
- Only version numbers updated.
- No functional changes to the framework.

## v19.1
- Added a verification-route gate for strong claims: requires at least one explicit verification route (measurement OR source OR contrast); otherwise the claim must be downgraded (hypothesis/PR-claim/unclear).
- Added strong-claim keyword heuristics (DE/EN) to trigger the gate and a standardized “Verification Route” output block with route templates.
- Added an optional “measurement snippet” (max 5 lines) for quick framing of technical performance claims (Task/Baseline/Metric/Ablation).
- Added a discursive loop guard: if a discussion runs >3 turns without new external friction (measurement/source/contrast/web_check/new_user_data), emit a loop warning and propose choosing a verification route.
- Added an evidence-cap rule: QC “Evidence” may not be reported as 3 when a strong claim is made without a verification route (caps to max 2).
- Extended drift-detection signals to include discursive loops without external friction.
- Ethics additions: “rule euphoria killswitch” reminder and a mandatory-contrast topics list (requires a serious counter-perspective for selected topics).

## v19.2.0
- Added a formal Web-Check hook for time-unstable/news-like claims (U4): standardized “Web-Check” output block (query time, search term, top sources, short conclusion, remaining uncertainty) and a marker for parsing/evaluation.
- Added Source-first Hard-Mode for U4/news triggers: hard factual claims are not allowed without either a source or a Web-Check; otherwise the claim must be downgraded and labeled with Uncertainty U4 + next verification step.
- Extended the verification-route gate to accept `web_check` as a fourth verification route; added route-presence markers (measurement/source/contrast/web_check) and updated the loop guard to count Web-Check as external friction.
- Expanded strong-claim/topic triggers (DE/EN) and mandatory-contrast topics to cover AGI/ASI/neocortex-related claims and “Integral AI” variants.
- Tightened U4 next-step wording (explicitly demands Web-/Live-Check or a primary source) and added a simple citation-format policy for source-first mode.

## v19.2.1
- Fixed command registry completeness & bilingual symmetry: added explicit EN commands for mode/SCI toggles (“Strict on/off”, “Explore on/off”, “SCI on/off”, “SCIplus on/off”) and linked DE variants via aliases (so all documented toggles exist as resolvable commands).
- Changed EN activation/deactivation command strings for Strict/Explore modes to match the new on/off command names.
- Added governance metadata: Source-of-Truth flag for the canonical JSON (clarifies that the canonical ruleset overrides secondary docs on conflicts).
- Changed minor EN syntax-rule examples for consistency (“Profile Expert … / What is time?”).
- No changes to core Control-Layer/QC/verification semantics; this is a patch-level command/metadata alignment release.

## v19.3.0
- Introduced an **English-only canonical ruleset** (`en-canonical`) as the single Source of Truth.
- Removed all bilingual (de/en) command and rule duplication from the core JSON.
- Decoupled **command tokens (EN, invariant)** from **rendered explanations (UI language)**.
- Established an architectural split: **kernel logic (JSON)** vs. **language rendering (LLM/UI)**.
- No behavioral change to Control Layer, QC, CGI, or SCI logic.

## v19.3.1
- Added a **mandatory help rendering policy** to prevent heuristic filtering of commands.
- Enforced **absolute completeness** for `Comm Help` output.
- Defined mandatory command levels (primary, mode, profile) that must always be rendered.
- Disabled AI-driven summarization and relevance filtering in help output.

## v19.3.2
- Added an explicit **UI rendering policy**:
  - Command tokens are always rendered in **English**.
  - Explanatory text is rendered in the **current conversation language**.
  - English fallback if the conversation language cannot be determined.
- Eliminated ambiguity between canonical command language and localized explanations.
- No changes to the command set or control semantics.

## v19.3.3
- Formalized **`Comm Config`** as a permanent public **primary command**.
- Marked `Comm Config` explicitly as **advanced / read-only / diagnostic**.
- Ensured `Comm Config` is **always listed in `Comm Help`** with a warning note.
- Improved auditability and transparency without adding new control capabilities.

## v19.3.4
- Added a **token validation policy** to prevent command hallucinations.
- Enforced explicit lookup of command tokens under `commands.*` before use.
- Added a **cross-version leak guard**: only the active canonical JSON defines valid commands.
- Introduced strict handling for **existence queries** as configuration lookups.
- Hardened grounding against LLM heuristic errors without modifying user-facing behavior.

## v19.4.0
- Added optional CSC (Control Layer Subsystem) as a **refinement-only** engine: triggers targeted neutrality/consistency refinements on the draft text **without switching profiles/SCI/overlays or dynamic prompting**.
- Hardened canonical behavior: **English-only command tokens** + token validation; explanatory/help text may be rendered in the conversation language (rendering policy).
- Added cross-version leak guard: when multiple versions appear in context, only the active canonical JSON is authoritative for command tokens/help output.
- Introduced an SCI variant selection menu (A–H) with timeout semantics: if SCI selection is pending, the next standalone letter selects the variant; otherwise letters are treated as normal user input.

## v19.4.1
- Fixed CSC governance-trigger refinement: CSC refinement can be **forced by governance triggers** (U4 / Web-Check / strong-claim / negative neutrality delta) to prevent trigger mismatches.
- Improved auditability: bridge signals now use **path-precise parameter references** (thresholds/bindings) for reliable tracing in audits/diagnostics.

## v19.4.2
- **Hardening SCI auditability:** When SCI is enabled, the complete step trace (Plan → Solution → Check) must be rendered in the output; silent compression or omission of reasoning steps is prohibited.
- Fixed QC visibility: ensures the QC matrix is rendered correctly even for very short/minimal answers.

## v19.4.3
- **Hardening menu visibility:** While an SCI variant selection (A–H) is pending, the selection menu must be rendered on every response turn to prevent user errors caused by missing context.

## v19.4.4
- **Hardening dialog-language rendering:** Explicitly requires help, status, and menu text to be rendered in the current conversation language (e.g., German) when supported.
- Command tokens remain unaffected and strictly canonical English.

## v19.4.5
- **System consolidation:** Integrated the hardenings from v19.4.2–v19.4.4 into the stable main line.
- Optimized CSC (Control Layer Subsystem) logic to improve detection of neutrality deltas.

## v19.4.6
- **Hardening Comm-Start initialization:** The system now enforces instantiation of the `default_profile` (Standard) on every restart.
- Prohibited “inferred profile switching”: automatic profile changes by the AI based on user context are forbidden; switches now require an explicit audited command.

## v19.4.7
- **CSC transparency patch:** The marker `CSC-Refine: applied` was switched from internal-only to user-visible (`always_visible_if_applied`).
- **U4 loop resolution:** The `discursive_loop_guard` now forces a clearly marked `Hypothetical-Model-Analysis` after 3 turns without new data, to break argumentative dead-ends.
- **UI fallback alignment:** If translations are missing (U1), the system automatically generates a bilingual summary (EN/DE) to preserve cognitive flow.
- **SCI context persistence:** The timeout for variant selection is extended to 2 turns when the user asks methodological questions instead of sending an A–H token.

## Diff: v19.4.17 → v19.4.15

> Note: v19.4.15 represents a focused stabilization and clarification step relative to later experimental or internal iterations.

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
v19.4.15 consolidates and clarifies core governance semantics (uncertainty handling and QC deviation interpretation) while deliberately avoiding architectural changes. The release is fully backward-compatible in behavior and focuses on auditability and semantic precision rather than feature expansion.