# Comm-SCI-Control
**Explizites Regelsystem für kontrollierte Mensch–KI-Interaktion**

> Ein LLM-agnostisches Kontroll- und Governance-Framework zur Reduktion von Drift, zur Sicherung von Transparenz und zur bewussten Beherrschbarkeit von KI-Antworten.

---

## Motivation

Moderne Large Language Models liefern beeindruckende Ergebnisse —
gleichzeitig zeigen sie systemische Schwächen:

- inkonsistente Antworten über längere Konversationen,
- stillschweigende Anpassung des Antwortverhaltens,
- fehlende oder unklare Unsicherheitskennzeichnung,
- Qualität, die schwer zu verifizieren ist.

**Comm-SCI-Control** adressiert diese Probleme **nicht durch bessere Prompts**,
sondern durch ein **explizites, transparentes Regelsystem**, das:

- Antwortqualität sichtbar macht,
- Denk- und Begründungsprozesse strukturiert,
- menschliche Kontrolle erhält,
- und stille Re‑Adaption reduziert.

---

## Was dieses Regelsystem ist

Comm-SCI-Control ist:

- ein **rein textbasiertes Regelsystem** (kein Code, kein Plugin),
- **LLM-agnostisch** (mit mehreren LLMs nutzbar; Verhalten hängt von Modell-Compliance ab),
- ein **externes Kontroll-Framework** für KI-Interaktion,
- ein Werkzeug zur **Reduktion von Reibung, Drift und Fehlinterpretation**.

Es definiert u. a.:

- Profile (Standard, Expert, Sparring, Briefing, Sandbox),
- strukturierte Denk-/Begründungsprozesse (SCI; erweiterte dialektische Tiefe über Variantenwahl – früher „SCIplus“ genannt),
- eine explizite QC-Matrix (inkl. Abweichungsreporting),
- einen Control Layer gegen stille Verhaltensänderung,
- optionale, aber kontrollierte Erweiterungen (CGI, Trade-Off Guard).

---

## Was dieses Regelsystem **nicht** ist

- ❌ kein autonomes Lern- oder Selbstoptimierungssystem
- ❌ kein Wrapper, keine API-Erweiterung und kein Plugin
- ❌ keine Garantie für „wahre“ oder „korrekte“ Antworten
- ❌ kein Ersatz für menschliches Urteilsvermögen oder Verantwortung

> **Kernaussage:**
> *Das Regelsystem kann Fehler und Drift sichtbarer machen — es eliminiert sie nicht.*

---

## Kernkonzepte (Kurzübersicht)

### Profile
Profile definieren den **Kooperationsmodus** zwischen Mensch und KI
(z. B. Alltagsnutzung, Expertenanalyse, Sparring, Verdichtung, Exploration).

### SCI (mit Varianten; früheres „SCIplus“ über Variantenwahl)
Explizite Begründungsstruktur:
- **SCI:** Plan → Solution → Check.
- **Erweiterte dialektische Tiefe (früher „SCIplus“):** wird über **SCI on** plus anschließende Variantenwahl im A–H‑Menü aktiviert (z. B. Deep‑Dive/Dialectics++).

### QC-Matrix
Sechs Qualitätsdimensionen:
- Klarheit
- Kürze
- Evidenz
- Empathie
- Konsistenz
- Neutralität

Jede Antwort enthält:
- eine aktuelle QC-Einschätzung,
- eine geschätzte Abweichung (Δ) vom Profil-Ziel.

### Control Layer
Meta-Ebene zur Sicherung von:
- Regelkohärenz,
- Drift-Erkennung,
- Schutz vor stiller Verhaltensänderung.

---

## Neue Funktionen in v19.x

Die v19‑Linie fokussiert **Verifizierbarkeit**, **Drift-Kontrolle** und **Auditierbarkeit** — ohne Korrektheit zu versprechen.

### Verifikation und Evidenz-Disziplin
- **Verification Route Gate (v19.1.x):** starke Behauptungen benötigen mindestens eine explizite Verifikationsroute (Messung / Quelle / Kontrast / Web‑Check).
- **Evidenz‑Cap‑Regeln (v19.1.x+):** wenn eine starke Behauptung ohne erfolgreiche Verifikationsroute erfolgt, darf die Evidenz nicht als „3“ ausgewiesen werden.

### Stabilität bei zeitinstabilen Themen
- **Web‑Check‑Hook + Source‑first Hard‑Mode (v19.2.0):** bei zeitinstabilen oder news‑artigen Behauptungen (U4) erfordern harte Fakten eine Quelle oder einen Web/Live‑Check; andernfalls müssen sie downgraded und markiert werden.

