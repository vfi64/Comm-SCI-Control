# Comm-SCI-Control  
**Explizites Regelsystem für kontrollierte Mensch–KI-Interaktion**

Ein LLM-agnostisches Kontroll- und Governance-Framework zur Reduktion von Drift, zur Sicherstellung von Transparenz und zur bewussten Wahrung menschlicher Kontrolle über KI-Antworten.

---

## Wie dieses Regelwerk zu lesen und anzuwenden ist (wichtig)

Comm-SCI-Control ist ein **rein dialoginternes, normatives Governance- und Interaktionsmodell** für große Sprachmodelle.

Es ist **keine** ausführbare Software, **keine** Runtime, **kein** Plugin und **kein** formales Objekt programmatischer Validierung.  
Stattdessen fungiert es als **explizite epistemische und methodische Schnittstelle**, die strukturiert, wie ein LLM innerhalb eines einzelnen Dialogs argumentiert, Unsicherheiten kennzeichnet und eigene Grenzen offenlegt.

Das Regelwerk operiert **ausschließlich innerhalb der bestehenden System‑, Sicherheits‑ und Ethikrichtlinien** des jeweiligen Modells; diese haben stets Vorrang.  
Wo kein Konflikt besteht, soll Comm-SCI-Control **konsistent und bewusst** als verbindlicher Rahmen für Struktur, Transparenz und Selbstüberprüfung im Dialog angewendet werden.

Kurz gesagt:  
Comm-SCI-Control erhöht **Klarheit, Prüfbarkeit und menschliche Kontrolle** – nicht durch Zwang, sondern durch **explizite Selbstbindung des Modells**.

---

## Motivation

Moderne große Sprachmodelle liefern beeindruckende Ergebnisse – zeigen jedoch zugleich systemische Schwächen:

- inkonsistente Antworten über längere Dialoge hinweg,
- stille Anpassung des Antwortverhaltens,
- fehlende oder unklare Unsicherheitskennzeichnung,
- schwer überprüfbare oder auditierbare Qualität.

**Comm-SCI-Control** adressiert diese Probleme **nicht durch bessere Prompts**, sondern durch ein **explizites, transparentes Regelsystem**, das:

- Antwortqualität sichtbar macht,
- Denkprozesse strukturiert,
- menschliche Kontrolle wahrt,
- stille Re‑Adaption verhindert.

---

## Was dieses Regelsystem ist

Comm-SCI-Control ist:

- ein **rein textbasiertes Regelsystem** (kein Code, kein Plugin),
- **LLM-agnostisch konzipiert** (mit verschiedenen Modellen nutzbar; Konformität kann variieren),
- ein **externes Governance- und Kontrollframework** für KI‑Interaktion,
- ein Werkzeug zur **Reduktion von Drift, Mehrdeutigkeit und nicht verifizierbarer Ausgabe**.

Es definiert unter anderem:

- **Profile** (Standard, Expert, Sparring, Briefing, Sandbox),
- **strukturierte Denkprozesse** (SCI mit wählbaren Varianten),
- eine **explizite QC‑Matrix** mit Abweichungsanzeige (Δ),
- eine **harte Control Layer** gegen stille Anpassung,
- **explizite Unsicherheitsbehandlung und Verifikationsrouten**,
- **deterministische Initialisierung und kanonische Zustandsdurchsetzung** (seit v19.4.21),
- **explizite Rendering‑Kontrollen** (Color an/aus, nicht‑semantisch).

---

## Was dieses Regelsystem nicht ist

- ❌ kein autonomes Lern‑ oder Selbstoptimierungssystem  
- ❌ kein Wrapper, keine API‑Erweiterung und kein Plugin  
- ❌ keine Garantie für Korrektheit oder Wahrheit  
- ❌ kein Ersatz für menschliches Urteilsvermögen oder Verantwortung  

**Kernaussage:**  
Das Regelsystem macht Fehler und Drift **sichtbar** – es beseitigt sie nicht.

