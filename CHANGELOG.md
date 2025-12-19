## v19.0
- Dynamic Prompting remains default-off (manual control)
- One-shot override: "Dynamic einmal an"
- No behavioral auto-adaptation

## v19.0.1
- Added canonical Comm-SCI-Control JSON configuration to the repository.
- Configuration is no longer provided only as a release asset.
- No functional changes to the framework.

## v19.0.2
- Include JSON config files in release snapshot for Zenodo.

## v19.0.3
- Only version numbers updated.
- No functional changes to the framework.

## v19.1
- Added verification route gate for strong claims: requires at least one explicit verification route (measurement OR source OR contrast); otherwise the claim must be downgraded (hypothesis/PR-claim/unclear).
- Added strong-claim keyword heuristics (DE/EN) to trigger the gate and a standardized "Prüfroute" output block with route templates.
- Added optional "measurement snippet" (max 5 lines) for quick framing of technical performance claims (Task/Baseline/Metric/Ablation).
- Added discursive loop guard: if a discussion runs >3 turns without new external friction (measurement/source/contrast/web_check/new_user_data), emit a loop warning and propose choosing a verification route.
- Added evidence cap rule: QC "Evidenz" may not be reported as 3 when a strong claim is made without a verification route (caps to max 2).
- Extended drift detection signals to include discursive loops without external friction.
- Ethics additions: "rule euphoria killswitch" reminder and mandatory-contrast topics list (requires a serious counter-perspective for selected topics).

## v19.2.0
- Added formal Web-Check hook for time-unstable/news-like claims (U4): standardized "Web-Check" output block (query time, search term, top sources, short conclusion, remaining uncertainty) and a marker for parsing/evaluation.
- Added Source-first Hard-Mode for U4/news triggers: hard factual claims are not allowed without either a source or a Web-Check; otherwise the claim must be downgraded and labeled with Unsicherheit U4 + next verification step.
- Extended verification route gate to accept `web_check` as a fourth verification route; added route presence markers (measurement/source/contrast/web_check) and updated loop guard to count Web-Check as external friction.
- Expanded strong-claim/topic triggers (DE/EN) and mandatory-contrast topics to cover AGI/ASI/neocortex-related claims and "Integral AI" variants.
- Tightened U4 next-step wording (explicitly demands Web-/Live-Check or primary source) and added a simple citation-format policy for source-first mode.

## v19.2.1
- Fixed command registry completeness & bilingual symmetry: added explicit EN commands for mode/Sci toggles ("Strict on/off", "Explore on/off", "SCI on/off", "SCIplus on/off") and linked DE variants via aliases (so all documented toggles exist as resolvable commands).
- Changed EN activation/deactivation command strings for Strict/Explore modes to match the new on/off command names.
- Added governance metadata: Source-of-Truth flag for the canonical JSON (clarifies that the canonical ruleset overrides secondary docs on conflicts).
- Changed minor EN syntax-rule examples for consistency ("Profile Expert … / What is time?").
- No changes to core Control-Layer/QC/verification semantics; this is a patch-level command/metadata alignment release.

## v19.3.0
- Introduced **English-only canonical ruleset** (`en-canonical`) as the single Source of Truth.
- Removed all bilingual (`de/en`) command and rule duplication from the core JSON.
- Decoupled **command tokens (EN, invariant)** from **rendered explanations (UI language)**.
- Established architectural split: **kernel logic (JSON)** vs. **language rendering (LLM/UI)**.
- No behavioral change to Control Layer, QC, CGI, or SCI logic.

## v19.3.1
- Added **mandatory help rendering policy** to prevent heuristic filtering of commands.
- Enforced **absolute completeness** for `Comm Help` output.
- Defined mandatory command levels (primary, mode, profile) that must always be rendered.
- Disabled AI-driven summarization and relevance filtering in help output.

## v19.3.2
- Added explicit **UI rendering policy**:
  - Command tokens are always rendered in **English**.
  - Explanatory text is rendered in the **current conversation language**.
  - English fallback if conversation language cannot be determined.
- Eliminated ambiguity between canonical command language and localized explanations.
- No changes to command set or control semantics.

