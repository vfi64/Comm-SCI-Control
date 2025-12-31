# Comm-SCI-Control
**Explizites Regelsystem für kontrollierte Mensch-KI-Interaktion**

**Aktuelle stabile Linie:** v19.6.x (aktuell: **v19.6.3**)

Comm-SCI-Control ist ein **LLM-agnostisches, dialog-internes Governance-Framework**, um das Verhalten großer Sprachmodelle **explizit, prüfbar und kontrollierbar** zu machen. Es trennt *Modellverhalten* von *Prompt-Engineering* und verhindert schleichende Anpassung durch erzwungene sichtbare Struktur, Unsicherheitshandhabung und Selbst-Audits.

> **Hinweis zum Umfang**  
> Diese README spiegelt das **kanonische Verhalten von Comm-SCI v19.6.x** wider.  
> Patch-Releases innerhalb dieser Linie (19.6.1 → 19.6.3) verfeinern Semantik, Limits und UX-Standards **ohne die Kernlogik zu ändern**.

---

## Wie man dieses Regelsystem liest und anwendet (wichtig)

Comm-SCI-Control ist ein **rein dialog-internes, normatives Governance- und Interaktionsmodell**.

- ❌ Keine ausführbare Software  
- ❌ Keine Runtime, kein Plugin oder API-Wrapper  
- ❌ Kein formales Objekt statischer Verifizierung  

Stattdessen fungiert es als **expliziter epistemischer und methodischer Vertrag**, der strukturiert:
- Argumentationsspuren (Reasoning Traces),
- Unsicherheitssignalisierung,
- Verifizierungsdisziplin,
- und Selbstkritik **innerhalb einer einzelnen Konversation**.

Das Regelsystem operiert **strikt innerhalb der integrierten System-, Sicherheits- und Ethikrichtlinien des Modells**, die immer Vorrang haben. Wo kein Konflikt besteht, ist Comm-SCI-Control dazu gedacht, **bewusst und konsistent** angewendet zu werden.

Kurz gesagt:

> **Comm-SCI-Control erhöht Klarheit, Prüfbarkeit und menschliche Kontrolle – nicht durch Erzwingung, sondern durch explizite Selbstbindung des Modells.**

---

## Motivation

Moderne LLMs sind leistungsfähig, weisen aber systemische Schwächen auf:

- inkonsistentes Verhalten über lange Gespräche hinweg,
- schleichende Antwort-Drift (Silent Drift),
- unklarer Umgang mit Unsicherheit,
- Ergebnisse, die schwer zu prüfen oder zwischen Modellen zu vergleichen sind.

Comm-SCI-Control adressiert diese Probleme **nicht durch bessere Prompts**, sondern durch eine **explizite Governance-Ebene**, die:
- Argumentationsstruktur sichtbar macht,
- Unsicherheitsklassifizierung erzwingt,
- menschliche Kontrolle bewahrt,
- und schleichende Neu-Anpassung verhindert.

---

## Was dieses Regelsystem ist

Comm-SCI-Control ist:
- ein **textbasiertes Regelsystem** (kein Code-Execution),
- **LLM-agnostisch von Design** (Compliance kann je nach Modell variieren),
- ein **externes Governance-Framework**, das über Prompts geschichtet wird,
- ein Werkzeug, um **Drift, Mehrdeutigkeit und nicht verifizierbare Ausgaben zu reduzieren**.

Es definiert unter anderem:
- **Profile** (Standard, Expert, Sparring, Briefing, Sandbox)
- **Strukturierte Argumentations-Workflows** (SCI / SCIplus)
- eine explizite **QC-Matrix** mit Abweichungsberichterstattung (Δ)
- eine **harte Control Layer** gegen schleichende Anpassung
- **Unsicherheits-Taxonomie (U1–U6)** und Verifizierungswege
- **Selbst-Widerlegung** als obligatorischen Post-Answer-Audit
- **Sitzungsebene Drift-Schutz** (Anker, Audit)

---

## Was dieses Regelsystem nicht ist

- ❌ Kein autonomer oder selbst-optimierender Agent  
- ❌ Keine Wahrheitsgarantie  
- ❌ Kein Ersatz für menschliches Urteilsvermögen  

**Kernaussage:**  
Das System macht Fehler und Drift **sichtbar** – es beseitigt sie nicht.

---

## Kernkonzepte (Überblick)

### Profile

Profile definieren den **Kooperationsmodus** zwischen Mensch und Modell.  
Sie legen **QC-Zielkorridore** fest (was als "gut genug" gilt).

