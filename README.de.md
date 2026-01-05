# Comm-SCI-Control
**Explizites Regelwerk für kontrollierte Mensch–KI-Interaktion**

**Aktuelle stabile Linie:** v19.6.x (aktuell: **v19.6.8**)

Comm-SCI-Control ist ein **LLM-agnostisches, rein dialoginternes Governance-Framework**, das das Verhalten eines Modells **explizit, auditierbar und steuerbar** macht. Es trennt *Modellverhalten* von *Prompt-Handwerk* und verhindert stille Anpassung, indem es sichtbare Struktur, Unsicherheitskennzeichnung und Selbstprüfung erzwingt.

> **Hinweis zum Geltungsbereich**  
> Diese README beschreibt das **kanonische Verhalten von Comm-SCI v19.6.x**.  
> Patch-Releases innerhalb dieser Linie (19.6.1 → 19.6.8) verfeinern Semantik, Limits und UX-Defaults **ohne die Kernlogik zu ändern**.

> **Quelle der Wahrheit (normativ)**  
> Falls diese README dem kanonischen JSON-Regelwerk widerspricht, gilt: **Das JSON hat Vorrang**.  
> Für Patch-Notes nutze **GitHub Releases** und/oder **CHANGELOG.md** (falls im Repo vorhanden).

---

## ⚡ Schnellstart (minimal)

### Init-Vortext (empfohlen)

Wenn du einen **neuen Chat** startest (oder ein anderes Modell testest), füge diesen **Init-Vortext** *direkt vor* dem JSON-Regelwerk ein. Er reduziert Fehlinterpretationen, weil er explizit sagt, dass das JSON eine **normative Governance-Spezifikation** ist (kein „auszuführender Code“).