### Auditability-Härtung (v19.4.x)
- **SCI‑Trace‑Enforcement (v19.4.2):** wenn SCI aktiv ist, ist eine sichtbare Schritt‑Trace verpflichtend (keine stille Kompression/kein Weglassen).
- **SCI‑Variant‑Menü‑Enforcement (v19.4.3):** wenn die SCI‑Auswahl pending ist, verlangt das Regelsystem, dass das A–H‑Menü gerendert wird (kein stilles Weglassen; Auslassungen sollten repariert/markiert werden).
- **Dialogsprache für UI‑Texte (v19.4.4):** Erklär-/Help-/Status-/Fehler-/Menü‑Text muss in der aktuellen Dialogsprache gerendert werden (wenn unterstützt); Command‑Tokens bleiben kanonisch Englisch.
- **Comm‑Start‑Initialisierungs‑Guard (v19.4.6):** verhindert inferierte Profilwechsel bei Aktivierung; Profilwechsel erfordern explizite Standalone‑Kommandos.
- **Edge‑Case‑Patches (v19.4.7):** CSC‑Refinement‑Marker muss bei Anwendung für den Nutzer sichtbar sein; der Discursive‑Loop‑Guard erzwingt nach 3 Zügen ohne externe Reibung einen markierten Hypothetical‑Analysis‑Exit (wenn kein Web/Live‑Check verfügbar ist); Translation‑Gap U1 triggert eine kurze zweisprachige Key‑Point‑Summary; die SCI‑Variantenwahl kann bei kontextuellen SCI‑Methodikfragen einen zusätzlichen Zug pending bleiben.

---

## Kommandos (Kurzübersicht)

**Wichtig:** Kommandos werden **nur** erkannt, wenn sie als **Standalone‑Prompt** gesendet werden (eine Zeile, nichts anderes).

- **Comm Start**: Regelsystem aktivieren (Default‑Profil initialisieren).
- **Comm Stop**: Regelsystem deaktivieren.
- **Comm Status** *(Alias: Comm State)*: aktuellen Status anzeigen.
- **Comm Config** *(Alias: Config)*: kompakte Konfigurationssicht (für Audits/Debugging).
- **Comm Help**: Kommandoliste und Nutzungshinweise anzeigen.

- **Profile Standard | Expert | Sparring | Briefing | Sandbox**: Profil wechseln (nur Standalone).
- **SCI on / SCI off**: SCI aktivieren/deaktivieren (nur Standalone). Wenn SCI aktiv ist und eine Variantenwahl pending ist, verlangt das Regelsystem, dass das A–H‑Menü gerendert wird (und der Control Layer sollte Auslassungen reparieren). **Es gibt keinen separaten „SCIplus“-Befehl; die frühere SCIplus‑Pipeline wird über SCI + Variantenwahl erreicht.**
- **Strict on / Strict off**: Strict‑Modus umschalten.
- **Explore on / Explore off**: Explore‑Modus umschalten.
- **Dynamic one-shot on**: Dynamic Prompting nur für die nächste Antwort aktivieren (danach Auto‑Reset).

---

## Ethik & Verantwortung (explizit)

Comm‑SCI‑Control behandelt Ethik **nicht als Add‑on**,
sondern als **funktionalen Bestandteil der Kontrolllogik**.

### Grundannahmen

- LLMs sind **probabilistische Textmodelle**, keine intentionalen Akteure.
- Verantwortung bleibt **immer beim Menschen**.
- Komfort, Geschwindigkeit oder Überzeugungskraft dürfen
  **niemals Transparenz und Verifizierbarkeit übersteuern**.

### Operationalisierte Ethik im Regelsystem

Ethik wird nicht moralisch, sondern **technisch** implementiert durch:

- **Safety Core:** keine Unterstützung für Schaden, klare Grenzen, Transparenz.
- **Unsicherheitsklassifikation (U1–U4):**
  Unwissen wird explizit markiert — nicht kaschiert.
- **QC‑Dimension „Neutralität“:**
  Trennung von Fakten und Werturteilen, Gegenperspektiven wenn angemessen.
- **Dynamic Prompting standardmäßig deaktiviert:**
  keine automatische Verhaltenskorrektur ohne explizite Nutzerentscheidung.

> Ziel ist **Erhalt von Autonomie**, nicht Optimierung um jeden Preis.

---

## Praktische Nutzung

Comm‑SCI‑Control wird typischerweise so genutzt:

1. als vollständiges JSON‑Regelset in einen Chat eingebracht,
2. am Anfang einer neuen Konversation explizit aktiviert,
3. in langen Dialogen bewusst re‑initialisiert (Reset),
4. intentional gesteuert statt automatisch.

---

## Zielgruppe

- Lehrkräfte und Bildungsbereich
- Fachleute in technischen und wissenschaftlichen Feldern
- reflektierte Power‑User von LLMs
- Menschen, die **Kontrollierbarkeit über Bequemlichkeit** priorisieren

---

## Status

- Aktuelle Version: **v19.4.7**
- Entwicklungsstatus: **stabil**
- Source of Truth: das **kanonische JSON‑Regelset** (README ist beschreibend, nicht normativ)

- Aktueller Fokus: Dokumentation, Beispiele, Usability, Evaluation

---

## Zitation

Wenn du dieses Framework nutzt, zitiere bitte die archivierte Version auf Zenodo:
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17930749.svg)](https://doi.org/10.5281/zenodo.17930749)
**DOI:** [10.5281/zenodo.17930749](https://doi.org/10.5281/zenodo.17930749)

---

## Lizenz

Dieses Werk ist lizenziert unter der
**Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

https://creativecommons.org/licenses/by/4.0/