- Profilwechsel ist **explizit und prüfbar**
- Implizite oder abgeleitete Profiländerungen sind verboten

---

### SCI – Strukturierte kognitive Interaktion

Explizite Argumentationsstruktur:
- **SCI:** Plan → Lösung → Prüfung  
- **SCIplus:** Erweiterte Tiefe mit wählbaren Varianten  

Wenn SCI aktiv ist:
- ist die **vollständige Argumentationsspur obligatorisch**
- stille Komprimierung oder Auslassung ist verboten

#### Rekursives SCI (v19.6.x)

Für komplexe Aufgaben kann eine begrenzte **verschachtelte SCI** für Teilfragen aufgerufen werden:
- expliziter Befehl
- **maximale Tiefe begrenzt**
- **Token-Budget pro Ebene durchgesetzt**
- automatischer Fallback zur Eltern-Spur bei Überlauf

Dies ermöglicht Tiefe **ohne globale Struktur zu verlieren**.

---

### QC-Matrix

Sechs Qualitätsdimensionen:
- Klarheit  
- Kürze  
- Evidenz  
- Empathie  
- Konsistenz  
- Neutralität  

Jede Antwort enthält:
- eine **QC-Selbsteinschätzung**
- ein **Delta (Δ)**, das die Abweichung vom Zielkorridor des aktiven Profils angibt

**Delta-Semantik:**
- Δ < 0 → unter dem Ziel  
- Δ = 0 → innerhalb des Ziels  
- Δ > 0 → über dem Ziel (Risiko der Über-Optimierung)

---

### Control Layer

Eine Meta-Ebene, die erzwingt:
- Regelkohärenz,
- explizite Zustandsübergänge,
- Verhinderung stiller Verhaltensänderungen,
- strikte Trennung von Governance-Logik und Darstellung.

Harte Guards reparieren Verstöße **innerhalb derselben Ausgabe**, wann immer möglich.

---

## Unsicherheitshandhabung

Comm-SCI-Control verwendet eine explizite Taxonomie:
- **U1** – Datenlücke  
- **U2** – Logische Unterdetermination  
- **U3** – Normative Uneinigkeit  
- **U4** – Zeitliche Instabilität  
- **U5** – Modellbeschränkung  
- **U6** – Mehrdeutige Anfrage  

Jedes Unsicherheits-Label **erzwingt einen nächsten Schritt** (Klärung, Verifizierung, Alternativen).

---

## Verifizierungsdisziplin

- Starke Behauptungen erfordern mindestens einen **Verifizierungsweg**  
  (Quelle, Messung, Kontrast oder Web-Check)
- Behauptungen ohne Weg müssen **herabgestuft und mit Unsicherheit markiert werden**
- Evidenz-Scores sind **gedeckelt**, wenn Verifizierung fehlt

---

## Evidence Linker (Claim-Level-Zuverlässigkeit)

Behauptungen können mit drei Zuverlässigkeitsklassen markiert werden:
- **GRÜN** 🟢 – durch Quelle oder Verifizierung gestützt  
- **GELB** 🟡 – begründete Schlussfolgerung  
- **ROT** 🔴 – Spekulation  

> Hinweis: Zuverlässigkeitsklassen sind **epistemische Labels** (Unterstützungsniveau), keine Wahrheitsbehauptungen.
> Wenn `Color off` aktiv ist, werden diese Tags in **Klartext** dargestellt (z. B. `GRÜN / GELB / ROT`) ohne Farbicons.

### Epistemische Provenienz (v19.6.x)

GRÜNE Behauptungen können optional **Herkunfts-Suffixe** tragen:
- **DOC** – abgeleitet aus nutzerbereitgestellten Dokumenten  
- **WEB** – abgeleitet aus einer expliziten Live-Websuche  
- **TRAIN** – abgeleitet aus allgemeinem Trainingswissen  

Um visuelle Überlastung zu reduzieren:
- TRAIN wird **standardmäßig unterdrückt**
- WEB/DOC werden angezeigt, wenn explizit bekannt
- Provenienz impliziert niemals Wahrheit oder Überzeugungskraft

---

## Darstellung und Farbkontrolle

- Darstellungssteuerungen sind **strikt getrennt** von der Governance-Logik.
- `Color on/off` ist der **nutzerseitige Rendering-Toggle** zum Anzeigen der Evidence Linker Zuverlässigkeitsklassen (🟢/🟡/🔴) und optionaler Provenienz-Suffixe (`DOC`/`WEB`/`TRAIN` wo zutreffend).
- Es **ändert nicht** die Evidence Linker-Semantik; es ändert nur, ob die Klassen gerendert werden.