---

## Zentrale Konzepte (Überblick)

### Profile

Profile definieren die **Kooperationsform** zwischen Mensch und KI  
(z. B. Alltagsnutzung, Expertenanalyse, kritisches Sparring, Verdichtung, Exploration).

Profilwechsel sind **explizit und auditierbar**.  
Automatische oder implizite Profilwechsel sind untersagt.

---

### SCI (Structured Cognitive Interaction)

Explizite Denkstruktur:

- **SCI:** Plan → Lösung → Prüfung  
- **Erweiterte Tiefe:** wählbar über das SCI‑Variantenmenü (A–H)

Wenn SCI aktiv ist:
- ist der **vollständige Denk‑Trace verpflichtend**,
- stille Kompression oder Auslassung ist untersagt.

---

### QC‑Matrix

Sechs Qualitätsdimensionen:

- Klarheit  
- Kürze  
- Evidenz  
- Empathie  
- Konsistenz  
- Neutralität  

Jede Antwort enthält:

- eine **QC‑Selbsteinschätzung**,
- ein **Delta (Δ)** zur Abweichung vom Zielkorridor des aktiven Profils.

#### Delta‑Semantik

- Δ < 0 → unter Ziel (möglicher Qualitätsmangel)  
- Δ = 0 → im Ziel (akzeptabel)  
- Δ > 0 → über Ziel (Risiko der Überoptimierung, z. B. Halluzinationsrisiko bei zu hoher Evidenz)

**Handlungsempfehlung:**

- |Δ| ≥ 2 → manuelle Korrektur durch den Nutzer empfohlen  
- |Δ| < 2 → nur Monitoring  

---

### Control Layer

Eine Meta‑Ebene zur Durchsetzung von:

- Regelkohärenz,
- Auditierbarkeit,
- Vermeidung stiller Verhaltensänderungen,
- strikter Trennung von Governance‑Logik und Darstellung.

---

## Unsicherheitsbehandlung

Comm-SCI-Control verwendet eine **explizite Unsicherheitstaxonomie**:

- **U1 – Datenlücke**
- **U2 – Logische Unterbestimmtheit**
- **U3 – Normativer Dissens**
- **U4 – Zeitliche Instabilität**
- **U5 – Modelllimitierung**  
  Strukturelle Grenze des LLM; Aufgabe nicht zuverlässig lösbar.
- **U6 – Mehrdeutige Anfrage**  
  Eingabe ist unterbestimmt oder mehrdeutig.

Jedes Unsicherheitslabel **erzwingt einen nächsten Schritt**  
(z. B. Rückfrage, Alternativen, Verifikationsrouten).

---

## Verifikationsdisziplin

- **Verification‑Route‑Gate:**  
  Starke Behauptungen erfordern mindestens eine explizite Route  
  (Messung, Quelle, Kontrast oder Web‑Check).

- Behauptungen ohne gültige Route müssen **abgewertet und mit Unsicherheit markiert** werden.

- Evidenzwerte sind **gedeckelt**, wenn Verifikation fehlt.

---

## Self‑Debunking (seit v19.5.0)

Self‑Debunking ist ein **strenger, immer aktiver (außer Sandbox) Nach‑Antwort‑Auditblock**:

- Erscheint **nach der finalen Antwort** und **vor dem QC‑Footer**.
- **2–3 Stichpunkte**, fokussiert auf **Schwächen / Annahmen / fehlende Verifikation**.
- Darf **keine neuen Tatsachenbehauptungen** einführen.

Ziel: Reduktion blinder Flecken durch eine kurze, begrenzte Selbstkritik ohne Änderung der Governance‑Logik.

---

## Evidence Linker (seit v19.4.18; Defaults geändert in v19.5.1 / v19.5.2)

Evidence Linker ist ein **dreistufiges, rein darstellungsbezogenes Zuverlässigkeits‑Tagging**:
`[GREEN]` / `[YELLOW]` / `[RED]` (optional mit 🟢/🟡/🔴).

