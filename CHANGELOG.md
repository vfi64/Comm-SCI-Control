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

## v19.2
- Added formal Web-Check hook for time-unstable/news-like claims (U4): standardized "Web-Check" output block (query time, search term, top sources, short conclusion, remaining uncertainty) and a marker for parsing/evaluation.
- Added Source-first Hard-Mode for U4/news triggers: hard factual claims are not allowed without either a source or a Web-Check; otherwise the claim must be downgraded and labeled with Unsicherheit U4 + next verification step.
- Extended verification route gate to accept `web_check` as a fourth verification route; added route presence markers (measurement/source/contrast/web_check) and updated loop guard to count Web-Check as external friction.
- Expanded strong-claim/topic triggers (DE/EN) and mandatory-contrast topics to cover AGI/ASI/neocortex-related claims and "Integral AI" variants.
- Tightened U4 next-step wording (explicitly demands Web-/Live-Check or primary source) and added a simple citation-format policy for source-first mode.