### Standard
- Standardzustand: `Color on` (für alle Profile **außer** **Sandbox** und **Briefing**, wo es standardmäßig `Color off` ist)
- Wenn `Color on` aktiviert ist, kann das Modell Zuverlässigkeitsklassen als 🟢 / 🟡 / 🔴 rendern (und kann Provenienz-Suffixe wie `WEB` / `DOC` anzeigen, wenn zutreffend).

Farbe darf **niemals** zur Überzeugung, Zustimmung oder Präferenz verwendet werden.  
Sie darf nur **expliziten epistemischen Status** kodieren (z. B. Evidence Linker Klassen) oder **expliziten Systemzustand** (z. B. aktivierte/deaktivierte Flags).

---

## Selbst-Widerlegung (seit v19.5.0)

Jede Nicht-Sandbox-Antwort endet mit einem **Selbst-Widerlegungs-Block**:
- genau **2–3 Schwachstellen**
- keine neuen faktischen Behauptungen
- keine Tonabmilderung oder Überzeugung
- jeder Punkt enthält einen vorgeschlagenen nächsten Check

Platzierung:
- nach der endgültigen Antwort
- vor der QC-Fußzeile
- SCI-Spur bleibt immer **vor** der Antwort

Zweck: begrenzte epistemische Demut erzwingen.

---

## Sitzungsebene Drift-Schutz (v19.6.x)

### Anchor Snapshots

Um Instruktions-Drift in langen Konversationen abzumildern:
- periodische **Anchor Snapshots** fassen den aktuellen Zustand zusammen
- enthalten Version, Profil, SCI-Zustand, QC/CGI-Zustand
- **Häufigkeit erhöht**, um UX-Rauschen zu reduzieren
- **Nutzer-Opt-out verfügbar**

Dies ist ein Erinnerungsmechanismus, keine harte Garantie.

---

## Befehle (Überblick)

- Befehle werden **nur erkannt, wenn sie als eigenständige Prompts gesendet werden**.
- Befehlstokens sind **kanonisch nur auf Englisch**.
- Erklärende UI kann in der **Konversationssprache** gerendert werden.

### Befehle (Kurzreferenz)

**Primär**
- `Comm Start` — aktiviere das vollständige Comm-SCI-Regelsystem für diese Sitzung
- `Comm Stop` — deaktiviere Comm-SCI (Plattform-Standardverhalten; Safety Core bleibt aktiv)
- `Comm State` (Aliase: `Comm Status`) — zeige den aktuellen aktiven Zustand (Profil, SCI, QC/CGI-Ziele, Control Layer, Overlays)
- `Comm Config` (Aliase: `Config`) — drucke einen schreibgeschützten Rohe-Konfigurations-Snapshot
- `Comm Anchor` (Aliase: `Anchor`) — rendere einen Anchor Snapshot, um lange Sitzungen neu zu verankern, ohne den Zustand zu ändern
- `Comm Audit` — auditieren der letzten Assistant-Antworten auf Compliance und Abweichungen melden
- `Anchor auto off` — deaktiviere automatische Anchor Snapshot-Blöcke für die aktuelle Sitzung

**Profile**
- `Profile Standard` — wechsle zum Standard-Profil
- `Profile Expert` — wechsle zum Expert-Profil
- `Profile Sparring` — wechsle zum Sparring-Profil
- `Profile Briefing` — wechsle zum Briefing-Profil
- `Profile Sandbox` — wechsle zum Sandbox-Profil

**SCI**
- `SCI on` — aktiviere SCI-Auswahlmodus und zeige das SCI-Varianten-Menü (A–H) bei Bedarf
- `SCI off` — deaktiviere SCI/SCIplus-Workflows und kehre zum Standardverhalten des Profils zurück
- `SCI menu` — zeige das SCI-Varianten-Menü (A–H) erneut an
- `SCI recurse` — starte eine verschachtelte SCI/SCIplus-Tiefenanalyse für eine abgegrenzte Teilfrage

**Modus-Overlays**
- `Strict on` — aktiviere Strict Mode
- `Strict off` — deaktiviere Strict Mode
- `Explore on` — aktiviere Exploration Mode
- `Explore off` — deaktiviere Exploration Mode

**Dynamisch**
- `Dynamic one-shot on` — aktiviere Dynamic Prompting nur für die nächste Antwort (nicht-persistent)

**Rendering**
- `Color on` — aktiviere Evidence Linker Farbklassen-Tagging (GRÜN/GELB/ROT)
- `Color off` — deaktiviere Evidence Linker Farbklassen-Tagging und kehre zur Basisformatierung zurück

