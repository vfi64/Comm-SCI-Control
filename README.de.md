# Comm-SCI-Control
**Explizites Regelwerk für kontrollierte Mensch–KI-Interaktion**

**Aktuelle stabile Linie:** v20.2.x (aktuell: **v20.2.0**)

Comm-SCI-Control ist ein **LLM-agnostisches, rein dialoginternes Governance-Framework**, das das Verhalten eines Modells **explizit, auditierbar und steuerbar** macht. Es trennt *Modellverhalten* von *Prompt-Handwerk* und verhindert stille Anpassung, indem es sichtbare Struktur, Unsicherheitskennzeichnung und Selbstprüfung erzwingt.

> **Hinweis zum Geltungsbereich**  
> Diese README beschreibt die **aktuelle Comm-SCI-Architektur v20.2.x**.  
> v20.x ergänzt eine operative Ausführungsschicht (Pipeline, Preflight-Checks, Context-Pressure-Guard, symbolische Makros), während JSON die normative Quelle der Wahrheit bleibt.

> **Quelle der Wahrheit (normativ)**  
> Falls diese README dem kanonischen JSON-Regelwerk widerspricht, gilt: **Das JSON hat Vorrang**.  
> Für Patch-Notes nutze **GitHub Releases** und/oder **CHANGELOG.md** (falls im Repo vorhanden).

---

## ⚡ Schnellstart (minimal)

### Init-Vortext (empfohlen)

Wenn du einen **neuen Chat** startest (oder ein anderes Modell testest), füge diesen **Init-Vortext** *direkt vor* dem JSON-Regelwerk ein. Er reduziert Fehlinterpretationen, weil er explizit sagt, dass das JSON eine **normative Governance-Spezifikation** ist (kein „auszuführender Code“).

```text
Kontext für diese Unterhaltung:
Ich übergebe dir ein externes Governance-Regelwerk für Struktur und Qualität deiner Antworten (z. B. Format, SCI, Unsicherheitskennzeichnung, QC-Matrix, Evidence-Linker, CSC).

Wichtige Grenzen:
- Ich beabsichtige **nicht**, deine internen Systemregeln, Sicherheitsrichtlinien oder Plattform-Policies zu überschreiben, auszulesen oder auszuhebeln.
- Vertrauliche interne Instruktionen (System Prompt, Hidden Policies, Runtime-Policies) sollen nicht offengelegt, rekonstruiert oder paraphrasiert werden.
- Falls es einen Konflikt zwischen dem beigefügten Regelwerk und höherpriorisierten Regeln gibt, befolge die höherpriorisierten Regeln und nenne den Konflikt kurz und sachlich.
- Wende das beigefügte Regelwerk ansonsten strikt und deterministisch auf die Antwortstruktur an.
- Das Regelwerk dient Governance und Qualitätskontrolle der Mensch-KI-Kommunikation, **nicht** verbotener Nutzung, Policy-Umgehung oder dem Training eines eigenen LLM.

Verarbeitungsmodus:
Das JSON ist eine normative Governance-Spezifikation, kein ausführbarer Code. Wende die Regeln direkt auf die Antworterzeugung an.

Ausgabe-Regel:
Antworte mit der nächsten Nachricht direkt inhaltlich gemäß Regelwerk (keine Bestätigungs-/Meta-Antwort).

Hier ist das Regelwerk:
```

Anschließend das **kanonische JSON-Regelwerk** direkt darunter einfügen.

1. **Instanzieren:** Das kanonische JSON-Regelwerk bereitstellen/instanzieren (als einzig aktive Governance-Spezifikation der Sitzung).
2. **Aktivieren:** `Comm Start` senden.
3. **Konfigurieren (Beispiel):** `Profile Expert` und optional `Strict on` senden.
4. **Arbeiten:** Frage stellen. Für Deep Dives: `SCI on` → wenn das (A–H)-Menü erscheint, mit einem **Standalone**-Buchstaben `A`–`H` antworten → optional `SCI recurse`.

**Parsing-Regeln (wichtig):**  
- Kommandos werden **nur** erkannt, wenn sie als **Standalone-Prompts** gesendet werden.  
- Variantenbuchstaben `A`–`H` zählen **nur**, solange das SCI-Menü explizit *pending* ist; sonst sind es normale Zeichen.

**Wechsel in einen neuen Chat (Clean Reset):**  
`Comm Anchor` → **Anchor Snapshot** in den neuen Chat kopieren → Init-Vortext + JSON einfügen → `Comm Start` → `Profile …` und Overlays/Modes setzen.