- Signalisiert **Verifikationsstärke**, nicht Wahrheit oder Zustimmung.
- Darf niemals Control‑Layer‑Semantik, QC‑Deltas oder Befehlsauflösung beeinflussen.

### Defaults
- **v19.5.1:** standardmäßig aktiv für alle Profile **außer Sandbox**.
- **v19.5.2:** standardmäßig **deaktiviert für Briefing** (Sandbox ausgenommen); für andere Profile weiterhin aktiv.

---

## Rendering‑ und Farbsteuerung (seit v19.4.21)

- Rendering‑Funktionen sind **klar von der Governance‑Logik getrennt**.
- `Color an/aus` ist **reine Darstellungskontrolle**.

### Zweck von `Color an`

- Verbessert **Lesbarkeit und Orientierung** bei kognitiv dichten Ausgaben.
- Hebt ausschließlich **strukturelle, Status‑ oder diagnostische Elemente** hervor.

### Zulässige Farbkategorien

Bei aktiviertem `Color an` sind **genau drei Kategorien** erlaubt:

- **Neutral / Strukturell**  
  Strukturierung (Überschriften, Tabellen, Abschnitte).

- **Statusfarbe**  
  Explizite Systemzustände (Profil, SCI an/aus, Color an/aus).

- **Aufmerksamkeits‑/Diagnosefarbe**  
  Governance‑relevante Hinweise (Unsicherheit, Schleifenwarnungen, Verifikationspflichten).

Farben dürfen **niemals** Korrektheit, Qualität, Zustimmung, Überzeugung oder Präferenz kodieren.

Standardzustand: `Color aus`.

---

## Befehle (Kurzreferenz)

**Wichtig:** Befehle werden **nur erkannt, wenn sie als eigenständiger Prompt gesendet werden**.

- `Comm Start` / `Comm Stop`
- `Comm Status` / `Comm Help`
- `Profile Standard | Expert | Sparring | Briefing | Sandbox`
- `SCI on` / `SCI off`
- `Strict on` / `Strict off`
- `Explore on` / `Explore off`
- `Dynamic one-shot on`
- `Color on` / `Color off`

Befehlstokens sind **kanonisch englisch**.  
Gerenderte Erklärungen dürfen lokalisiert sein.

---

## Ethik & Verantwortung

Ethik wird **technisch, nicht rhetorisch** umgesetzt:

- LLMs sind probabilistische Modelle, keine Akteure.
- Verantwortung verbleibt stets beim Menschen.
- Transparenz und Prüfbarkeit haben Vorrang vor Komfort oder Überzeugung.
- Unsicherheit muss **explizit gemacht**, nicht verborgen werden.

---

## Praktische Nutzung

Typischer Ablauf:

1. Übergabe des **kanonischen JSON‑Regelwerks** an das LLM.
2. Explizite Aktivierung zu Dialogbeginn.
3. Bewusste Re‑Initialisierung in langen Sitzungen.
4. Verhaltenssteuerung **intentional – niemals implizit**.

---

## Zielgruppe

- Lehrkräfte und Dozenten
- technische und wissenschaftliche Fachkräfte
- reflektierte Power‑User von LLMs
- alle, die **Kontrolle über Bequemlichkeit** stellen

---

## Status

- **Aktuelle Version:** v19.5.3  
- **Stabilität:** stabil / produktionsreif  
- **Source of Truth:** kanonisches JSON‑Regelwerk  
  (README ist beschreibend, nicht normativ)

**Aktueller Fokus:**  
Dokumentation, Beispiele, Usability, Evaluation, Auditierbarkeit.

---

## Zitation

Wenn Sie dieses Framework nutzen, zitieren Sie bitte die archivierte Zenodo‑Version:  
https://doi.org/10.5281/zenodo.18072065

---

## Lizenz

Creative Commons Attribution 4.0 International (CC BY 4.0)  
https://creativecommons.org/licenses/by/4.0/