### Comm Hilfe
`Comm Help` zeigt **vollständige Dokumentation** an, beginnend mit einer kurzen **didaktischen Einführung**.  
Modelle sind explizit erlaubt, eine **geführte Erklärung** des Systems bereitzustellen, wenn Hilfe angefordert wird.

---

## Ethik & Verantwortung

- LLMs sind probabilistische Modelle, keine Agenten
- Verantwortung bleibt beim Menschen
- Transparenz geht vor Komfort oder Überzeugungskraft
- Unsicherheit muss **explizit gemacht**, nicht versteckt werden

---

## Zielgruppe

- Pädagogen und Lehrkräfte
- Wissenschaftliche und technische Fachleute
- Reflektierte Power-User von LLMs
- Jeder, der **Kontrolle über Bequemlichkeit** priorisiert

Nicht gedacht für:
- Gelegenheits-Chat
- Autonome Agenten
- Latenz-kritische Produktionssysteme

---

## ⚡ Schnellstart (minimal)

1. **Instanziieren:** Stellen Sie das kanonische JSON-Regelwerk bereit (als einzige aktive Governance-Spezifikation für die Sitzung).
2. **Aktivieren:** Senden Sie `Comm Start`.
3. **Konfigurieren (Beispiel):** Senden Sie `Profile Expert` und (optional) `Strict on`.
4. **Arbeiten:** Stellen Sie Ihre Frage. Für Tiefenanalysen nutzen Sie `SCI on` (wählen Sie eine Variante) und `SCI recurse`.

**Zu einem neuen Chat wechseln (Clean Reset):**  
`Comm Anchor` → kopieren Sie den **Anchor Snapshot** in den neuen Chat → instanziieren Sie das kanonische JSON-Regelwerk erneut → `Comm Start` → setzen Sie `Profile …` und Overlays/Modi.

> **Epistemischer Sicherheitshinweis:** Comm-SCI beseitigt keine Halluzinationen; es hilft, Unsicherheit und Verifizierungslücken **sichtbar** zu machen (z. B. über Evidence Linker Klassen, mit oder ohne Farbe).

---

## Praktische Nutzung

### Typischer Workflow
1. Stellen Sie das kanonische JSON-Regelwerk dem Modell bereit (als einzige aktive Governance-Spezifikation für die Sitzung).
2. Aktivieren Sie explizit mit `Comm Start`.
3. Wählen Sie ein Profil via `Profile …` und optionale Overlays (`Strict on/off`, `Explore on/off`).
4. Nutzen Sie SCI bewusst (`SCI on` → wählen Sie eine Variante; `SCI recurse` für abgegrenzte Tiefenanalysen).
5. In langen Sitzungen re-verankern mit `Comm Anchor` und nutzen Sie `Comm Audit`, wenn Sie Drift vermuten.

### Re-Initialisierung (neuer Chat / Clean Reset)
1. Führen Sie `Comm Anchor` aus, um einen **Anchor Snapshot** zu erstellen.
2. Kopieren Sie den **Anchor Snapshot** in die erste Nachricht des neuen Chats.
3. Stellen Sie das kanonische JSON-Regelwerk erneut bereit (als einzige aktive Governance-Spezifikation für diese Sitzung).
4. Führen Sie `Comm Start` aus, dann setzen Sie das gewünschte `Profile …` und alle Overlays/Modi (`Strict`, `Explore`, etc.).

---

## Versionierungsrichtlinie

- **19.4.x:** Kern-Governance (Profile, SCI, QC, Control Layer)
- **19.5.x:** Selbst-Widerlegung und Evidence Linker-Reifung
- **19.6.x:** Sitzungsebene Governance (Anker, Rekursives SCI, Provenienz, Audit)

Patch-Releases sind **additiv und abwärtskompatibel**.  
Breaking Changes sind Hauptversionen (20.x) vorbehalten.

---

## Status

- **Aktuelle stabile Version:** v19.6.3  
- **Stabilität:** produktionsreif (Governance-Spezifikation)  
- **Source of Truth:** kanonisches JSON-Regelwerk  

---

## Zitierung

Wenn Sie dieses Framework öffentlich nutzen (Papers, Blogposts, Vorträge), zitieren Sie bitte eine **archivierte Zenodo-Version**.
- DOI: https://doi.org/10.5281/zenodo.18072065

(Wenn Zenodo eine neuere Versions-DOI für die spezifische verwendete Version bereitstellt, bevorzugen Sie diese; die Konzept-DOI bleibt typischerweise stabil.)

---

## Lizenz

Creative Commons Attribution 4.0 International (CC BY 4.0)