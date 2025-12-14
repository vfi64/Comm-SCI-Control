# Comm-SCI-Control  
**Explizites Regelwerk zur kontrollierten Mensch–KI-Interaktion**

> Ein LLM-agnostisches Steuerungs- und Governance-Regelwerk zur Reduktion von Drift, zur Sicherung von Transparenz und zur bewussten Beherrschbarkeit von KI-Antworten.

---

## Motivation

Moderne Large Language Models liefern beeindruckende Antworten –  
gleichzeitig zeigen sie systemische Schwächen:

- inkonsistente Antworten über längere Chats,
- stilles Anpassen des Antwortverhaltens,
- fehlende Unsicherheitsmarkierung,
- schwer überprüfbare Qualität.

**Comm-SCI-Control** adressiert diese Probleme **nicht durch bessere Prompts**,  
sondern durch ein **explizites, transparentes Regelwerk**, das:

- Antwortqualität sichtbar macht,
- Denkprozesse strukturiert,
- menschliche Kontrolle erhält,
- und stilles Umlernen verhindert.

---

## Was dieses Regelwerk ist

Comm-SCI-Control ist:

- ein **rein textbasiertes Regelwerk** (kein Code, kein Plugin),
- **LLM-agnostisch** (getestet u. a. mit ChatGPT, Gemini, Mistral, Claude, DeepSeek),
- ein **externer Steuerungsrahmen** für KI-Interaktion,
- ein Werkzeug zur **Reduktion von Reibung, Drift und Fehlinterpretation**.

Es definiert u. a.:

- Profile (Standard, Expert, Sparring, Briefing, Sandbox),
- strukturierte Denkprozesse (SCI, SCIplus),
- eine explizite QC-Matrix (inkl. Abweichungsreporting),
- einen Control Layer gegen stille Adaption,
- optionale, aber kontrollierte Erweiterungen (CGI, Trade-Off-Guard).

---

## Was dieses Regelwerk **nicht** ist

- ❌ kein autonomes Lern- oder Selbstoptimierungssystem  
- ❌ kein Wrapper, keine API-Erweiterung, kein Plugin  
- ❌ kein Garant für „wahre“ oder „richtige“ Antworten  
- ❌ kein Ersatz für menschliches Urteil oder Verantwortung  

> **Kernsatz:**  
> *Das Regelwerk macht Fehler sichtbarer – es eliminiert sie nicht.*

---

## Zentrale Konzepte (Kurzüberblick)

### Profile
Definieren den **Kooperationsmodus** zwischen Mensch und KI  
(z. B. Alltag, Fachexpertise, Sparring, Verdichtung, Exploration).

### SCI / SCIplus
Explizite Denkstruktur:
- **SCI:** Plan → Lösung → Check  
- **SCIplus:** erweiterte dialektische Prüfung (Many-Lenses-Ansatz)

### QC-Matrix
Sechs Qualitätsdimensionen:
- Klarheit
- Kürze
- Evidenz
- Empathie
- Konsistenz
- Neutralität  

Jede Antwort enthält:
- aktuelle QC-Bewertung,
- eine geschätzte Abweichung (Δ) vom Profilziel.

### Control Layer
Meta-Schicht zur Sicherung von:
- Regelkohärenz,
- Drift-Erkennung,
- Schutz vor stiller Verhaltensänderung.

---

## Ethik & Verantwortung (explizit)

Comm-SCI-Control versteht **Ethik nicht als Zusatz**,  
sondern als **funktionalen Bestandteil der Steuerlogik**.

### Grundannahmen

- LLMs sind **probabilistische Textmodelle**, keine intentionalen Akteure.
- Verantwortung verbleibt **immer beim Menschen**.
- Komfort, Geschwindigkeit oder Überzeugungskraft dürfen  
  **nicht über Transparenz und Prüfbarkeit gestellt werden**.

### Operative Ethik im Regelwerk

Ethik wird nicht moralisch, sondern **technisch** umgesetzt durch:

- **Safety Core:** Keine Schädigungshilfe, klare Grenzen, Transparenz.
- **Unsicherheitsklassifikation (U1–U4):**  
  Unwissen wird explizit markiert – nicht kaschiert.
- **QC-Dimension „Neutralität“:**  
  Trennung von Fakten und Wertungen, Gegenperspektiven bei Bedarf.
- **Deaktiviertes Dynamic Prompting (Default):**  
  Keine automatische Verhaltenskorrektur ohne Nutzerentscheidung.

> Ziel ist **Autonomieerhalt**, nicht Optimierung um jeden Preis.

---

## Nutzung in der Praxis

Comm-SCI-Control wird typischerweise:

1. als vollständiges JSON-Regelwerk in einen Chat eingebracht,
2. zu Beginn eines neuen Chats explizit aktiviert,
3. bei langen Dialogen bewusst re-initialisiert (Reset),
4. nicht automatisch, sondern **absichtlich** gesteuert.

---

## Zielgruppe

- Lehrkräfte & Didaktiker
- technisch-wissenschaftlich Arbeitende
- reflektierte Power-User von LLMs
- Menschen, die **Beherrschbarkeit über Bequemlichkeit** stellen

---

## Status

- Aktuelle Version: **v19.0.3**
- Entwicklungsstand: **stabil, produktiv einsetzbar**
- Fokus weiterer Arbeit: Dokumentation, Beispiele, Usability, Evalution

---

## 📘 Zitation

Wenn Sie dieses Regelwerk verwenden, zitieren Sie bitte die archivierte Version auf Zenodo:
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17930749.svg)](https://doi.org/10.5281/zenodo.17930749)
**DOI:** [10.5281/zenodo.17930749](https://doi.org/10.5281/zenodo.17930749)

---

## Lizenz

Dieses Werk ist lizenziert unter der  
**Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

https://creativecommons.org/licenses/by/4.0/