## v19.3.3
- Formalized **`Comm Config`** as a permanent public **primary command**.
- Marked `Comm Config` explicitly as **advanced / read-only / diagnostic**.
- Ensured `Comm Config` is **always listed in `Comm Help`** with a warning note.
- Improved auditability and transparency without adding new control capabilities.

## v19.3.4
- Added **token validation policy** to prevent command hallucinations.
- Enforced explicit lookup of command tokens under `commands.*` before use.
- Added **cross-version leak guard**: only the active canonical JSON defines valid commands.
- Introduced strict handling for **existence queries** as configuration lookups.
- Hardened grounding against LLM heuristic errors without modifying user-facing behavior.

## v19.4.0
- Added optional CSC (Control Layer Subsystem) as a **refinement-only** engine: triggers targeted neutrality/consistency refinements on the draft text **without switching profiles/SCI/overlays or dynamic prompting**.
- Hardened canonical behavior: **English-only command tokens** + token validation; explanatory/help text may be rendered in the conversation language (rendering policy).
- Added cross-version leak guard: when multiple versions appear in context, only the active canonical JSON is authoritative for command tokens/help output.
- Introduced SCI variant selection menu (A–H) with timeout semantics: if SCI selection is pending, the next standalone letter selects the variant; otherwise letters are treated as normal user input.

## v19.4.1
- Fixed CSC governance-trigger refinement: CSC refinement can be **forced by governance triggers** (U4 / Web-Check / strong-claim / negative neutrality delta) to prevent trigger mismatches.
- Improved auditability: bridge signals now use **path-precise parameter references** (thresholds/bindings) for reliable tracing in audits/diagnostics.

## v19.4.2
- **Härtung der SCI-Auditierbarkeit**: Wenn SCI aktiviert ist, muss der vollständige Step-Trace (Plan → Solution → Check) zwingend im Output gerendert werden; eine stille Kompression oder Auslassung der Denkschritte ist untersagt.
- Korrektur der QC-Sichtbarkeit: Sicherstellung, dass die QC-Matrix auch bei minimalen Antwortlängen korrekt gerendert wird.

## v19.4.3
- **Härtung der Menü-Sichtbarkeit**: Solange eine SCI-Variantenwahl (A–H) aussteht, muss das Auswahlmenü in jedem Antwort-Turn gerendert werden, um Fehlbedienungen durch fehlenden Kontext zu vermeiden.

## v19.4.4
- **Härtung des Dialog-Language Rendering**: Explizite Regelung, dass Hilfe-, Status- und Menütexte zwingend in der aktuellen Konversationssprache (z. B. Deutsch) gerendert werden müssen, sofern diese unterstützt wird.
- Befehls-Token (Command Tokens) bleiben davon unberührt und strikt kanonisch Englisch.

## v19.4.5
- **System-Konsolidierung**: Integration der Härtungen aus v19.4.2–v19.4.4 in den stabilen Hauptzweig.
- Optimierung der CSC (Control Layer Subsystem) Logik zur besseren Erkennung von Neutralitäts-Deltas.

## v19.4.6
- **Härtung der Comm-Start Initialisierung**: Das System erzwingt nun bei jedem Neustart die Instanziierung des `default_profile` (Standard).
- Verbot von "Inferred Profile Switching": Automatische Profilwechsel durch die KI basierend auf dem Nutzerkontext sind untersagt; Wechsel erfordern nun ein explizites Audit-Kommando.

## v19.4.7
- **CSC Transparenz-Patch**: Der Marker `CSC-Refine: applied` wurde von intern auf nutzersichtbar umgestellt (`always_visible_if_applied`).
- **U4-Loop Resolution**: Der `discursive_loop_guard` erzwingt nun nach 3 Zügen ohne neue Daten eine markierte `Hypothetical-Model-Analysis`, um argumentative Sackgassen zu durchbrechen.
- **UI Fallback Alignment**: Bei fehlenden Übersetzungen (U1) wird nun automatisch eine zweisprachige Zusammenfassung (EN/DE) erstellt, um den kognitiven Fluss zu erhalten.
- **SCI Context Persistence**: Das Timeout für die Variantenwahl wurde bei inhaltlichen Rückfragen zur Methodik auf 2 Turns erweitert.