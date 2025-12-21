# Comm-SCI-Control
**Explizites Regelwerk für kontrollierte Mensch–KI-Interaktion**

> Ein LLM‑agnostisches Steuerungs‑ und Governance‑Framework zur Reduktion von Drift, zur Sicherung von Transparenz und zur bewussten Aufrechterhaltung menschlicher Kontrolle über KI‑Antworten.

---

## Motivation

Moderne Large Language Models liefern beeindruckende Ergebnisse –  
gleichzeitig zeigen sie systemische Schwächen:

- inkonsistente Antworten über längere Dialoge hinweg,
- stilles Anpassen des Antwortverhaltens,
- fehlende oder unklare Unsicherheitskennzeichnung,
- schwer überprüfbare Qualität.

**Comm‑SCI‑Control** adressiert diese Probleme **nicht durch bessere Prompts**,  
sondern durch ein **explizites, transparentes Regelwerk**, das:

- Antwortqualität sichtbar macht,
- Denk‑ und Argumentationsprozesse strukturiert,
- menschliche Kontrolle bewahrt,
- und stilles Re‑Adaptieren verhindert.

---

## Was dieses Regelwerk ist

Comm‑SCI‑Control ist:

- ein **rein textbasiertes Regelwerk** (kein Code, kein Plugin),
- **LLM‑agnostisch konzipiert** (nutzbar mit verschiedenen LLMs; Modell‑Compliance kann variieren),
- ein **externes Governance‑ und Kontrollframework** für KI‑Interaktion,
- ein Werkzeug zur **Reduktion von Drift, Mehrdeutigkeit und nicht verifizierbaren Ausgaben**.

Es definiert u. a.:

- Profile (Standard, Expert, Sparring, Briefing, Sandbox),
- strukturierte Denkprozesse (SCI mit auswählbaren Varianten),
- eine explizite QC‑Matrix mit Abweichungsanzeige (Δ),
- einen harten Control Layer gegen stille Anpassungen,
- explizite Unsicherheits‑ und Verifikationsrouten.

---

## Was dieses Regelwerk **nicht** ist

- ❌ kein autonomes Lern‑ oder Selbstoptimierungssystem
- ❌ kein Wrapper, keine API‑Erweiterung, kein Plugin
- ❌ keine Garantie für Korrektheit oder Wahrheit
- ❌ kein Ersatz für menschliches Urteil oder Verantwortung

> **Kernaussage:**  
> *Das Regelwerk macht Fehler und Drift sichtbar – es beseitigt sie nicht.*

---

## Zentrale Konzepte (Überblick)

### Profile
Profile definieren den **Kooperationsmodus** zwischen Mensch und KI  
(z. B. Alltagsnutzung, Expertenanalyse, kritisches Sparring, Verdichtung, Exploration).

### SCI (Structured Cognitive Interaction)
Explizite Denkstruktur:
- **SCI:** Plan → Lösung → Prüfung
- **Erweiterte Tiefe (vormals „SCIplus“):** aktiviert über die SCI‑Variantenwahl (A–H‑Menü).

Wenn SCI aktiv ist, sind sichtbare SCI‑Traces verpflichtend.

### QC‑Matrix
Sechs Qualitätsdimensionen:
- Klarheit
- Kürze
- Evidenz
- Empathie
- Konsistenz
- Neutralität

Jede Antwort enthält:
- eine QC‑Selbsteinschätzung,
- ein **Delta (Δ)** als Abweichung vom Zielkorridor des aktiven Profils.

#### Delta‑Semantik (seit v19.4.15)
- **Δ < 0:** unter Ziel → potenzieller Qualitätsmangel
- **Δ = 0:** im Ziel → akzeptabel
- **Δ > 0:** über Ziel → Risiko der Überoptimierung  
  (z. B. Halluzinationsrisiko bei zu hoher Evidenz)

**Handlungsempfehlung:**
- |Δ| ≥ 2 → manuelle Korrektur durch den Nutzer empfohlen
- |Δ| < 2 → nur Beobachtung

### Control Layer
Meta‑Ebene zur Durchsetzung von:
- Regelkohärenz,
- Auditierbarkeit,
- Schutz vor stillen Verhaltensänderungen.

---

## Umgang mit Unsicherheit

Comm‑SCI‑Control verwendet eine explizite Unsicherheits‑Taxonomie:

- **U1 – Datenlücke**
- **U2 – Logische Unterbestimmtheit**
- **U3 – Normativer Dissens**
- **U4 – Zeitliche Instabilität**
- **U5 – Modellgrenze** *(seit v19.4.15)*  
  Strukturelle Begrenzung des LLM; Aufgabe ist nicht zuverlässig lösbar.
- **U6 – Mehrdeutige Anfrage** *(seit v19.4.15)*  
  Anfrage ist unterbestimmt oder besitzt mehrere valide Interpretationen.

Jedes Unsicherheitslabel erzwingt einen **definierten nächsten Schritt**  
(z. B. Klärung, alternative Methoden, Verifikationsrouten).

---

## Verifikationsdisziplin

- **Verification Route Gate:** starke Behauptungen erfordern mindestens eine explizite Route  
  (Messung, Quelle, Kontrast oder Web‑Check).
- Behauptungen ohne valide Route müssen herabgestuft und als unsicher markiert werden.
- Evidenzwerte werden begrenzt, wenn Verifikation fehlt.

---

## Befehle (Kurzreferenz)

**Wichtig:** Befehle werden **nur** erkannt, wenn sie als **alleinstehender Prompt** gesendet werden.

- **Comm Start / Comm Stop**
- **Comm Status / Comm Help**
- **Profile Standard | Expert | Sparring | Briefing | Sandbox**
- **SCI on / SCI off**
- **Strict on / Strict off**
- **Explore on / Explore off**
- **Dynamic one‑shot on**

---

## Ethik & Verantwortung

Ethik wird **technisch**, nicht rhetorisch umgesetzt:

- LLMs sind probabilistische Sprachmodelle, keine handelnden Subjekte.
- Verantwortung verbleibt stets beim Menschen.
- Transparenz und Verifizierbarkeit haben Vorrang vor Komfort oder Überzeugungskraft.
- Unsicherheit muss explizit benannt werden, nicht verdeckt.

---

## Praktische Nutzung

Typischer Ablauf:

1. Übergabe des kanonischen JSON‑Regelwerks an das LLM,
2. explizite Aktivierung zu Beginn eines Dialogs,
3. bewusste Re‑Initialisierung in längeren Gesprächen,
4. intentionale Steuerung statt impliziter Anpassung.

---

## Zielgruppe

- Lehrkräfte und Pädagogen
- Fachkräfte aus Technik und Wissenschaft
- reflektierte Power‑User von LLMs
- Personen, die **Kontrollierbarkeit über Bequemlichkeit** stellen

---

## Status

- **Aktuelle Version:** v19.4.15
- **Stabilität:** stabil / produktionsreif
- **Source of Truth:** kanonisches JSON‑Regelwerk  
  (README ist beschreibend, nicht normativ)

Aktueller Fokus: Dokumentation, Beispiele, Usability, Evaluation.

---

## Zitation

Wenn Sie dieses Framework verwenden, zitieren Sie bitte die archivierte Zenodo‑Version:  
**DOI:** https://doi.org/10.5281/zenodo.17930749

---

## Lizenz

Creative Commons Attribution 4.0 International (CC BY 4.0)  
https://creativecommons.org/licenses/by/4.0/
