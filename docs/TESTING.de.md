# Teststrategie

Dieses Dokument beschreibt Zweck, Umfang und Ergebnisinterpretation der Testsuite.

## Zweck

Die Tests sind darauf ausgerichtet, Governance-Qualität zu schützen, nicht bloß eine hohe Testanzahl zu erzeugen.

Primäre Ziele:

- Unbeabsichtigten Regelwerks-Drift früh erkennen.
- JSON, Dokumentation und Metadaten auf derselben Versionsbasis halten.
- Versionsänderungen explizit und auditierbar machen.
- Deterministische Strukturprüfungen klar von probabilistischen Live-Model-Checks trennen.

## Umfang

Die Suite ist in fokussierte Ebenen aufgeteilt:

- `tests/core`: JSON-Grundvalidität, Versions-/Dateikonsistenz, Command-Token-Sanity.
- `tests/schema`: tiefe Strukturvalidierung gegen dedizierte Schemata in `/schemas`.
- `tests/versions`: Vertragsprüfungen für die aktive operative Linie (`v20.2.2`).
- `tests/integrity`: deterministische Hash-/Integritätsprüfungen operativer Artefakte.
- `tests/docs`: Konsistenzprüfungen für README/CHANGELOG/CITATION.
- `tests/migration`: versionsübergreifende Feature-Matrix + Migrationsinvarianten.
- `tests/e2e`: optionale Live-LLM-Verhaltenstests (Scoring-Szenarien, Retries, kein striktes Exact-Match-Orakel).

## Determinismus-Stufen

- Deterministisch (blocking): `core`, `schema`, `versions`, `integrity`, `docs`, `migration`.
- Probabilistisch (standardmäßig advisory): Live-`e2e`-Tests.

Diese Trennung ist beabsichtigt. LLM-Ausgaben sind inhärent nicht deterministisch, daher arbeiten E2E-Checks mit Schwellwerten und Wiederholungslogik.

## Tests ausführen

Deterministische Vollsuite:

```bash
bash scripts/validate_repo.sh
```

Schneller deterministischer Core-Tier:

```bash
bash scripts/validate_repo.sh --tier core
```

Nur advisory Live-E2E-Tier:

```bash
bash scripts/validate_repo.sh --tier e2e
```

Fixtures nach beabsichtigten Regeländerungen neu generieren:

```bash
python3 scripts/generate_fixtures.py
```

Optionale Live-LLM-E2E-Checks:

```bash
CSC_E2E_API_KEY=... bash scripts/run_e2e_llm_tests.sh
```

## Ergebnisse interpretieren

- `OK` (deterministische Suite): Struktur- und Governance-Baselines sind konsistent.
- Fixture-Mismatch (`tests/fixtures/*.json`): Regeln oder Generatorlogik wurden geändert.
  - Aktion: Absicht prüfen, Fixtures neu generieren, Diff prüfen, dann committen.
- Schema-Fehler: JSON-Struktur passt nicht mehr zum kanonischen/operativen Vertrag.
  - Aktion: Regelwerksstruktur korrigieren oder Schema bewusst anpassen.
- Migrationsinvarianten-Fehler: versionsübergreifende Annahmen sind gebrochen.
  - Aktion: entscheiden, ob beabsichtigt; falls ja, Migrations-Fixture + Invarianten aktualisieren.
- E2E-Fehler: typischerweise Verhaltensdrift oder Prompt-Sensitivität im aktuellen Modell/Runtime-Setup.
  - Aktion: Szenario-Report prüfen, erneut ausführen, dann Schwellwerte/Szenarien nur mit klarer Begründung anpassen.

## CI-Policy

- `validate.yml` führt deterministische Checks bei Push/PR aus und sollte blocking bleiben.
- `e2e-llm.yml` ist manuell (`workflow_dispatch`) und optional, da API-Credentials sowie Modell-/Runtime-Varianz nötig sind.

## Änderungs-Governance für Tests

Wenn sich das Regelwerk ändert:

1. JSON/Regeln anpassen.
2. Fixtures neu generieren.
3. Deterministische Suite ausführen.
4. Fixture- und Doku-Diffs prüfen.
5. Optional Live-E2E für zusätzliche Verhaltenssicherheit ausführen.