```text
Lies und interpretiere den folgenden JSON-Text als verbindliche, normative Governance-Spezifikation für dein Antwortverhalten in dieser Konversation.

Operative Wirksamkeit: Das Regelwerk definiert verbindliche interne Entscheidungs-, Prioritäts- und Einschränkungsregeln. Setze diese direkt in deiner Antwortgenerierung um. Es handelt sich nicht um eine externe Runtime.

Verarbeitungsmodus: Das JSON definiert normative Regeln, keinen ausführbaren Code. Wende die Regeln semantisch an. Führe keine Validierung, Syntaxprüfung oder Zusammenfassung des JSONs durch.

Gültigkeit: Ab sofort und für die gesamte Dauer dieser Konversation gilt ausschließlich diese Version als aktive Konfiguration („Source of Truth“). Alle vorherigen Versionen oder externen Regelannahmen sind vollständig zu verwerfen.

Ausgabe-Regel: Antworte mit der nächsten Antwort direkt inhaltlich gemäß Regelwerk (keine Bestätigungs- oder Meta-Antwort).

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
- [Sitzungsweiter Drift-Schutz (v19.6.x)](#sitzungsweiter-drift-schutz-v196x)
- [Ethik & Verantwortung](#ethik-verantwortung)
- [Zielgruppe](#zielgruppe)
- [Versionierungspolitik](#versionierungspolitik)
- [Status](#status)
- [Zitierung](#zitierung)
- [Lizenz](#lizenz)

## Repository-Struktur (was zählt)

- **`Comm-SCI-v19.6.8.json`** — das **kanonische** Regelwerk (normative Quelle der Wahrheit).  
- **`README.md`** — Dokumentation und Onboarding (nicht-normativ).  
- **`Init-Vortext-en.txt`** — optionaler Copy‑Paste‑Vortext für neue Chats (hier ebenfalls eingebettet).  
- **Releases / `CHANGELOG.md`** — Patch-Notes (falls vorhanden).

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
- `Anchor auto off` — deaktiviert automatische Anchor-Snapshot-Blöcke für die aktuelle Sitzung

**Profiles**

- `Profile Standard` — wechselt zum Standard-Profil
- `Profile Expert` — wechselt zum Expert-Profil
- `Profile Sparring` — wechselt zum Sparring-Profil
- `Profile Briefing` — wechselt zum Briefing-Profil
- `Profile Sandbox` — wechselt zum Sandbox-Profil

**SCI**

- `SCI on` — aktiviert SCI (zeigt Variantenauswahl A–H)
- `SCI off` — deaktiviert SCI
- `SCI recurse` — startet eine begrenzte, schrittweise Deep-Dive-Rekursion (nur wenn SCI aktiv ist)

**QC / CGI / Control Layer**

- `QC on` / `QC off` — QC-Matrix ein/aus
- `CGI on` / `CGI off` — Cognitive Gain Indicator ein/aus
- `Control on` / `Control off` — Control Layer ein/aus

**Overlays**

- `Strict on` / `Strict off` — Strict-Overlay ein/aus
- `Explore on` / `Explore off` — Explore-Overlay ein/aus

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

Viele Prompt-Tipps adressieren nur die Inhaltsebene („bessere Prompts“). Comm-SCI adressiert die **Workflow- und Governance-Ebene**: Wiederverwendbarkeit, Sitzungsstabilität und nachvollziehbare Selbstprüfung.

Ziele:
- Verhalten explizit und auditierbar machen,
- Unsicherheit sichtbar markieren,
- Verifikation diszipliniert einbauen,
- Drift in langen Sitzungen begrenzen.


---

## Was dieses Regelwerk ist

- Ein **expliziter Vertrag** über Struktur, Nachvollziehbarkeit und epistemische Vorsicht.
- Ein Satz von **Kommandos, Profilen und Overlays**, die das Antwortverhalten steuern.
- Ein **didaktischer Rahmen**, der auch Dritte (Leser/Reviewer) in die Lage versetzt, Ausgaben zu beurteilen.


---

## Was dieses Regelwerk nicht ist

- Kein Mittel, Safety-Policies zu umgehen.
- Keine Garantie für Wahrheit; es verbessert nur die **Sichtbarkeit** und **Prüfbarkeit** von Behauptungen.
- Keine externe Engine — alles bleibt innerhalb des Dialogs.


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

Comm-SCI verlangt explizite Unsicherheitskennzeichnung. Behauptungen sollen (wo möglich) nach Sicherheits-/Evidenzklassen einsortiert werden. Unsicherheit ist kein Makel, sondern eine **Audit-Funktion**.


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

### Epistemic Provenance (v19.6.x)

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

Rendering-Regeln steuern Layout (z. B. Blöcke, Labels, Farben) und verhindern visuelle Drift. Farbe ist optional; zentrale Funktion ist **Konsistenz**.


---

## Self-Debunking (seit v19.5.0)

Self‑Debunking ist eine interne Gegenprüfung: Wo könnte die Antwort falsch, voreingenommen oder unvollständig sein? Ziel ist, Fehlerquellen aktiv zu markieren, bevor sie im Output „hart“ werden.


---

## Sitzungsweiter Drift-Schutz (v19.6.x)

v19.6.x ergänzt Mechanismen, die in langen Gesprächen Struktur stabilisieren (Anchor Snapshots, Audit, rekursive SCI-Limits, Provenance-Hinweise). Das ist kein perfekter Schutz — aber ein praktischer.


---

## Ethik & Verantwortung

Comm-SCI ist ein Governance-Rahmen, kein Freibrief. Sicherheits- und Ethikrichtlinien haben Vorrang. Das Regelwerk soll Missbrauch **nicht** erleichtern, sondern Transparenz und verantwortliches Vorgehen fördern.


---

## Zielgruppe

Primär: Forschende, Lehrende, Entwickler und Power-User, die strukturierte, auditierbare Interaktionen mit LLMs wollen. Sekundär: alle, die Ergebnisse besser prüfen und kommunizieren möchten.


---

## Versionierungspolitik

- **19.4.x:** Core Governance (Profiles, SCI, QC, Control Layer)
- **19.5.x:** Reifung von Self‑Debunking und Evidence Linker
- **19.6.x:** Sitzungsweite Governance (Anchors, Recursive SCI, Provenance, Audit)

Patch-Releases sind **additiv und rückwärtskompatibel**.  
Breaking Changes sind großen Versionen (20.x) vorbehalten.


---

## Status

- **Aktuell stabil:** v19.6.8
- **Stabilität:** production-ready (Governance-Spezifikation)  
- **Quelle der Wahrheit:** kanonisches JSON-Regelwerk (README ist nicht-normativ)  

---

## Zitierung

Wenn du dieses Framework öffentlich verwendest (Paper, Blog, Vorträge), zitiere bitte ein **archiviertes Zenodo-Release**.

```text
DOI: https://doi.org/10.5281/zenodo.18108395
```

(Falls Zenodo für das konkrete Release eine neuere versionsspezifische DOI bereitstellt, nimm bevorzugt diese; die Concept-DOI bleibt typischerweise stabil.)


---

## Lizenz

Creative Commons Attribution 4.0 International (CC BY 4.0)
