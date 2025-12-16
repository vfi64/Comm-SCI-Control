# Comm-SCI-Control
**Explizites Regelsystem für kontrollierte Mensch–KI-Interaktion**

> Ein LLM-agnostisches Kontroll- und Governance-Framework zur Reduzierung von Drift, Gewährleistung von Transparenz und Aufrechterhaltung der bewussten menschlichen Kontrolle über KI-Antworten.

---

## Motivation

Moderne Large Language Models liefern beeindruckende Ergebnisse –
gleichzeitig weisen sie systemische Schwächen auf:

- inkonsistente Antworten über längere Konversationen,
- stillschweigende Anpassung des Antwortverhaltens (Drift),
- fehlende oder unklare Unsicherheitssignalisierung,
- schwer überprüfbare Qualität.

**Comm-SCI-Control** begegnet diesen Problemen **nicht durch bessere Prompts**,
sondern durch ein **explizites, transparentes Regelsystem**, das:

- die Antwortqualität sichtbar macht,
- Denkprozesse strukturiert,
- die menschliche Kontrolle wahrt,
- und stilles Umlernen verhindert.

---

## Was dieses Regelsystem ist

Comm-SCI-Control ist:

- ein **rein textbasiertes Regelsystem** (kein Code, kein Plugin),
- **LLM-agnostisch** (getestet u. a. mit ChatGPT, Gemini, Mistral, Claude, DeepSeek),
- ein **externes Kontroll-Framework** für KI-Interaktion,
- ein Werkzeug zur **Reduzierung von Reibung, Drift und Fehlinterpretationen**.

Es definiert unter anderem:

- Profile (Standard, Expert, Sparring, Briefing, Sandbox),
- strukturierte Denkprozesse (SCI, SCIplus),
- eine explizite QC-Matrix (inkl. Abweichungs-Reporting),
- einen Control Layer gegen stilles Umlernen,
- optionale, aber kontrollierte Erweiterungen (CGI, Trade-Off Guard).

---

## Was dieses Regelsystem **nicht** ist

- ❌ kein autonomes Lern- oder Selbstoptimierungssystem
- ❌ kein Wrapper, keine API-Erweiterung oder Plugin
- ❌ keine Garantie für „wahre“ oder „korrekte“ Antworten
- ❌ kein Ersatz für menschliches Urteilsvermögen oder Verantwortung

> **Kernaussage:**
> *Das Regelsystem macht Fehler sichtbarer — es eliminiert sie nicht.*

---

## Kernkonzepte (Kurzübersicht)

### Profile
Definieren den **Modus der Kooperation** zwischen Mensch und KI
(z. B. Alltagsnutzung, Expertenanalyse, Sparring, Kondensation, Exploration).

### SCI / SCIplus
Explizite Denkstruktur:
- **SCI:** Plan → Lösung → Check
- **SCIplus:** erweiterte dialektische Prüfung (Many-Lenses-Ansatz)

### QC Matrix
Sechs Qualitätsdimensionen:
- Klarheit
- Kürze
- Evidenz
- Empathie
- Konsistenz
- Neutralität

Jede Antwort beinhaltet:
- eine aktuelle QC-Bewertung,
- eine geschätzte Abweichung (Δ) vom Profil-Ziel.

### Control Layer
Meta-Schicht zur Sicherstellung von:
- Regelkohärenz,
- Drift-Erkennung,
- Schutz vor stillschweigender Verhaltensänderung.

---

## Neue Features in v19.x

**Gegenüber v19.0.3:** v19.1.x ergänzt *Prüfroute-Gate*, *Evidence Cap* und *Discursive Loop Guard*; v19.2.0 ergänzt *Web-Check Hook* und *Source-first Hard-Mode*.


Die folgenden funktionalen Regeln erhöhen die **Überprüfbarkeit** und die **strukturelle Integrität**, insbesondere bei zeitkritischen oder hochspekulativen Behauptungen:

### Überprüfungsrouten (Verification Routes)
* **Prüfroute-Gate (Verification Route Gate) (v19.1.x):** Erzwingt für starke Behauptungen mindestens eine explizite Verifizierungsroute (Messung, Quelle, Kontrast oder **Web-Check**).
* **Evidence Cap Rules:** Wird eine starke Behauptung ohne erfolgreiche Verifizierungsroute aufgestellt, wird der QC-Score für **Evidenz** auf maximal 2 begrenzt, um übertriebene Sicherheit zu verhindern.

