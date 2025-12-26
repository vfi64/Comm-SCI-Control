# Comm-SCI-Control  
**Explizites Regelsystem für kontrollierte Mensch–KI-Interaktion**

Ein modellagnostischer Control- und Governance-Rahmen zur Reduktion von Drift, zur Sicherung von Transparenz und zur bewussten Aufrechterhaltung menschlicher Kontrolle über KI-Antworten.

---

## Motivation

Moderne Large Language Models liefern beeindruckende Ergebnisse — zugleich zeigen sie systemische Schwächen:

- inkonsistente Antworten über längere Gespräche hinweg,
- stille Anpassung des Antwortverhaltens,
- fehlende oder unklare Kennzeichnung von Unsicherheit,
- Qualität, die schwer zu verifizieren oder zu auditieren ist.

**Comm-SCI-Control** adressiert diese Probleme **nicht durch bessere Prompts**, sondern durch ein **explizites, transparentes Regelsystem**, das:

- Antwortqualität sichtbar macht,
- Denkprozesse strukturiert,
- menschliche Kontrolle erhält,
- und stille Re-Adaptation verhindert.

---

## Was dieses Regelsystem ist

Comm-SCI-Control ist:

- ein **rein textbasiertes Regelsystem** (kein Code, kein Plugin),
- **modellagnostisch** konzipiert (nutzbar mit mehreren Modellen; Compliance kann variieren),
- ein **externer Governance- und Kontrollrahmen** für KI-Interaktion,
- ein Werkzeug zur **Reduktion von Drift, Mehrdeutigkeit und nicht verifizierbarer Ausgabe**.

Es definiert unter anderem:

- **Profile** (Standard, Expert, Sparring, Briefing, Sandbox),
- **strukturierte Denkprozesse** (SCI mit auswählbaren Varianten),
- eine **explizite QC-Matrix** mit Abweichungsreporting (Δ),
- eine **harte Control Layer** gegen stille Adaption,
- **explizites Unsicherheits-Handling und Prüf-/Verifikationsrouten**,
- **deterministische Initialisierung und kanonische Zustandsdurchsetzung** (seit v19.4.21),
- **explizite Rendering-Kontrollen** (Color on/off, nicht-semantisch).

---

## Was dieses Regelsystem nicht ist

- ❌ kein autonom lernendes oder selbstoptimierendes System  
- ❌ kein Wrapper, keine API-Erweiterung, kein Plugin  
- ❌ keine Garantie für Korrektheit oder Wahrheit  
- ❌ kein Ersatz für menschliches Urteil oder Verantwortung  

**Kernaussage:**  
Das Regelsystem macht Fehler und Drift **sichtbar** — es eliminiert sie nicht.

---

## Kernkonzepte (Überblick)

### Profile

Profile definieren den **Kooperationsmodus** zwischen Mensch und KI  
(z. B. Alltag, Expertenanalyse, kritisches Sparring, Verdichtung, Exploration).

Profilwechsel sind **explizit und auditierbar**.  
Automatische oder erschlossene Profilwechsel sind verboten.

---

### SCI (Structured Cognitive Interaction)

Explizite Denkstruktur:

- **SCI:** Plan → Solution → Check  
- **Erweiterte Tiefe:** wählbar über ein SCI-Variantenmenü (A–H)

Wenn SCI aktiv ist:
- ist die **vollständige Reasoning-Trace verpflichtend**,
- stille Komprimierung oder Auslassung ist untersagt.

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

- eine **QC-Selbsteinschätzung**,
- ein **Delta (Δ)** als Abweichung vom Zielkorridor des aktiven Profils.

#### Delta-Semantik

- Δ < 0 → unter Ziel (potenzielles Qualitätsdefizit)  
- Δ = 0 → im Zielkorridor (akzeptabel)  
- Δ > 0 → über Ziel (Risiko von Überoptimierung, z. B. Halluzinationsrisiko bei zu viel „Evidenz“)

**Handlungsleitfaden:**

- |Δ| ≥ 2 → manuelle Nutzer-Korrektur empfohlen  
- |Δ| < 2 → nur Monitoring  

---

### Control Layer

Eine Meta-Ebene, die erzwingt:

- Regelkohärenz,
- Auditierbarkeit,
- Verhinderung stiller Verhaltensänderungen,
- strikte Trennung von Governance-Logik und Präsentation.

---

## Umgang mit Unsicherheit

Comm-SCI-Control nutzt eine **explizite Unsicherheits-Taxonomie**:

- **U1 – Datenlücke**
- **U2 – Logische Unterbestimmtheit**
- **U3 – Normative Uneinigkeit**
- **U4 – Zeitliche Instabilität**
- **U5 – Modelllimitierung**  
  Strukturelle Limitierung des LLM; die Aufgabe ist nicht zuverlässig lösbar.
- **U6 – Mehrdeutige Anfrage**  
  Eingabe ist unterbestimmt oder hat mehrere plausible Interpretationen.

Jedes Unsicherheitslabel erzwingt einen **erforderlichen nächsten Schritt**  
(z. B. Rückfrage, alternative Ansätze, Verifikationsrouten).

