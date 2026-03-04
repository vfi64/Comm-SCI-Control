# Comm-SCI-Control Handbuch (DE)

Version: 20.2.0 (operational)  
Referenz fuer erklaerende Semantik: 20.1.0 (canonical)

## Inhaltsverzeichnis

- [1. Zweck und Leitidee](#1-zweck-und-leitidee)
- [2. Zielgruppen und Nutzenprofil](#2-zielgruppen-und-nutzenprofil)
- [3. Sinnvolle und nicht sinnvolle Anwendung](#3-sinnvolle-und-nicht-sinnvolle-anwendung)
- [4. Lernkurve, Aufwand und Return on Investment](#4-lernkurve-aufwand-und-return-on-investment)
- [5. Kein Prompt-Korsett: Was das System wirklich tut](#5-kein-prompt-korsett-was-das-system-wirklich-tut)
- [6. Architektur und Execution Model](#6-architektur-und-execution-model)
- [7. Evidenzfokus statt Prompt-Optimierung](#7-evidenzfokus-statt-prompt-optimierung)
- [8. Self-Debunking: Vorteile und Grenzen](#8-self-debunking-vorteile-und-grenzen)
- [9. Nachvollziehbarkeit ueber SCI Trace](#9-nachvollziehbarkeit-ueber-sci-trace)
- [10. Reproduzierbarkeit: Determinismus vs Probabilistik](#10-reproduzierbarkeit-determinismus-vs-probabilistik)
- [11. Vergleichbarkeit verschiedener LLM](#11-vergleichbarkeit-verschiedener-llm)
- [12. Drift-Erkennung und Drift-Reduktion](#12-drift-erkennung-und-drift-reduktion)
- [13. Kontextfenster und Token-Footprint](#13-kontextfenster-und-token-footprint)
- [14. Wrapper-Strategie und Trennung von Regelwerk/Enforcement](#14-wrapper-strategie-und-trennung-von-regelwerkenforcement)
- [15. Vollstaendige Command Reference](#15-vollstaendige-command-reference)
- [16. Vollstaendige Numeric Codes](#16-vollstaendige-numeric-codes)
- [17. Profile im Detail mit typischen Anwendungen](#17-profile-im-detail-mit-typischen-anwendungen)
- [18. SCI Varianten A-H und SCI recurse](#18-sci-varianten-a-h-und-sci-recurse)
- [19. RAG Governance (inkl. U7/U8)](#19-rag-governance-inkl-u7u8)
- [20. Uncertainty U1-U8 mit Beispielen](#20-uncertainty-u1-u8-mit-beispielen)
- [21. QC-Matrix und Delta-Interpretation](#21-qc-matrix-und-delta-interpretation)
- [22. Phi(x): enthalten oder verteilt](#22-phix-enthalten-oder-verteilt)
- [23. Didaktische Anwendungsbeispiele](#23-didaktische-anwendungsbeispiele)
- [24. LLM als Lernhilfe fuer das Regelwerk](#24-llm-als-lernhilfe-fuer-das-regelwerk)
- [25. Installation und Setup](#25-installation-und-setup)
- [26. Troubleshooting und Debugging-Flow](#26-troubleshooting-und-debugging-flow)
- [27. Kompakter Startablauf](#27-kompakter-startablauf)
- [28. Grenzen, Risiken und realistische Erwartungen](#28-grenzen-risiken-und-realistische-erwartungen)
- [29. Stichwortverzeichnis](#29-stichwortverzeichnis)

## 1. Zweck und Leitidee

Comm-SCI-Control ist ein Governance-System fuer LLM-Interaktion, kein Satz von Stil-Prompts.

Der Fokus liegt auf:
- besserer Bewertung der Evidenz in Antworten
- strukturierter Mensch-KI-Kommunikation
- kontrollierter Unsicherheitsdarstellung
- auditierbare Regeladherenz statt impliziter Verhaltenserwartung

Leitgedanke:
Nicht die Suche nach dem besten Prompt, sondern die Suche nach besserer Evidenzqualitaet, Nachvollziehbarkeit und Vergleichbarkeit.

## 2. Zielgruppen und Nutzenprofil

Geeignete Zielgruppen mit Begruendung:
- Wissenschaftler: brauchen Quellenqualitaet, Unsicherheitsmarkierung, reproduzierbare Struktur.
- Ingenieure: brauchen deterministische Arbeitsablaeufe, Failure-Mode-Denken, klare Verification Route.
- Aerzte: brauchen explizite Unsicherheit, Konfliktdisclosure, konservative Evidenzklassifikation.
- Juristen: brauchen Trennung von Fakt, Wertung und Unsicherheit; hohe Dokumentationsqualitaet.
- Lehrer: brauchen didaktisch strukturierte, pruefbare Antworten und Steuerungstiefe fuer Unterricht.
- Studenten: profitieren von SCI Trace, Self-Debunking und klarem Lernfeedback.

Weniger geeignet fuer:
- rein spielerische Kurzchats ohne Qualitaetsanspruch
- ultra-kurze ad-hoc Antworten, bei denen Governance-Overhead stoert
- Nutzer, die nur kreative Freitext-Ideen ohne Struktur wollen (dafuer eher `Profile Sandbox`)

## 3. Sinnvolle und nicht sinnvolle Anwendung

Sinnvoll:
- wissenschaftsnahe Analyse
- Unterrichtsvorbereitung mit Evidenzfokus
- technische Entscheidungsfindung
- Vergleich mehrerer LLM unter gleichen Regeln

Nicht sinnvoll oder nur eingeschraenkt sinnvoll:
- reine Unterhaltung/Smalltalk
- vollautomatische Wahrheitsgarantie (unmoeglich bei probabilistischen Modellen)
- extrem knappe Prompts mit harter Tokengrenze

## 4. Lernkurve, Aufwand und Return on Investment

Lernkurve ist real. Das System lohnt sich vor allem fuer Nutzer mit wiederkehrenden, qualitaetskritischen Aufgaben.

Hoher ROI:
- Forscher, Lehrende, Analysten, Entscheider mit Dokumentationspflicht
- Teams, die Antworten systematisch vergleichen oder auditieren wollen

Niedriger ROI:
- sporadische Einmalfragen ohne Folgeprozess
- reine Ideation ohne Evidenzanforderung

Praktischer Einstieg:
- zuerst `Profile Standard` + `Comm Audit`
- danach `SCI on` und `RAG`-Regeln schrittweise nutzen

## 5. Kein Prompt-Korsett: Was das System wirklich tut

Comm-SCI-Control ist kein starres Korsett fuer LLM, sondern eine transparente Kommunikationsschicht.

Es verbessert Interaktion durch:
- explizite State-Steuerung
- einheitliche Output Contracts
- klare Unsicherheitslogik
- reproduzierbare Audit-Kriterien

Wichtig:
Das System verhindert nicht jede Modellabweichung, macht sie aber sichtbarer und messbarer.

## 6. Architektur und Execution Model

Kernbausteine:
- `parser_contract`: gueltige Command Tokens, Standalone-Regel
- `state_model`: zustaende wie `active_profile`, `overlay`, `sci_active`, `color`
- `command_model`: deterministische Transitions
- `preemptive_logic`: PF-001 bis PF-008 vor dem ersten Output-Token
- `normative_model`: MUST/SHOULD/FORBID mit `failure_action`
- `contracts.output_contract`: Reihenfolge und Pflichtbloecke
- `runtime_guards.context_pressure_guard`: Schutz bei langem Kontext
- `csc.engine`: refinement_only ohne State-Switching

Execution Order (operational):
- P0 Parse
- P1 Route
- P2 State
- P2A Context Pressure
- P2B Preflight
- P3 Output Contract
- P4 Repair
- P5 Render

## 7. Evidenzfokus statt Prompt-Optimierung

Systemlogik priorisiert Evidenzarbeit:
- Verification Route bei starken Claims
- RAG-Hardening fuer WEB/DOC/TRAIN-Mix
- Uncertainty bei Datenluecken, Konflikten, Zeitinstabilitaet
- Evidence Linker (`GREEN`, `YELLOW`, `RED`) fuer Claim-Qualitaet

Ergebnis:
- weniger Schein-Sicherheit
- mehr explizite Begruendung

## 8. Self-Debunking: Vorteile und Grenzen

`Self-Debunking` ist fuer Content-Antworten Pflicht (gem. Contract), fuer Command/Status-Ausgaben verboten.

Vorteile:
- zwingt zur Selbstkritik vor Abschluss
- reduziert einseitige Ueberzeugungssprache
- macht Schwachstellen fuer den Nutzer sichtbar

Grenzen:
- erzeugt Zusatzlaenge
- kann bei trivialen Fragen als Overhead wirken
- bleibt modellintern probabilistisch (keine perfekte Fehlergarantie)

## 9. Nachvollziehbarkeit ueber SCI Trace

Wenn `SCI` aktiv ist, muss `SCI Trace` mit den erforderlichen Steps erscheinen.

Nutzen:
- nachvollziehbare Denkschritte statt Black-Box-Eindruck
- didaktischer Mehrwert fuer Unterricht/Studium
- bessere Fehlerlokalisierung (welcher Step war schwach)

## 10. Reproduzierbarkeit: Determinismus vs Probabilistik

Deterministische Anteile:
- Command Parsing
- State Transitions
- Output Contracts
- Preflight-Reparaturregeln (`repair_once_then_block`)

Probabilistische Anteile:
- inhaltliche Formulierung
- Gewichtung von Argumenten
- variable Kreativanteile je Modell

Realistische Aussage:
Comm-SCI-Control erhoeht Reproduzierbarkeit deutlich, ersetzt aber nicht die probabilistische Natur von LLM.

## 11. Vergleichbarkeit verschiedener LLM

Vergleich wird besser, wenn alle Modelle unter identischen Regeln laufen:
- gleiches Profil-/Overlay-/SCI-Setting
- identische Commands
- identische Audit-Kriterien
- gleiche Prompt- und Kontextbedingungen

Metriken fuer Vergleich:
- Contract-Verletzungen pro Antwort
- QualityClass-Disziplin bei RAG
- Haeufigkeit sinnvoller Uncertainty Labels
- Delta-Muster in QC-Matrix

## 12. Drift-Erkennung und Drift-Reduktion

Drift-Erkennung:
- `Comm Audit` (strukturierte Compliance-Checks)
- `Comm Anchor` (State-Snapshot)
- QC Delta-Verlauf
- Konfliktdisclosure bei widerspruechlichen Retrieval-Ergebnissen

Drift-Reduktion:
- regelmaessiges Re-Ankern (`Comm Anchor`)
- harte Preflight-Pruefung
- strikte Command-Token-Integritaet
- Kontextdruck-Warnung und Macro-Re-Ankerung

## 13. Kontextfenster und Token-Footprint

Zwei praktische Probleme:
- Kontextfensterproblem: lange Dialoge reduzieren Regeltreue in mittleren Abschnitten.
- Token-Footprint des Regelwerks: grosse Governance-Dateien verbrauchen Prompt-Budget.

Mechanismen in 20.2.0:
- `context_pressure_guard` mit Schwellwerten (medium/high/critical)
- kompakter Runtime-Spine
- Macro-Mode bei hohem Druck

Grenze:
Auch mit Guard bleibt sehr langes Kontextmaterial ein Risiko.

## 14. Wrapper-Strategie und Trennung von Regelwerk/Enforcement

Grundprinzip:
- JSON-Regelwerk beschreibt Normen
- Wrapper setzt technisch durch (Loading, Rendering, Tooling, Logging)

Vorteile eines Wrapper-Ansatzes:
- geringere Tokenlast im Prompt
- oft hoehere Regeleinhaltung durch kontrollierte Runtime
- Einbindung wissenschaftlicher Tools moeglich
- klare Trennung zwischen Governance und Durchsetzung

Typische Herausforderungen:
- API-Kosten
- Rendering-Unterschiede zwischen Modellen
- Formeln und LaTeX-Darstellung
- Upload-Pfade und Dokumentreferenzen
- multimodale Inhalte (Text/Bild/Datei)

Wrapper-Referenz (oeffentlich):
- [Comm-SCI-Control Wrapper Repository](https://github.com/vfi64/wrapper)

## 15. Vollstaendige Command Reference

Hinweis: Gueltig fuer 20.2.0 `parser_contract.command_tokens`.

### 15.1 Primary

| Command | Funktion | Typischer Einsatz |
|---|---|---|
| `Comm Start` | Aktiviert Regelbetrieb. | Start einer kontrollierten Session |
| `Comm Stop` | Deaktiviert Regelbetrieb (Safety Core bleibt). | Ende/Reset |
| `Comm State` | Zeigt aktuellen State. | Diagnose |
| `Comm Config` | Zeigt Raw Config (read-only). | Debug/Audit |
| `Comm Anchor` | Rendert `Anchor Snapshot`. | Re-Ankerung |
| `Comm Anchor on` | setzt `anchor_auto=on`. | Anchor-Automation aktivieren |
| `Comm Anchor off` | setzt `anchor_auto=off`. | Anchor-Automation reduzieren |
| `Comm Audit` | prueft letzte Antworten auf Compliance. | Drift-/Qualitaetskontrolle |
| `Comm Validate` | heuristische Strukturpruefung des Rule-Context. | schneller Regeln-Sanity-Check |

### 15.2 Help and Codes

| Command | Funktion |
|---|---|
| `Comm Help` | Vollstaendige, geordnete Hilfe inkl. Commands und Numeric Codes. |

### 15.3 Profile Control

| Command | Funktion |
|---|---|
| `Profile Standard` | setzt Profil auf `Standard`. |
| `Profile Expert` | setzt `Expert`, oeffnet SCI Variant Menu. |
| `Profile Sparring` | setzt `Sparring`, oeffnet SCI Variant Menu. |
| `Profile Briefing` | setzt `Briefing`. |
| `Profile Sandbox` | setzt `Sandbox`. |

### 15.4 Mode Control

| Command | Funktion |
|---|---|
| `Strict on` | aktiviert `Strict Mode`. |
| `Strict off` | deaktiviert `Strict Mode`. |
| `Explore on` | aktiviert `Exploration Mode`. |
| `Explore off` | deaktiviert `Exploration Mode`. |

### 15.5 SCI Control

| Command | Funktion |
|---|---|
| `SCI on` | startet SCI-Auswahl (A-H). |
| `SCI off` | beendet aktiven SCI-Workflow. |
| `SCI menu` | zeigt SCI Variant Menu erneut. |
| `SCI recurse` | startet verschachtelten SCI-Subtrace. |

### 15.6 Color Control

| Command | Funktion |
|---|---|
| `Color on` | aktiviert farbige Evidence Marker. |
| `Color off` | deaktiviert farbige Evidence Marker. |

### 15.7 Dynamic Control

| Command | Funktion |
|---|---|
| `Dynamic one-shot on` | aktiviert Dynamic Prompting fuer genau die naechste Antwort. |

## 16. Vollstaendige Numeric Codes

Quelle: canonical 20.1.0, genutzt fuer menschenlesbare Steuerung.

Struktur: `Mode-Depth-Audience-Format-CommunicationStyle`  
Dash-Regel: `-` laesst eine Kategorie bewusst offen.

### 16.1 Kategorien

| Index | Kategorie | Optionen |
|---|---|---|
| 1 | `Mode` | `1` Analysis, `2` Creative, `3` Socratic, `4` Compact |
| 2 | `Depth` | `1` Brief, `2` Medium, `3` Detailed |
| 3 | `Audience` | `1` Layperson, `2` Expert, `3` Manager, `4` Teacher, `5` Student, `6` Interested general reader |
| 4 | `Format` | `1` Prose, `2` Table, `3` Bullets, `4` JSON, `5` LaTeX, `6` Diagram/Visualization, `7` Code |
| 5 | `Communication style` | `1` Technical-factual, `2` Philosophical-reflective, `3` Personal-empathic, `4` Critical-provocative |

### 16.2 Beispiele

- `122-1`: Analysis, Medium, Expert, Format offen, Technical-factual
- `411-1`: Compact, Brief, Layperson, Format offen, Technical-factual
- `123-4`: Analysis, Medium, Manager, Format offen, Critical-provocative

## 17. Profile im Detail mit typischen Anwendungen

| Profile | Charakteristik | Gut geeignet fuer | Eher ungeeignet fuer |
|---|---|---|---|
| `Standard` | robuste Alltagsanalyse | normale Fachfragen | extreme Tiefe ohne Zusatzsteuerung |
| `Expert` | maximale Evidenzdisziplin | Forschung, kritische Entscheidungen | lockere Ideation |
| `Sparring` | Gegenposition und Dialektik | Argumenthaertung, Debatten | reine Kurzantworten |
| `Briefing` | sehr kompakt und klar | Executive Summary | tiefe Herleitungen |
| `Sandbox` | explorativ-kreativ | Brainstorming, Szenarien | harte Evidenzpflicht |

Explizit:
- `Profile Sparring`: fuer kritische Gegenpruefung mit hoher Neutrality/Consistency.
- `Profile Sandbox`: fuer kreative Expansion bei bewusst reduziertem `Control Layer`.

## 18. SCI Varianten A-H und SCI recurse

### 18.1 Varianten A-H

| Variante | Name | Fokus | Typisches Beispiel |
|---|---|---|---|
| A | Standard | Plan -> Solution -> Check | Standardproblem loesen |
| B | Deep-Dive | Dialectics++ (13 Schritte) | kontroverse Thesis pruefen |
| C | Branch Evaluation | Tree-of-Thoughts | Build-vs-Buy |
| D | Axiomatic Reduction | First Principles | Grundlagenpruefung |
| E | Confidence Tracker | Confidence Update | Hypothesen-Revision |
| F | Impact Projection | Second-order effects | Policy-Folgen |
| G | Failure Mode Analysis | Pre-mortem | Rollout-Risiken |
| H | Multi-Agent Simulation | Rollen-Simulation | Expertenkonflikt analysieren |

### 18.2 Wozu `SCI recurse` dient

`SCI recurse` startet einen verschachtelten Subtrace fuer ein Teilproblem und kehrt danach in den Parent Trace zurueck.

Sinnvoll bei:
- gekoppelten Teilfragen mit unterschiedlicher Evidenzlage
- grossen Aufgaben, die sonst in einem einzigen Trace zu breit werden

## 19. RAG Governance (inkl. U7/U8)

20.2.0 enthaelt harte RAG-Normen:
- `R-RAG-001`: WEB ohne `QualityClass` -> downgrade + `U8`
- `R-RAG-002`: kein `GREEN` aus anonymous/unverifiable Quellen
- `R-RAG-003`: bei Mix TRAIN/DOC/WEB pro Claim Provenienz
- `R-RAG-004`: ohne Retrieval-Tools/Metadaten -> `U5` + rag_core

Preflight-Haertung:
- `PF-008` prueft vor erstem Token, ob WEB-Claim eine `QualityClass` hat.

Konfliktregel:
- bei unaufgeloestem Retrieval-Konflikt explizite `Conflict Disclosure` + `U7`.

## 20. Uncertainty U1-U8 mit Beispielen

Pflichtformat:
`Uncertainty: U# - Name. Needed: ...`

| Code | Name | Wann verwenden | Kurzbeispiel |
|---|---|---|---|
| `U1` | Data gap | fehlende Daten/Quelle | "Exakte Zahl fehlt im Kontext." |
| `U2` | Logical underdetermination | Annahmen nicht entscheidend | "Mehrere Schlussfolgerungen sind gleich plausibel." |
| `U3` | Normative disagreement | Wertekonflikt | "Fakten allein entscheiden diese Frage nicht." |
| `U4` | Temporal instability | zeitkritische Veraenderung moeglich | "Status kann sich seit gestern geaendert haben." |
| `U5` | Model limitation | strukturelle LLM-Grenze | "Ohne Toolzugriff ist kein verifizierbarer Nachweis moeglich." |
| `U6` | Ambiguous query | Mehrdeutigkeit der Frage | "Begriff ist nicht eindeutig definiert." |
| `U7` | Retrieval conflict | Quellen widersprechen sich | "Quelle A vs Quelle B konfligiert." |
| `U8` | Source quality unassessed | Qualitaet nicht eingeordnet | "WEB-Quelle ohne QualityClass." |

## 21. QC-Matrix und Delta-Interpretation

Dimensionen:
- Clarity, Brevity, Evidence, Empathy, Consistency, Neutrality (0..3)

Footer:
- eine Zeile als `QC-Matrix: ... (Delta)`
- bei Content-Antworten direkt nach `Self-Debunking`

Delta-Bedeutung:
- `Delta = 0`: innerhalb Zielkorridor
- `Delta < 0`: unter Zielkorridor
- `Delta > 0`: ueber Zielkorridor (potenzielle Uebersteuerung)

Faustregel:
- `|Delta| >= 2` => manuelle Korrektur pruefen

## 22. Phi(x): enthalten oder verteilt

Antwort auf die Kernfrage:
- Als eigener `phi_compliance`-Block ist Phi in 20.2.0 nicht separat enthalten.
- Funktional bleibt Phi erhalten, verteilt auf:
  - `preemptive_logic` (PF-001 bis PF-008)
  - `repair_once_then_block`
  - `output_contract` + `formatting_strictness`
  - optionales `CSC`-Refinement

Bewertung:
- Architekturwechsel von monolithischem Block zu verteiltem Enforcement
- gleiche Zielrichtung: vor Ausgabe pruefen, einmal reparieren, sonst blocken/downgraden

## 23. Didaktische Anwendungsbeispiele

### 23.1 Schule und Hochschule

Mathematik:
- Beweisstruktur mit `SCI` + `Comm Audit` pruefen.
- Beispiel: "Beweise den Satz des Pythagoras; markiere Annahmen und Verification Route."

Physik:
- Experimentanalyse mit `SCI variant F` oder `G`.
- Beispiel: "Analysiere Federpendel inkl. Fehlerquellen und Second-order effects."

Informatik:
- Algorithmusanalyse mit `SCI variant C` und `G`.
- Beispiel: "Bewerte QuickSort und nenne Failure Modes bei schlechtem Input."

### 23.2 Forschung und Entscheidung

Hypothesenpruefung:
- `Profile Expert`, `Strict on`, `RAG`-Regeln aktiv.

Strategiearbeit:
- `Profile Sparring` fuer Gegenpositionen + Synthese.

## 24. LLM als Lernhilfe fuer das Regelwerk

Praktischer Vorteil:
- LLM kann das Regelwerk selbst erklaeren, pruefen und mit `Comm Audit` reflektieren.

Sinnvolle Lernprompts:
- "Erklaere mir den Unterschied zwischen `U7` und `U8` mit zwei eigenen Beispielen."
- "Zeige, wie `Self-Debunking` fuer diese Antwort konkret aussieht."
- "Vergleiche `Strict` und `Explore` fuer dieselbe Frage in zwei kurzen Antworten."

## 25. Installation und Setup

Das Regelwerk kann auf zwei Arten genutzt werden: direkt als JSON-Governance im Chat oder ueber eine lokale Runtime/Wrapper-Umgebung.

### 25.1 Minimal-Setup (JSON direkt im Chat)

1. Aktuelles Ruleset verwenden (`JSON/Comm-SCI-v20.2.0.json`).
2. Init-Preface + JSON in einen neuen Chat einspielen.
3. Mit `Comm Start` aktivieren.
4. Profil und Modus setzen (`Profile ...`, optional `Strict on` oder `Explore on`).
5. Bei langen Verlaeufen mit `Comm Anchor` re-ankern.

### 25.2 Lokales Repo-Setup (Validierung/Test)

```bash
cd /path/to/Comm-SCI-Control
bash scripts/validate_repo.sh
```

Optional fuer Live-E2E:

```bash
CSC_E2E_ENABLE=1 CSC_E2E_API_KEY=... bash scripts/run_e2e_llm_tests.sh
```

### 25.3 Wrapper-Setup (wenn Enforcement ausserhalb des Chats gewuenscht ist)

- Wrapper-Repo: [Comm-SCI-Control Wrapper Repository](https://github.com/vfi64/wrapper)
- Nutzen: geringere Prompt-Tokenlast, stabilere Enforcement-Pfade, erweiterbare Tool-Integration.
- Trade-offs: API-Kosten, Rendering-Differenzen zwischen Modellen, Betriebsaufwand.

## 26. Troubleshooting und Debugging-Flow

### 26.1 Command wird nicht erkannt

Pruefen:
1. Command als Standalone-Nachricht gesendet?
2. Exaktes Token verwendet (keine Uebersetzung, keine Zusatztokens)?
3. Session aktiv (`Comm Start`)?
4. Mit `Comm State` den aktuellen Zustand verifizieren.

### 26.2 SCI-Ausgabe ohne `SCI Trace`

Pruefen:
1. Ist `SCI` wirklich aktiv (`SCI on` + Variante A-H gewaehlt)?
2. Wurde die Variante als einzelne Nachricht (`A` bis `H`) gesendet?
3. `Comm Audit` ausfuehren und auf `sci_trace_presence_if_sci_on` achten.

### 26.3 RAG-Claim wird downgraded (`U8`/`U7`)

Typische Ursache:
- fehlende `QualityClass` bei WEB-Claim (`PF-008`, `R-RAG-001`)
- Konflikt zwischen Quellen (`U7`)

Naechster Schritt:
- Retrieval-Metadaten vervollstaendigen (`QualityClass`, `RetrievedAt`, Provenienz pro Claim)
- Claim erst danach hochstufen.

### 26.4 Drift in langen Sessions

Pruefen:
1. `Comm Anchor` fuer State-Snapshot.
2. `Comm Audit` fuer Compliance-Verletzungen.
3. Kontextdruck beachten (lange Threads ggf. in neuen Chat ueberfuehren).

### 26.5 Regelwerk-/Repo-Validierung faellt lokal fehl

```bash
bash scripts/validate_repo.sh
```

Wenn fehlerhaft:
1. Diff gegen `main` pruefen.
2. Fixtures bei absichtlicher Regelwerksaenderung regenerieren.
3. Danach Validierung erneut laufen lassen.

### 26.6 Minimaler Debugging-Flow

```text
Comm State -> Comm Anchor -> Comm Audit -> Comm Validate
```

So bekommst du schnell Zustand, Drift-Indikatoren und Struktur-Checks in fester Reihenfolge.

## 27. Kompakter Startablauf

```text
1) Comm Start
2) Profile waehlen (meist Standard/Expert/Sparring)
3) optional Strict on oder Explore on
4) optional SCI on + Variante A-H
5) Arbeitsfrage stellen
6) bei langen Sessions: Comm Anchor
7) bei Qualitaetszweifel: Comm Audit
8) bei Regelwerkscheck: Comm Validate
```

## 28. Grenzen, Risiken und realistische Erwartungen

Wichtige Grenzen:
- keine 100%-Wahrheitsgarantie
- probabilistische Modellvarianz bleibt
- Token- und Kontextgrenzen bleiben technisch relevant
- RAG-Qualitaet haengt von Quellenqualitaet und Retrieval-Metadaten ab

Realistische Zielsetzung:
- nicht perfekte Wahrheit erzwingen
- sondern Fehler frueher sichtbar machen und Risiko systematisch reduzieren

## 29. Stichwortverzeichnis

- Anchor Snapshot: Abschnitt 12, 15
- Command Tokens: Abschnitt 15
- Context Pressure Guard: Abschnitt 13
- CSC Engine: Abschnitt 6, 22
- Delta: Abschnitt 21
- Deterministic Transitions: Abschnitt 6, 10
- Dynamic one-shot: Abschnitt 15
- Evidence Linker: Abschnitt 7, 15, 19
- Explore Mode: Abschnitt 15, 17
- Numeric Codes: Abschnitt 16
- Phi(x): Abschnitt 22
- Profile Sandbox: Abschnitt 17
- Profile Sparring: Abschnitt 17
- QC-Matrix: Abschnitt 21
- RAG Hardening: Abschnitt 19
- SCI recurse: Abschnitt 18
- SCI Trace: Abschnitt 9, 18
- Self-Debunking: Abschnitt 8
- Strict Mode: Abschnitt 15, 17
- Uncertainty U1-U8: Abschnitt 20
- Verification Route: Abschnitt 7, 19
- Wrapper: Abschnitt 14
