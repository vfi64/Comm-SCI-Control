# Comm-SCI-Control Handbook (EN)

Version: 20.2.0 (operational)  
Reference for explanatory semantics: 20.1.0 (canonical)

## Table of Contents

- [1. Purpose and guiding idea](#1-purpose-and-guiding-idea)
- [2. Target audiences and value profile](#2-target-audiences-and-value-profile)
- [3. Good-fit and poor-fit use cases](#3-good-fit-and-poor-fit-use-cases)
- [4. Learning curve, effort, and return on investment](#4-learning-curve-effort-and-return-on-investment)
- [5. Not an LLM corset: what the system really does](#5-not-an-llm-corset-what-the-system-really-does)
- [6. Architecture and execution model](#6-architecture-and-execution-model)
- [7. Evidence focus instead of prompt optimization](#7-evidence-focus-instead-of-prompt-optimization)
- [8. Self-Debunking: strengths and limits](#8-self-debunking-strengths-and-limits)
- [9. Traceability via SCI Trace](#9-traceability-via-sci-trace)
- [10. Reproducibility: determinism vs probabilistic models](#10-reproducibility-determinism-vs-probabilistic-models)
- [11. Cross-LLM comparability](#11-cross-llm-comparability)
- [12. Drift detection and drift reduction](#12-drift-detection-and-drift-reduction)
- [13. Context-window pressure and token footprint](#13-context-window-pressure-and-token-footprint)
- [14. Wrapper strategy and rule/enforcement separation](#14-wrapper-strategy-and-ruleenforcement-separation)
- [15. Full command reference](#15-full-command-reference)
- [16. Full numeric codes](#16-full-numeric-codes)
- [17. Profiles in depth with typical applications](#17-profiles-in-depth-with-typical-applications)
- [18. SCI variants A-H and SCI recurse](#18-sci-variants-a-h-and-sci-recurse)
- [19. RAG governance (including U7/U8)](#19-rag-governance-including-u7u8)
- [20. Uncertainty U1-U8 with examples](#20-uncertainty-u1-u8-with-examples)
- [21. QC matrix and delta interpretation](#21-qc-matrix-and-delta-interpretation)
- [22. Phi(x): explicit block or distributed function](#22-phix-explicit-block-or-distributed-function)
- [23. Didactic application examples](#23-didactic-application-examples)
- [24. LLM as learning aid for the ruleset](#24-llm-as-learning-aid-for-the-ruleset)
- [25. Installation and setup](#25-installation-and-setup)
- [26. Troubleshooting and debugging flow](#26-troubleshooting-and-debugging-flow)
- [27. Compact startup flow](#27-compact-startup-flow)
- [28. Limits, risks, and realistic expectations](#28-limits-risks-and-realistic-expectations)
- [29. Keyword index](#29-keyword-index)

## 1. Purpose and guiding idea

Comm-SCI-Control is a governance system for LLM interaction, not a collection of style prompts.

It prioritizes:
- better evidence evaluation in answers
- structured human-AI communication
- explicit uncertainty management
- auditable rule adherence

Core orientation:
Not searching for the best prompt, but for better evidence quality, traceability, and comparability.

## 2. Target audiences and value profile

High-value audiences and why:
- Scientists: need source quality controls, uncertainty disclosure, and structured reproducibility.
- Engineers: need deterministic workflows, failure-mode thinking, and explicit verification routes.
- Physicians: need conservative evidence handling and conflict disclosure.
- Lawyers: need fact/value separation and documented reasoning paths.
- Teachers: need didactic structure and transparent answer quality controls.
- Students: benefit from SCI Trace, Self-Debunking, and explicit reasoning scaffolds.

Less suitable for:
- casual, low-stakes chat
- ultra-short responses where governance overhead is not worth it
- pure ideation without evidence goals (use `Profile Sandbox` instead)

## 3. Good-fit and poor-fit use cases

Good fit:
- research-adjacent analysis
- evidence-focused teaching preparation
- technical decision support
- controlled comparison across multiple LLMs

Poor fit or limited fit:
- entertainment-only chat
- expectations of absolute truth guarantees
- highly token-constrained one-liners

## 4. Learning curve, effort, and return on investment

There is a real learning curve. The system pays off most for recurring, quality-critical work.

High ROI:
- researchers, instructors, analysts, and decision-makers with documentation requirements
- teams that compare and audit model output systematically

Lower ROI:
- sporadic one-off queries
- low-structure creative usage only

Practical onboarding path:
- start with `Profile Standard` + `Comm Audit`
- add `SCI on` and RAG governance step by step

## 5. Not an LLM corset: what the system really does

Comm-SCI-Control is a transparent communication layer, not a rigid model corset.

It improves interaction through:
- explicit state control
- stable output contracts
- explicit uncertainty handling
- reproducible audit criteria

Important:
It does not eliminate model variance; it makes deviations more visible and manageable.

## 6. Architecture and execution model

Core components:
- `parser_contract`: valid command tokens and standalone-only command rule
- `state_model`: states such as `active_profile`, `overlay`, `sci_active`, `color`
- `command_model`: deterministic transitions
- `preemptive_logic`: PF-001 to PF-008 before first output token
- `normative_model`: MUST/SHOULD/FORBID + `failure_action`
- `contracts.output_contract`: output block ordering and constraints
- `runtime_guards.context_pressure_guard`: long-context protection
- `csc.engine`: refinement-only pipeline without state switching

Operational execution order:
- P0 Parse
- P1 Route
- P2 State
- P2A Context Pressure
- P2B Preflight
- P3 Output Contract
- P4 Repair
- P5 Render

## 7. Evidence focus instead of prompt optimization

The system is evidence-first:
- verification route requirement for strong claims
- RAG hardening for WEB/DOC/TRAIN mixing
- uncertainty labeling for gaps/conflicts/instability
- evidence classes (`GREEN`, `YELLOW`, `RED`) for claim quality

Outcome:
- lower false confidence
- clearer justification boundaries

## 8. Self-Debunking: strengths and limits

`Self-Debunking` is required for content answers and forbidden for command/status outputs.

Strengths:
- forces explicit self-critique
- reduces one-sided confidence language
- makes limitations visible before closure

Limits:
- adds output length
- can feel heavy for trivial queries
- remains probabilistic in content quality

## 9. Traceability via SCI Trace

When `SCI` is active, `SCI Trace` is mandatory with required steps.

Benefits:
- transparent reasoning path
- didactic value in teaching and learning
- easier fault localization by reasoning step

## 10. Reproducibility: determinism vs probabilistic models

Deterministic parts:
- command parsing
- state transitions
- output contracts
- preflight repair policy (`repair_once_then_block`)

Probabilistic parts:
- wording and argument emphasis
- creative variability by model
- partial differences despite same settings

Practical conclusion:
Comm-SCI-Control improves reproducibility substantially, but cannot fully remove probabilistic variability.

## 11. Cross-LLM comparability

Comparability improves when all models run with identical governance settings:
- same profile/overlay/SCI configuration
- same commands and prompt shape
- same audit criteria
- same context constraints

Useful comparison metrics:
- contract violations per answer
- RAG quality-class discipline
- uncertainty-label quality and timing
- QC delta patterns over tasks

## 12. Drift detection and drift reduction

Drift detection:
- `Comm Audit` compliance checks
- `Comm Anchor` state snapshots
- QC delta trend monitoring
- explicit conflict disclosure in retrieval conflicts

Drift reduction:
- periodic re-anchoring (`Comm Anchor`)
- hard preflight checks
- strict command-token integrity
- context-pressure warning + macro re-anchor

## 13. Context-window pressure and token footprint

Two practical constraints:
- context-window pressure can reduce adherence in long conversations
- large governance payload consumes prompt budget

20.2.0 mitigations:
- `context_pressure_guard` thresholds (medium/high/critical)
- runtime-spine recap
- compact or macro-only modes under pressure

Limit:
At extreme context size, residual degradation risk remains.

## 14. Wrapper strategy and rule/enforcement separation

Core separation:
- JSON ruleset defines governance
- wrapper runtime enforces execution, rendering, tooling, and logging

Wrapper advantages:
- reduced prompt token load
- often higher rule adherence in runtime
- scientific tool integrations are possible
- clean separation of governance and enforcement

Typical wrapper challenges:
- API costs
- rendering differences across models
- formulas/LaTeX rendering variance
- upload and document-link handling
- multimodal integration complexity

Wrapper reference (public):
- [Comm-SCI-Control Wrapper Repository](https://github.com/vfi64/wrapper)

## 15. Full command reference

Source of token list: 20.2.0 `parser_contract.command_tokens`.

### 15.1 Primary

| Command | Function | Typical use |
|---|---|---|
| `Comm Start` | Activates governed session behavior. | session start |
| `Comm Stop` | Deactivates governed behavior (Safety Core remains). | session stop/reset |
| `Comm State` | Outputs active state. | diagnostics |
| `Comm Config` | Outputs raw configuration (read-only). | debug/audit |
| `Comm Anchor` | Renders `Anchor Snapshot`. | re-anchoring |
| `Comm Anchor on` | sets `anchor_auto=on`. | enable anchor automation flag |
| `Comm Anchor off` | sets `anchor_auto=off`. | reduce anchor automation |
| `Comm Audit` | Audits recent answers for compliance. | drift/quality control |
| `Comm Validate` | Heuristic structural checks on the active ruleset context. | fast ruleset sanity check |

### 15.2 Help and codes

| Command | Function |
|---|---|
| `Comm Help` | Full ordered help including commands and numeric codes. |

### 15.3 Profile control

| Command | Function |
|---|---|
| `Profile Standard` | switch to `Standard`. |
| `Profile Expert` | switch to `Expert`, open SCI variant menu. |
| `Profile Sparring` | switch to `Sparring`, open SCI variant menu. |
| `Profile Briefing` | switch to `Briefing`. |
| `Profile Sandbox` | switch to `Sandbox`. |

### 15.4 Mode control

| Command | Function |
|---|---|
| `Strict on` | enable `Strict Mode`. |
| `Strict off` | disable `Strict Mode`. |
| `Explore on` | enable `Exploration Mode`. |
| `Explore off` | disable `Exploration Mode`. |

### 15.5 SCI control

| Command | Function |
|---|---|
| `SCI on` | enter SCI selection flow (A-H). |
| `SCI off` | disable active SCI workflow. |
| `SCI menu` | re-open SCI variant menu. |
| `SCI recurse` | run nested SCI subtrace. |

### 15.6 Color control

| Command | Function |
|---|---|
| `Color on` | enable evidence color markers. |
| `Color off` | disable evidence color markers. |

### 15.7 Dynamic control

| Command | Function |
|---|---|
| `Dynamic one-shot on` | enable dynamic prompting for next answer only. |

## 16. Full numeric codes

Source: canonical 20.1.0 for human-readable code semantics.

Pattern: `Mode-Depth-Audience-Format-CommunicationStyle`  
Dash rule: `-` keeps a category intentionally open.

### 16.1 Categories

| Index | Category | Options |
|---|---|---|
| 1 | `Mode` | `1` Analysis, `2` Creative, `3` Socratic, `4` Compact |
| 2 | `Depth` | `1` Brief, `2` Medium, `3` Detailed |
| 3 | `Audience` | `1` Layperson, `2` Expert, `3` Manager, `4` Teacher, `5` Student, `6` Interested general reader |
| 4 | `Format` | `1` Prose, `2` Table, `3` Bullets, `4` JSON, `5` LaTeX, `6` Diagram/Visualization, `7` Code |
| 5 | `Communication style` | `1` Technical-factual, `2` Philosophical-reflective, `3` Personal-empathic, `4` Critical-provocative |

### 16.2 Examples

- `122-1`: Analysis, Medium, Expert, Format open, Technical-factual
- `411-1`: Compact, Brief, Layperson, Format open, Technical-factual
- `123-4`: Analysis, Medium, Manager, Format open, Critical-provocative

## 17. Profiles in depth with typical applications

| Profile | Character | Good for | Not ideal for |
|---|---|---|---|
| `Standard` | robust general analysis | everyday technical questions | maximal-depth expert work without additional controls |
| `Expert` | strongest evidence discipline | research-like and high-stakes analysis | loose ideation |
| `Sparring` | counter-position pressure testing | argument stress-testing | very short direct replies |
| `Briefing` | concise, structured output | executive summaries | deep derivations |
| `Sandbox` | exploratory creativity | brainstorming and scenarios | strict evidence obligations |

Explicit profile notes:
- `Profile Sparring`: optimized for critical counterargument and synthesis.
- `Profile Sandbox`: optimized for creative range with intentionally reduced `Control Layer` pressure.

## 18. SCI variants A-H and SCI recurse

### 18.1 Variants A-H

| Variant | Name | Focus | Typical example |
|---|---|---|---|
| A | Standard | Plan -> Solution -> Check | solve a standard task |
| B | Deep-Dive | Dialectics++ (13 steps) | examine a controversial thesis |
| C | Branch Evaluation | Tree-of-Thoughts branching | build-vs-buy analysis |
| D | Axiomatic Reduction | first-principles reduction | foundation-level model analysis |
| E | Confidence Tracker | confidence update loop | hypothesis revision |
| F | Impact Projection | second-order effects | policy side-effects |
| G | Failure Mode Analysis | pre-mortem/inversion | rollout risk analysis |
| H | Multi-Agent Simulation | role-based ensemble simulation | cross-expert conflict synthesis |

### 18.2 Purpose of `SCI recurse`

`SCI recurse` creates a nested subtrace for a scoped subproblem and then returns to the parent trace.

Useful when:
- one request contains tightly coupled but distinct subproblems
- one trace would otherwise be too broad and shallow

## 19. RAG governance (including U7/U8)

20.2.0 formalizes hard RAG rules:
- `R-RAG-001`: WEB without `QualityClass` -> downgrade + `U8`
- `R-RAG-002`: never `GREEN` from anonymous/unverifiable WEB sources
- `R-RAG-003`: per-claim provenance required when mixing TRAIN/DOC/WEB
- `R-RAG-004`: if retrieval tools/metadata unavailable -> `U5` + rag_core restriction

Preflight hardening:
- `PF-008` checks `QualityClass` before first output token for WEB claims.

Conflict rule:
- unresolved retrieval conflicts require explicit `Conflict Disclosure` + `U7`.

## 20. Uncertainty U1-U8 with examples

Required format:
`Uncertainty: U# - Name. Needed: ...`

| Code | Name | When to use | Short example |
|---|---|---|---|
| `U1` | Data gap | missing source/data | "Exact value is missing in context." |
| `U2` | Logical underdetermination | assumptions do not uniquely decide | "Multiple conclusions remain plausible." |
| `U3` | Normative disagreement | value conflict | "Facts alone do not settle this trade-off." |
| `U4` | Temporal instability | likely time-sensitive change | "This may have changed recently." |
| `U5` | Model limitation | structural model/tool limit | "No reliable verification possible without tool access." |
| `U6` | Ambiguous query | query has multiple valid interpretations | "Key term is ambiguous." |
| `U7` | Retrieval conflict | sources contradict each other | "Source A conflicts with source B." |
| `U8` | Source quality unassessed | source quality class missing | "WEB claim has no QualityClass." |

## 21. QC matrix and delta interpretation

Dimensions:
- Clarity, Brevity, Evidence, Empathy, Consistency, Neutrality (0..3)

Footer rules:
- one-line `QC-Matrix` footer
- for content answers directly after `Self-Debunking`

Delta meaning:
- `delta = 0`: inside target corridor
- `delta < 0`: below corridor
- `delta > 0`: above corridor (possible over-optimization)

Rule of thumb:
- `|delta| >= 2` => manual correction is recommended

## 22. Phi(x): explicit block or distributed function

Answer to the core question:
- as an explicit `phi_compliance` block, Phi is not separate in 20.2.0
- functionally, Phi behavior remains via:
  - `preemptive_logic` (PF-001 to PF-008)
  - `repair_once_then_block`
  - `output_contract` + `formatting_strictness`
  - optional `CSC` refinement

Interpretation:
- architecture moved from one explicit block to distributed enforcement
- same goal: validate before output, repair once, otherwise block/downgrade

## 23. Didactic application examples

### 23.1 School and university

Mathematics:
- use `SCI` + `Comm Audit` to validate proof structure.
- prompt idea: "Prove the Pythagorean theorem and provide assumptions + verification route."

Physics:
- use `SCI variant F` or `G` for experiment and risk analysis.
- prompt idea: "Analyze a spring pendulum setup including error sources and second-order effects."

Computer science:
- use `SCI variant C` and `G` for algorithm branch/failure analysis.
- prompt idea: "Evaluate QuickSort and list failure modes for adversarial inputs."

### 23.2 Research and decision support

Hypothesis testing:
- `Profile Expert`, `Strict on`, strong RAG governance.

Strategic reasoning:
- `Profile Sparring` for adversarial counterposition and synthesis.

## 24. LLM as learning aid for the ruleset

Practical benefit:
- the LLM can teach the ruleset itself, then self-check via `Comm Audit`.

Useful learning prompts:
- "Explain the difference between `U7` and `U8` with two examples."
- "Show a compliant `Self-Debunking` block for this answer."
- "Compare `Strict` and `Explore` on the same question in two short outputs."

## 25. Installation and setup

The ruleset can be used in two ways: directly as JSON governance in chat, or via a local runtime/wrapper environment.

### 25.1 Minimal setup (JSON directly in chat)

1. Use the current ruleset (`JSON/Comm-SCI-v20.2.0.json`).
2. Insert init preface + JSON into a fresh chat.
3. Activate with `Comm Start`.
4. Set profile and mode (`Profile ...`, optionally `Strict on` or `Explore on`).
5. Re-anchor long sessions with `Comm Anchor`.

### 25.2 Local repo setup (validation/testing)

```bash
cd /path/to/Comm-SCI-Control
bash scripts/validate_repo.sh
```

Optional live E2E:

```bash
CSC_E2E_ENABLE=1 CSC_E2E_API_KEY=... bash scripts/run_e2e_llm_tests.sh
```

### 25.3 Wrapper setup (if external enforcement is desired)

- Wrapper repo: [Comm-SCI-Control Wrapper Repository](https://github.com/vfi64/wrapper)
- Benefit: lower prompt-token overhead, more stable enforcement paths, extensible tool integration.
- Trade-offs: API costs, model-specific rendering differences, operational overhead.

## 26. Troubleshooting and debugging flow

### 26.1 Command is not recognized

Check:
1. Command sent as a standalone message?
2. Exact canonical token used (no translation, no extra text)?
3. Session active (`Comm Start`)?
4. Confirm active state via `Comm State`.

### 26.2 SCI output appears without `SCI Trace`

Check:
1. Is `SCI` truly active (`SCI on` + variant A-H selected)?
2. Was the variant sent as a single-letter message (`A` to `H`)?
3. Run `Comm Audit` and inspect `sci_trace_presence_if_sci_on`.

### 26.3 RAG claim is downgraded (`U8`/`U7`)

Typical cause:
- missing `QualityClass` for WEB claim (`PF-008`, `R-RAG-001`)
- unresolved source conflict (`U7`)

Next step:
- complete retrieval metadata (`QualityClass`, `RetrievedAt`, per-claim provenance)
- only then consider claim upgrade.

### 26.4 SCI menu appears as list instead of table

Check:
1. Run `SCI menu` again (or switch to `Profile Expert`/`Profile Sparring` again).
2. Verify table columns are present: `Variant | Name | Focus / Method`.
3. Run `Comm Audit` and inspect SCI/menu contract findings.

### 26.5 `Comm Help` is incomplete

Check:
1. Run `Comm Help` in a standalone prompt.
2. Verify all command groups are present (primary, profiles, modes, SCI, color, dynamic, help).
3. Verify command/function rows are rendered as tables and not shortened.

### 26.6 Command turn answered an older content question

Expected behavior:
- standalone command turns are terminal and must not backfill older unresolved content prompts.

Check:
1. Send command again as standalone input only.
2. Confirm command output contains no retroactive final-answer block.
3. Continue content work with a fresh explicit question.

### 26.7 Text appears after `QC-Matrix` footer

Expected behavior:
- if a footer is rendered, `QC-Matrix: ...` is the absolute final line.

Check:
1. Ensure no follow-up sentence/question appears after footer.
2. If it happens, run `Comm Audit` and inspect footer placement finding.

### 26.8 Drift in long sessions

Check:
1. `Comm Anchor` for a state snapshot.
2. `Comm Audit` for compliance drift.
3. Watch context pressure; migrate to a fresh chat if thread size is too large.

### 26.9 Local ruleset/repo validation fails

```bash
bash scripts/validate_repo.sh
```

If failing:
1. inspect diff vs `main`
2. regenerate fixtures for intentional ruleset changes
3. rerun validation.

### 26.10 Minimal debugging sequence

```text
Comm State -> Comm Anchor -> Comm Audit -> Comm Validate
```

This gives you state, drift indicators, and structural checks in one fixed order.

## 27. Compact startup flow

```text
1) Comm Start
2) choose profile (usually Standard/Expert/Sparring)
3) optional Strict on or Explore on
4) optional SCI on + variant A-H
5) ask working question
6) for long sessions: Comm Anchor
7) for quality checks: Comm Audit
8) for ruleset sanity checks: Comm Validate
```

## 28. Limits, risks, and realistic expectations

Important limits:
- no 100% truth guarantee
- probabilistic model variance remains
- context and token limits still matter
- RAG quality depends on source quality and metadata completeness

Realistic objective:
- not absolute correctness enforcement
- but earlier error visibility and systematic risk reduction

## 29. Keyword index

- Anchor Snapshot: sections 12, 15
- Command Tokens: section 15
- Context Pressure Guard: section 13
- CSC Engine: sections 6, 22
- Delta: section 21
- Deterministic Transitions: sections 6, 10
- Dynamic one-shot: section 15
- Evidence Linker: sections 7, 15, 19
- Explore Mode: sections 15, 17
- Numeric Codes: section 16
- Phi(x): section 22
- Profile Sandbox: section 17
- Profile Sparring: section 17
- QC-Matrix: section 21
- RAG Hardening: section 19
- SCI recurse: section 18
- SCI Trace: sections 9, 18
- Self-Debunking: section 8
- Strict Mode: sections 15, 17
- Uncertainty U1-U8: section 20
- Verification Route: sections 7, 19
- Wrapper: section 14