---

## Verifikationsdisziplin

- **Verification Route Gate:**  
  Starke Behauptungen benötigen mindestens eine explizite Route  
  (Messung, Quelle, Kontrast oder Web-Check).

- Behauptungen ohne gültige Route müssen **abgewertet und als unsicher markiert** werden.

- Evidenz-Scores werden **gedeckelt**, wenn Verifikation fehlt.

---

## Self-Debunking (seit v19.5.0)

Self-Debunking ist ein **strikter, stets aktiver (außer Sandbox) Post-Answer-Auditblock**:

- Wird **nach der finalen Antwort** und **vor dem QC-Footer** gerendert.
- **2–3 Bulletpoints**, fokussiert auf **Schwächen / Annahmen / fehlende Verifikation**.
- Darf **keine neuen Faktenbehauptungen einführen**.

Zweck: Blindstellen reduzieren, indem eine kurze, begrenzte Selbstkritik erzwungen wird — ohne die Governance-Logik zu verändern.

---

## Evidence Linker (seit v19.4.18; Defaults geändert in v19.5.1 / v19.5.2)

Evidence Linker ist ein **3-Klassen, rein präsentationsbezogenes Reliability-Tagging**:
`[GREEN]` / `[YELLOW]` / `[RED]` (optional mit 🟢/🟡/🔴).

- Es signalisiert **Verifikationsstärke**, nicht „Wahrheit“, „Zustimmung“ oder Überredung.
- Es darf niemals die Control-Layer-Semantik, QC-Delta-Regeln oder Command-Auflösung verändern.

### Defaults
- **v19.5.1:** default-on für alle Profile **außer Sandbox**.
- **v19.5.2:** default-off für **Briefing** (Sandbox bleibt ausgeschlossen); Default bleibt für andere Profile on.

---

## Rendering- und Farbkontrolle (seit v19.4.21)

- Rendering-Features sind **explizit** von der Governance-Logik getrennt.
- `Color on/off` ist **ausschließlich** ein Präsentations-Layer-Schalter.

### Zweck von `Color on`

- Verbessert **Lesbarkeit und Orientierung** bei kognitiv dichten Ausgaben.
- Hebt **nur strukturelle, zustandsbezogene oder diagnostische Elemente** hervor.

### Erlaubte Farbkategorien

Wenn `Color on` aktiviert ist, sind **genau drei Kategorien** erlaubt:

- **Neutral / Structural Color**  
  Strukturelle Trennung (Überschriften, Tabellen, Abschnitte).

- **State / Status Color**  
  Explizite Systemzustände (Profil, SCI on/off, Color on/off).

- **Attention / Diagnostic Color**  
  Governance-relevante Hinweise (Unsicherheit, Loop-Warnungen, Verifikationspflicht).

Farbe darf **niemals** Korrektheit, Qualität, Zustimmung, Überredung oder Präferenz kodieren.

Default: `Color off`.

---

## Commands (Schnellreferenz)

**Wichtig:** Commands werden **nur erkannt, wenn sie als alleiniger Prompt** gesendet werden.

- `Comm Start` / `Comm Stop`
- `Comm Status` / `Comm Help`
- `Profile Standard | Expert | Sparring | Briefing | Sandbox`
- `SCI on` / `SCI off`
- `Strict on` / `Strict off`
- `Explore on` / `Explore off`
- `Dynamic one-shot on`
- `Color on` / `Color off`

Command-Tokens sind **kanonisch nur Englisch**.  
Gerenderte Erklärungen können lokalisiert werden.

---

## Ethik & Verantwortung

Ethik wird **technisch, nicht rhetorisch** umgesetzt:

- LLMs sind probabilistische Modelle, keine Agenten.
- Verantwortung bleibt immer beim Menschen.
- Transparenz und Verifizierbarkeit stehen über Komfort oder Überredung.
- Unsicherheit muss **explizit** gemacht werden, nicht versteckt.

---

## Praktische Nutzung

Typischer Workflow:

1. Das **kanonische JSON-Regelwerk** dem LLM geben.
2. Zu Gesprächsbeginn explizit aktivieren.
3. In langen Sessions bewusst re-initialisieren.
4. Verhalten **intentional steuern — niemals implizit**.

---

## Zielgruppe

- Lehrkräfte und Pädagog:innen
- technische und naturwissenschaftliche Professionals
- reflektierte Power-User von LLMs
- alle, die **Kontrolle vor Bequemlichkeit** priorisieren

---

## Status

- **Aktuelle Version:** v19.5.2  
- **Stabilität:** stable / production-ready  
- **Source of Truth:** kanonisches JSON-Regelwerk  
  (README ist beschreibend, nicht normativ)

**Aktueller Fokus:**  
Dokumentation, Beispiele, Usability, Evaluation, Auditierbarkeit.

---

## Zitation

Wenn du dieses Framework verwendest, zitiere bitte das archivierte Zenodo-Release:  
https://doi.org/10.5281/zenodo.18047859

---

## Lizenz

Creative Commons Attribution 4.0 International (CC BY 4.0)  
https://creativecommons.org/licenses/by/4.0/
