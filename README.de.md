# Comm-SCI-Control  
**Explizites Regelsystem für kontrollierte Mensch–KI-Interaktion**

Ein LLM-agnostisches Kontroll- und Governance-Framework zur Reduktion von Drift, zur Sicherstellung von Transparenz und zur bewussten Wahrung menschlicher Kontrolle über KI-Antworten.

---

## Motivation

Moderne Large Language Models liefern beeindruckende Ergebnisse – zugleich zeigen sie jedoch systemische Schwächen:

- inkonsistente Antworten über längere Konversationen hinweg,
- stille Anpassung des Antwortverhaltens,
- fehlende oder unklare Unsicherheitskennzeichnung,
- Qualität, die schwer überprüfbar oder auditierbar ist.

**Comm-SCI-Control** adressiert diese Probleme **nicht durch bessere Prompts**, sondern durch ein **explizites, transparentes Regelsystem**, das:

- Antwortqualität sichtbar macht,
- Denkprozesse strukturiert,
- menschliche Kontrolle bewahrt,
- und stille Re-Adaptation verhindert.

---

## Was dieses Regelsystem ist

Comm-SCI-Control ist:

- ein **rein textbasiertes Regelsystem** (kein Code, kein Plugin),
- **LLM-agnostisch konzipiert** (mit verschiedenen Modellen nutzbar; Regelbefolgung kann variieren),
- ein **externes Governance- und Kontrollframework** für KI-Interaktion,
- ein Werkzeug zur **Reduktion von Drift, Mehrdeutigkeit und nicht überprüfbarer Ausgabe**.

Es definiert unter anderem:

- **Profile** (Standard, Expert, Sparring, Briefing, Sandbox),
- **strukturierte Denkprozesse** (SCI mit auswählbaren Varianten),
- eine **explizite QC-Matrix** mit Abweichungsberichten (Δ),
- eine **harte Control Layer** gegen stille Anpassung,
- **explizite Unsicherheitsbehandlung und Verifikationsrouten**,
- **deterministische Initialisierung und kanonische Zustandsdurchsetzung** (seit v19.4.21),
- **explizite Rendering-Kontrollen** (Color on/off, nicht-semantisch).

---

## Was dieses Regelsystem nicht ist

- ❌ kein autonom lernendes oder selbstoptimierendes System  
- ❌ kein Wrapper, keine API-Erweiterung und kein Plugin  
- ❌ keine Garantie für Korrektheit oder Wahrheit  
- ❌ kein Ersatz für menschliches Urteil oder Verantwortung  

**Kernaussage:**  
Das Regelsystem macht Fehler und Drift **sichtbar** – es beseitigt sie nicht.

---

## Zentrale Konzepte (Überblick)

### Profile

Profile definieren den **Modus der Zusammenarbeit** zwischen Mensch und KI  
(z. B. Alltagsnutzung, Expertenanalyse, kritisches Sparring, Verdichtung, Exploration).

Profilwechsel sind **explizit und auditierbar**.  
Automatische oder implizite Profilwechsel sind verboten.

---

### SCI (Structured Cognitive Interaction)

Explizite Denkstruktur:

- **SCI:** Plan → Lösung → Prüfung  
- **Erweiterte Tiefe:** auswählbar über das SCI-Variantenmenü (A–H)

Wenn SCI aktiv ist:
- ist die **vollständige Denkspur verpflichtend**,
- stille Kompression oder Auslassung ist unzulässig.

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
- ein **Delta (Δ)**, das die Abweichung vom Zielkorridor des aktiven Profils angibt.

#### Delta-Semantik

- Δ < 0 → unter Ziel (potenzielles Qualitätsdefizit)  
- Δ = 0 → im Zielbereich (akzeptabel)  
- Δ > 0 → über Ziel (Risiko der Überoptimierung, z. B. Halluzinationsgefahr bei zu hoher Evidenz)

**Handlungsempfehlung:**

- |Δ| ≥ 2 → manuelle Korrektur durch den Nutzer empfohlen  
- |Δ| < 2 → nur Monitoring erforderlich  

---

### Control Layer

Eine Meta-Ebene zur Durchsetzung von:

- Regelkohärenz,
- Auditierbarkeit,
- Verhinderung stiller Verhaltensänderungen,
- strikter Trennung von Governance-Logik und Darstellung.

---

## Unsicherheitsbehandlung

Comm-SCI-Control verwendet eine **explizite Unsicherheitstaxonomie**:

- **U1 – Datenlücke**
- **U2 – Logische Unterbestimmtheit**
- **U3 – Normativer Dissens**
- **U4 – Zeitliche Instabilität**
- **U5 – Modellbegrenzung**  
  Strukturelle Grenze des LLM; Aufgabe kann nicht zuverlässig gelöst werden.
- **U6 – Mehrdeutige Anfrage**  
  Eingabe ist unterbestimmt oder erlaubt mehrere valide Interpretationen.

Jede Unsicherheitsklasse **erzwingt einen nächsten Schritt**  
(z. B. Klärung, alternative Ansätze, Verifikationsrouten).

---

## Verifikationsdisziplin

- **Verification-Route-Gate:**  
  Starke Behauptungen erfordern mindestens eine explizite Route  
  (Messung, Quelle, Kontrast oder Web-Check).

- Behauptungen ohne gültige Route müssen **abgestuft und als unsicher markiert** werden.

- Evidenzwerte werden **gedeckelt**, wenn keine Verifikation vorliegt.

---

## Rendering- und Farbkontrolle (seit v19.4.21)

- Darstellungsmerkmale sind **explizit von der Governance-Logik getrennt**.
- `Color on/off` ist **ausschließlich eine Präsentationskontrolle**.

### Zweck von `Color on`

- Verbesserung der **Lesbarkeit und Orientierung** bei kognitiv dichten Ausgaben.
- Hervorhebung **struktureller, zustandsbezogener oder diagnostischer Elemente**.

### Zulässige Farbkategorien

Wenn `Color on` aktiviert ist, sind **genau drei Kategorien** erlaubt:

- **Neutral / Strukturfarbe**  
  Strukturelle Trennung (Überschriften, Tabellen, Abschnitte).

- **Zustands- / Statusfarbe**  
  Explizite Systemzustände (Profil, SCI an/aus, Color an/aus).

- **Aufmerksamkeits- / Diagnosefarbe**  
  Governance-relevante Hinweise (Unsicherheit, Schleifenwarnungen, Verifikationspflichten).

Farben dürfen **niemals** Korrektheit, Qualität, Zustimmung, Überzeugung oder Präferenz codieren.

Standardzustand: `Color off`.

---

## Befehle (Kurzübersicht)

**Wichtig:** Befehle werden **nur erkannt, wenn sie als alleinstehende Eingabe gesendet werden**.

- `Comm Start` / `Comm Stop`
- `Comm Status` / `Comm Help`
- `Profile Standard | Expert | Sparring | Briefing | Sandbox`
- `SCI on` / `SCI off`
- `Strict on` / `Strict off`
- `Explore on` / `Explore off`
- `Dynamic one-shot on`
- `Color on` / `Color off`

Befehlstokens sind **kanonisch und ausschließlich englisch**.  
Erklärtexte dürfen lokalisiert sein.

---

## Ethik & Verantwortung

Ethik wird **technisch umgesetzt, nicht rhetorisch**:

- LLMs sind probabilistische Modelle, keine Akteure.
- Verantwortung verbleibt immer beim Menschen.
- Transparenz und Verifizierbarkeit haben Vorrang vor Komfort oder Überzeugung.
- Unsicherheit muss **explizit gemacht**, nicht verborgen werden.

---

## Praktische Nutzung

Typischer Ablauf:

1. Das **kanonische JSON-Regelwerk** an das LLM übergeben.
2. Zu Gesprächsbeginn explizit aktivieren.
3. In langen Sitzungen bewusst re-initialisieren.
4. Verhalten **intentional steuern – niemals implizit**.

---

## Zielgruppe

- Lehrkräfte und Pädagog:innen
- technische und wissenschaftliche Fachanwender:innen
- reflektierte Power-User von LLMs
- alle, die **Kontrolle höher bewerten als Bequemlichkeit**

---

## Status

- **Aktuelle Version:** v19.4.21  
- **Stabilität:** stabil / produktionsreif  
- **Source of Truth:** kanonisches JSON-Regelwerk  
  (README ist beschreibend, nicht normativ)

**Aktueller Fokus:**  
Dokumentation, Beispiele, Nutzbarkeit, Evaluation, Auditierbarkeit.

---

## Zitation

Wenn Sie dieses Framework verwenden, zitieren Sie bitte die archivierte Zenodo-Version:  
https://doi.org/10.5281/zenodo.17930749

---

## Lizenz

Creative Commons Attribution 4.0 International (CC BY 4.0)  
https://creativecommons.org/licenses/by/4.0/