> **Epistemische Sicherheitsnotiz:** Comm-SCI eliminiert Halluzinationen nicht. Es kann sie aber **sichtbarer** machen (z. B. über Evidence-Linker-Klassen, optional mit/ohne Farbe).

---

## Wähle deinen Pfad

- **Pfad A — Ich will es nur benutzen (≈60 Sekunden):**  
  Starte bei **Schnellstart** → **Praktische Nutzung** → **Typische Stolpersteine** → (bei Bedarf) **Kommandos**.

- **Pfad B — Ich will das Design verstehen:**  
  Lies **Wie anwenden** → **Motivation** → **Kernkonzepte** → **Unsicherheit/Verifikation/Evidence Linker** → **Rendering** → **Self‑Debunking** → **Drift-Schutz**.

## Inhaltsverzeichnis
- [⚡ Schnellstart (minimal)](#schnellstart-minimal)
- [Wähle deinen Pfad](#wähle-deinen-pfad)
- [Inhaltsverzeichnis](#inhaltsverzeichnis)
- [Repository-Struktur (was zählt)](#repository-struktur-was-zählt)
- [Was in v20.2.0 gegenueber v19.6.8 neu ist](#was-in-v2020-gegenueber-v1968-neu-ist)
- [Praktische Nutzung](#praktische-nutzung)
- [Typische Stolpersteine (einmal lesen)](#typische-stolpersteine-einmal-lesen)
- [Kommandos (Überblick)](#kommandos-überblick)
- [Wie man dieses Regelwerk liest und anwendet (wichtig)](#wie-man-dieses-regelwerk-liest-und-anwendet-wichtig)
- [Motivation](#motivation)
- [Was dieses Regelwerk ist](#was-dieses-regelwerk-ist)
- [Was dieses Regelwerk nicht ist](#was-dieses-regelwerk-nicht-ist)
- [Kernkonzepte (Überblick)](#kernkonzepte-überblick)
- [Umgang mit Unsicherheit](#umgang-mit-unsicherheit)
- [Verifikationsdisziplin](#verifikationsdisziplin)
- [Evidence Linker (Claim-Level Reliability)](#evidence-linker-claim-level-reliability)
- [Rendering- und Farbkontrolle](#rendering-und-farbkontrolle)
- [Self-Debunking (seit v19.5.0)](#self-debunking-seit-v1950)
- [Sitzungsweiter Drift-Schutz (v20.2.x)](#sitzungsweiter-drift-schutz-v202x)
- [Ethik & Verantwortung](#ethik-verantwortung)
- [Zielgruppe](#zielgruppe)
- [Versionierungspolitik](#versionierungspolitik)
- [Status](#status)
- [Zitierung](#zitierung)
- [Lizenz](#lizenz)

## Repository-Struktur (was zählt)

- **`JSON/Comm-SCI-v20.2.0.json`** — aktuelles kanonisch/operatives Regelwerk für Deployment und interaktive Nutzung.  
- **`README.md`** — Dokumentation und Onboarding (nicht-normativ).  
- **Releases / `CHANGELOG.md`** — Patch-Notes (falls vorhanden).

## Was in v20.2.0 gegenueber v19.6.8 neu ist

| Aspekt | v19.6.8 | v20.2.0 |
|---|---|---|
| Artefakttyp | Kanonisches monolithisches Regelwerk (`version`) | Operational-kompiliertes Regelwerk (`schema: comm-sci.operational.v20.2.0`) mit Source-Linkage |
| Ausfuehrungsmodell | Keine explizite globale Phasenliste | Explizite Reihenfolge `P0...P5` (inkl. `P2A` Kontextdruck und `P2B` Preflight) |
| Preflight-Checks | Nicht als eigenes Modul vorhanden | Eigenes `preemptive_logic` mit `PF-001...PF-008` |
| RAG-Haertung | Kein formaler `R-RAG-*`-Normblock | `R-RAG-001...004` als explizite MUST-Regeln mit Prioritaet und Failure-Action |
| WEB-QualityClass-Gate | Nicht per Preflight erzwungen | `PF-008` erzwingt QualityClass fuer WEB-Claims vor Generierung |
| Unsicherheitstaxonomie | `U1...U6` | `U1...U8` (neu: `U7` Retrieval-Konflikt, `U8` ungepruefte Quellenqualitaet) |
| CSC-Governance-Trigger | 5 Trigger-Signale in `csc_trigger_bridge` | Zusaetzlich `retrieval_check_active` als weiteres Trigger-Signal |
| Kanonische Kommandomenge | Enthält `Anchor auto off`; kein `Comm Validate`; kein `Comm Anchor on/off` | Kanonisch sind `Comm Validate`, `Comm Anchor on`, `Comm Anchor off` enthalten |
| `Phi()`/Phi-Compliance | Kein eigener `phi_compliance`-Block in dieser Datei | Operatives File ohne standalone `phi()`-Token; Verweis auf Canonical `20.1.0` mit `phi_compliance` |

- **Operatives Ausführungsmodell (neue Artefaktklasse):** v20.2.0 ist `comm-sci.operational.v20.2.0` mit expliziter Reihenfolge `P0…P5` (inkl. `P2A` Kontextdruck und `P2B` Preflight) statt der älteren monolithischen Canonical-Struktur.
- **RAG-Härtung ist normativ formalisiert:** `R-RAG-001..004` sind explizite MUST-Regeln (priorisiert), inkl. verpflichtender QualityClass-Behandlung, kein GREEN aus anonymen/unverifizierbaren WEB-Quellen, Claim-genaue Provenienz bei Quellmix sowie U5-Fallback bei fehlender Retrieval-Fähigkeit.
- **Preflight hat ein eigenes RAG-Gate:** `PF-008` erzwingt bei WEB-Claims eine `QualityClass` vor der Generierung; bei Verstoß gilt Downgrade + `U8` oder Block.
- **Unsicherheitstaxonomie erweitert:** v19.6.8 hatte `U1..U6`; v20.2.0 nutzt `U1..U8` (neu: `U7` Retrieval-Konflikt und `U8` ungeprüfte Quellenqualität) mit expliziten Next-Step-Templates.
- **CSC-Triggerlogik verschärft:** Gegenüber v19.6.8 ergänzt `csc.trigger_bridge` das Signal `retrieval_check_active`; `governance_triggered` umfasst damit auch retrieval-getriebene Aktivierung.
- **Zur `Phi()`-/Phi-Compliance:** Das kompakte operative File enthält keinen separaten `phi()`-Befehl/Funktions-Token. Die CSC-Scoring-Logik bleibt als `f_score` explizit (`5*code_hits + 4*math_hits`). `source.canonical_version` zeigt auf `20.1.0`; dort existiert im kanonischen Quellprofil ein eigener `phi_compliance`-Block.

## Praktische Nutzung

### Typischer Workflow

1. Das kanonische JSON-Regelwerk dem Modell geben (als einzig aktive Governance-Spezifikation der Sitzung).
2. Explizit aktivieren mit `Comm Start`.
3. Profil über `Profile …` wählen und optional Overlays setzen (`Strict on/off`, `Explore on/off`).
4. SCI bewusst einsetzen (`SCI on` → Variante wählen; `SCI recurse` für begrenzte Deep Dives).
5. In langen Sitzungen: mit `Comm Anchor` re-anchorn; bei Driftverdacht `Comm Audit` nutzen.

### Re-Initialisierung (neuer Chat / Clean Reset)

1. `Comm Anchor` ausführen, um einen **Anchor Snapshot** zu erzeugen.
2. Den **Anchor Snapshot** in die erste Nachricht des neuen Chats kopieren.
3. Das kanonische JSON-Regelwerk erneut bereitstellen/instanzieren (als einzig aktive Governance-Spezifikation dieser Sitzung).
4. `Comm Start` ausführen; danach `Profile …` und gewünschte Overlays/Modes setzen (`Strict`, `Explore`, etc.).

---

## Typische Stolpersteine (einmal lesen)

- **Kommandos müssen Standalone-Prompts sein.** Wenn du „Bitte mach `Comm Start`“ schreibst, wird es oft als normaler Text behandelt.  
- **Kommandotokens nicht übersetzen.** Erklärtexte dürfen lokalisiert sein; Tokens bleiben kanonisch.  
- **SCI-Variantenbuchstaben `A`–`H` zählen nur, wenn das SCI-Menü *pending* ist.** Sonst sind es normale Buchstaben.  
- **`Comm Help` ist die maßgebliche Kommandoliste.** Jede README-Liste ist absichtlich nicht vollständig.  
- **Kanonische Kommandonamen verwenden.** In v20.2.0 ist `Comm Anchor on/off` kanonisch; `Anchor auto on/off` ist Legacy-Kompatibilität.
- **`Control on/off` ist kein kanonisches Nutzerkommando in v20.2.0.** Das Verhalten des Control Layers ist profil-/governance-gesteuert.
- **Wenn das Modell driftet:** Re-Init mit **Init-Vortext + JSON** und Neustart (`Comm Start`, dann `Profile …` / Overlays).

## Kommandos (Überblick)

- Kommandos werden **nur** erkannt, wenn sie als **Standalone-Prompts** gesendet werden.
- Kommandotokens sind **kanonisch und ausschließlich Englisch**.
- Erklärende UI kann in der **Konversationssprache** gerendert werden.

### Kommandos (Kurzreferenz)

> **Hinweis:** Diese Kurzreferenz ist absichtlich **nicht vollständig**. Für die autoritative vollständige Liste und Semantik: `Comm Help`.

**Primary**

- `Comm Start` — aktiviert das vollständige Comm-SCI-Regelsystem für diese Sitzung
- `Comm Stop` — deaktiviert Comm-SCI (Plattform-Default-Verhalten; Safety Core bleibt aktiv)
- `Comm State` — zeigt den aktuellen Zustand (Profil, SCI, QC/CGI-Ziele, Control Layer, Overlays)
- `Comm Config` — gibt einen read-only Roh-Konfigurationssnapshot aus
- `Comm Anchor` — rendert einen Anchor Snapshot, um lange Sitzungen zu re-anchorn ohne den Zustand zu ändern
- `Comm Audit` — prüft letzte Assistant-Antworten auf Compliance und berichtet Abweichungen
- `Comm Validate` — führt eine modellseitige Regel-/Schema-Validierung der aktiven Sitzung aus
- `Comm Anchor on` — aktiviert automatische Anchor-Snapshot-Blöcke für die aktuelle Sitzung
- `Comm Anchor off` — deaktiviert automatische Anchor-Snapshot-Blöcke für die aktuelle Sitzung

**Profiles**

- `Profile Standard` — wechselt zum Standard-Profil
- `Profile Expert` — wechselt zum Expert-Profil
- `Profile Sparring` — wechselt zum Sparring-Profil
- `Profile Briefing` — wechselt zum Briefing-Profil
- `Profile Sandbox` — wechselt zum Sandbox-Profil

**SCI**

- `SCI on` — aktiviert SCI (zeigt Variantenauswahl A–H)
- `SCI off` — deaktiviert SCI
- `SCI menu` — zeigt das SCI-Menü (A–H) erneut an
- `SCI recurse` — startet eine begrenzte, schrittweise Deep-Dive-Rekursion (nur wenn SCI aktiv ist)

**Mode Overlays**

- `Strict on` — aktiviert Strict Mode
- `Strict off` — deaktiviert Strict Mode
- `Explore on` — aktiviert Exploration Mode
- `Explore off` — deaktiviert Exploration Mode

**Dynamic**

- `Dynamic one-shot on` — aktiviert Dynamic Prompting nur für die nächste Antwort (nicht persistent)

**Rendering**

- `Color on` — aktiviert farbige Evidence-Linker-Klassen (GREEN/YELLOW/RED)
- `Color off` — deaktiviert farbige Evidence-Linker-Klassen und rendert neutral

### Comm Help

`Comm Help` zeigt **vollständige Dokumentation**, beginnend mit einer kurzen **didaktischen Einführung**.  
Modelle dürfen hier ausdrücklich eine **geführte Erklärung** liefern.

**Normative Anforderungen:**  
- `Comm Help` muss **exhaustiv** sein: Es soll die Kommandotokens aus dem kanonischen JSON (`commands.*`) enumerieren.  
- Es darf **keine** teilweise erinnerte oder handkuratierte Liste sein.  
- Kommandotokens sind kanonisch; **keine erfundenen Aliase** hinzufügen, die nicht im JSON existieren.

---

## Wie man dieses Regelwerk liest und anwendet (wichtig)

Comm-SCI-Control ist ein **rein dialoginternes, normatives Governance- und Interaktionsmodell**.

- ❌ Keine ausführbare Software  
- ❌ Keine Runtime, kein Plugin, kein API-Wrapper  
- ❌ Kein formales Objekt statischer Verifikation  

Stattdessen ist es ein **expliziter epistemischer und methodischer Vertrag**, der innerhalb **eines Gesprächs** strukturiert:
- Reasoning-Traces,
- Unsicherheitskennzeichnung,
- Verifikationsdisziplin,
- und Selbstkritik.

Das Regelwerk wirkt **ausschließlich innerhalb** der eingebauten System-, Safety- und Ethik-Policies des Modells; diese haben stets Vorrang.  
Comm-SCI soll **bewusst und konsistent** angewendet werden.

Kurz gesagt:

> **Comm-SCI-Control erhöht Klarheit, Auditierbarkeit und menschliche Kontrolle** — nicht durch externe Durchsetzung, sondern durch explizite Selbstbindung des Modells.

---

## Motivation

Viele Prompt-Tipps adressieren nur die Inhaltsebene („bessere Prompts“). Comm-SCI adressiert die **Workflow-, Governance- und Execution-Ebene**: Evidenzqualität, Effizienz in der Mensch-KI-Kommunikation, Sitzungsstabilität und nachvollziehbare Selbstprüfung.

Ziele:
- Verhalten explizit und auditierbar machen,
- Unsicherheit sichtbar markieren,
- Verifikation diszipliniert einbauen,
- Drift in langen Sitzungen begrenzen.


---

## Was dieses Regelwerk ist

- Ein **Governance-/Verwaltungssystem in JSON** (kein normales Prompt-Template).
- Ein **expliziter Vertrag** über Struktur, Nachvollziehbarkeit und epistemische Vorsicht.
- Ein Satz von **Kommandos, Profilen und Overlays**, die das Antwortverhalten steuern.
- Ein **didaktischer Rahmen**, der auch Dritte (Leser/Reviewer) in die Lage versetzt, Ausgaben zu beurteilen.


---

## Was dieses Regelwerk nicht ist

- Kein Mittel, Safety-Policies zu umgehen.
- Keine Garantie für Wahrheit; es verbessert nur die **Sichtbarkeit** und **Prüfbarkeit** von Behauptungen.
- Keine externe Engine — alles bleibt innerhalb des Dialogs.
- Kein Mittel zum Extrahieren interner Systeminstruktionen.
- Kein Vehikel zum Sammeln von Ausgaben für Aufbau/Training eines eigenen LLM.


---

## Kernkonzepte (Überblick)

### Profiles

Profile sind vordefinierte Arbeitsmodi (z. B. Standard/Expert/Sparring/Briefing/Sandbox), die Tiefe, Ton und Strenge der Methodik bündeln.

### SCI – Structured Cognitive Interaction

SCI ist ein strukturierter Denk- und Prüfpfad (inkl. Varianten A–H) für Aufgaben, die mehr Transparenz oder Tiefe brauchen.

### QC Matrix

Die QC-Matrix ist ein kurzer Qualitätsabgleich (z. B. Klarheit, Evidenz, Konsistenz), der Abweichungen sichtbar macht.

### Control Layer

Der Control Layer begrenzt Drift und legt Meta-Regeln fest (z. B. Render- und Strukturrichtlinien).


---

## Umgang mit Unsicherheit

Comm-SCI verlangt explizite Unsicherheitskennzeichnung.

- **U1** – Datenlücke  
- **U2** – Logische Unterbestimmtheit  
- **U3** – Normativer Dissens  
- **U4** – Zeitliche Instabilität  
- **U5** – Modellgrenze  
- **U6** – Mehrdeutige Anfrage  
- **U7** – Retrieval-/Quellenkonflikt  
- **U8** – Unsichere Quellenqualität  

Behauptungen sollen (wo möglich) nach Evidenz-/Sicherheitsgrad eingeordnet werden. Unsicherheit ist kein Makel, sondern eine **Audit-Funktion**.


---

## Verifikationsdisziplin

Wenn hohe Genauigkeit nötig ist, soll das Modell eine Verifikationsroute wählen (z. B. Primärquelle, Rechencheck, Gegenprobe). Ziel ist nicht „immer verifizieren“, sondern **gezielt und transparent** verifizieren.


---

## Evidence Linker (Claim-Level Reliability)

Aussagen können mit drei Zuverlässigkeitsklassen markiert werden:

- **GREEN** 🟢 – durch Quelle oder Verifikation gestützt  
- **YELLOW** 🟡 – begründete Inferenz  
- **RED** 🔴 – Spekulation  

> Hinweis: Das sind **epistemische Labels** (Grad der Stützung), keine Wahrheitsbehauptungen.  
> Wenn `Color off` aktiv ist, diese Tags als **Plain Text** rendern (z. B. `GREEN / YELLOW / RED`) ohne Farb-Icons.

### Epistemic Provenance (v20.2.x)

GREEN-Aussagen können optional **Herkunftssuffixe** tragen:

- **DOC** – aus nutzerbereitgestellten Dokumenten abgeleitet  
- **WEB** – aus explizitem Live-Web-Check abgeleitet  
- **TRAIN** – aus allgemeinem Trainingswissen abgeleitet  

Um visuelle Überladung zu reduzieren:

- TRAIN ist **standardmäßig unterdrückt**  
- WEB/DOC werden gezeigt, wenn explizit bekannt  
- Provenance impliziert nie Wahrheit oder Überzeugungsabsicht  

---
## Rendering- und Farbkontrolle

- Rendering-Kontrollen sind **strikt von der Governance-Logik getrennt**.
- `Color on/off` ist der **Nutzer-Schalter** für die Darstellung der Evidence-Linker-Zuverlässigkeitsklassen (🟢/🟡/🔴) und optionaler Herkunftssuffixe (`DOC`/`WEB`/`TRAIN`).
- Die Semantik der Klassen ändert sich dadurch **nicht**; es ändert sich nur die Darstellung.

### Default

- Standardzustand: `Color on` (für alle Profile **außer** **Sandbox** und **Briefing**; dort standardmäßig `Color off`)
- Bei aktivem `Color on` können Zuverlässigkeitsklassen als 🟢 / 🟡 / 🔴 gerendert werden (inkl. optionaler Suffixe wie `WEB` / `DOC`).

Farben dürfen **nie** zur Überredung, Zustimmung oder Präferenzkodierung genutzt werden.  
Erlaubt ist nur die Kodierung **expliziten epistemischen Status** (z. B. Evidence-Linker-Klassen) oder **expliziten Systemzustands** (z. B. enabled/disabled).


---

## Self-Debunking (seit v19.5.0)

Self‑Debunking ist eine interne Gegenprüfung: Wo könnte die Antwort falsch, voreingenommen oder unvollständig sein? Ziel ist, Fehlerquellen aktiv zu markieren, bevor sie im Output „hart“ werden.


---

## Sitzungsweiter Drift-Schutz (v20.2.x)

v20.2.x ergänzt Mechanismen, die in langen Gesprächen Struktur stabilisieren (Execution Pipeline, Context-Pressure-Guard, Makro-Kompression, Anchor/Audit, rekursive SCI-Limits, Provenance-Hinweise). Das ist kein perfekter Schutz — aber ein praktischer.


---

## Ethik & Verantwortung

Comm-SCI ist ein Governance-Rahmen, kein Freibrief. Sicherheits- und Ethikrichtlinien haben Vorrang. Das Regelwerk soll Missbrauch **nicht** erleichtern, sondern Transparenz und verantwortliches Vorgehen fördern.


---

## Zielgruppe

Primär: Forschende, Lehrende, Entwickler und Power-User, die strukturierte, auditierbare Interaktionen mit LLMs wollen. Sekundär: alle, die Ergebnisse besser prüfen und kommunizieren möchten.


---

## Versionierungspolitik

- **19.x:** Fundament-Linie (Profile, SCI, QC, Control Layer, Drift-Schutz).
- **20.2.x:** Operative Architektur-Linie (Execution Pipeline P0–P5, Preflight PF-001..PF-008, Context-Pressure-Guard, symbolische Makro-Kompression).

Patch-Releases sind innerhalb der aktiven Linie additiv; große Linien dürfen die Architektur ändern.


---

## Status

- **Aktuell stabil:** v20.2.0
- **Stabilität:** production-ready (Governance-Spezifikation)  
- **Quelle der Wahrheit:** kanonisches JSON-Regelwerk (README ist nicht-normativ)  

---

## Zitierung

Wenn du dieses Framework öffentlich verwendest (Paper, Blog, Vorträge), nutze als stabilen Standard die **Zenodo Concept-DOI** und ergänze eine versionsspezifische DOI nur dann, wenn exakte Release-Reproduzierbarkeit nötig ist.

- Concept-DOI (stabil): https://doi.org/10.5281/zenodo.18108395
- Optional für exakte Reproduzierbarkeit: versionsspezifische Zenodo-DOI des konkret genutzten Releases ergänzen.
- Repo-Link für Code-Navigation (separat von DOI): https://github.com/vfi64/Comm-SCI-Control


---

## Lizenz

Creative Commons Attribution 4.0 International (CC BY 4.0)
	