### Reibung und Stabilität
* **Web-Check Hook (v19.2.0):** Formalisierter Mechanismus für kritische, zeitlich instabile Fakten (Unsicherheit U4). Diese Aktion wird vom System als „externe Reibung“ registriert.
* **Source-First Hard-Mode (v19.2.0):** Bei News-ähnlichen oder instabilen Claims (U4) sind harte, faktische Aussagen ohne Quelle oder Web-Check nicht zulässig. Die Behauptung wird stattdessen zur Hypothese degradiert oder klassifiziert.

### Schleifenschutz (Loop Prevention)
* **Discursive Loop Guard (v19.1.x):** Gibt eine Warnung aus, wenn die Interaktion eine definierte Schwelle (>3 Turns) ohne neue externe Reibung (Messung/Quelle/Kontrast/Web Check) überschreitet, um argumentative Schleifen zu vermeiden.

---


### Kommandos (Kurzreferenz)
- **Comm Start**: Regelwerk aktivieren.
- **Comm Stop**: Regelwerk deaktivieren.
- **Comm Status**: Status anzeigen (einzige Ausnahme, darf auch nicht-standalone vorkommen).
- **Comm Codes**: Code-/Optionentabelle anzeigen.
- **Comm Regeln aus**: Spielmodus (Comm-Regeln ignorieren; Sicherheitsrahmen bleibt).
- **Comm Regeln an**: Rückkehr in den Regelbetrieb.

## Ethik & Verantwortung (explizit)

Comm-SCI-Control behandelt **Ethik nicht als Add-on**,
sondern als **funktionalen Bestandteil der Kontrolllogik**.

### Kernannahmen

- LLMs sind **probabilistische Textmodelle**, keine intentionellen Akteure.
- Die Verantwortung **verbleibt immer beim Menschen**.
- Komfort, Geschwindigkeit oder Überzeugungskraft dürfen **niemals Transparenz und Überprüfbarkeit** außer Kraft setzen.

### Operative Ethik im Regelsystem

Ethik wird nicht moralisch, sondern **technisch** umgesetzt, durch:

- **Safety Core:** keine Assistenz bei Schaden, klare Grenzen, Transparenz.
- **Unsicherheitsklassifizierung (U1–U4):**
  Unwissenheit wird explizit markiert — nicht verschleiert.
- **QC-Dimension „Neutralität“:**
  Trennung von Fakten und Werturteilen, Gegenperspektiven, wo angebracht.
- **Deaktiviertes Dynamic Prompting (Default):**
  keine automatische Verhaltenskorrektur ohne explizite menschliche Entscheidung.

> Das Ziel ist **Autonomieerhalt**, nicht Optimierung um jeden Preis.

---

## Praktische Anwendung

Comm-SCI-Control wird typischerweise wie folgt angewendet:

1. als vollständiges JSON-Regelwerk in einen Chat eingeführt,
2. explizit zu Beginn einer neuen Konversation aktiviert,
3. in längeren Dialogen bewusst re-initialisiert (resetet),
4. intentional, statt automatisch gesteuert.

---

## Zielgruppe

- Lehrende und Pädagogen
- Fachkräfte in technischen und wissenschaftlichen Domänen
- reflektierte Power-User von LLMs
- Menschen, die **Kontrollierbarkeit über Bequemlichkeit** stellen

---

## Status

- Aktuelle Version: **v19.2.0**
- Entwicklungsstatus: **stabil, produktionsreif**
- Aktueller Fokus: Dokumentation, Beispiele, Usability, Evaluation

---

## Zitierung · Citation

Wenn Sie dieses Framework nutzen, zitieren Sie bitte die archivierte Version auf Zenodo:
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17930749.svg)](https://doi.org/10.5281/zenodo.17930749)
**DOI:** [10.5281/zenodo.17930749](https://doi.org/10.5281/zenodo.17930749)

---

## Lizenz

Dieses Werk ist lizenziert unter der
**Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

https://creativecommons.org/licenses/by/4.0/