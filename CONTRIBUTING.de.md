# Beitragshilfe

Dieses Repository enthaelt Governance-Artefakte (JSON-Regelwerke + Dokumentation), keine Runtime-Anwendung.

## Umfang von Beitraegen

Sinnvolle Beitraege sind:

- Regelwerksaenderungen in `JSON/`
- Governance-Doku-Updates (`README*`, `docs/*`, `CHANGELOG.md`, `CITATION.cff`)
- Verbesserungen der Validierung (`tests/*`, `schemas/*`, `scripts/*`)

Nicht sinnvoll:

- rein kosmetische Aenderungen ohne Governance-Nutzen
- Tests ohne reale Risiko-Reduktion

## Lokaler Ablauf

1. Artefakte anpassen.
2. Fixtures neu generieren, falls Regel-/Vertragslogik geaendert wurde:
   - `python3 scripts/generate_fixtures.py`
3. Deterministische Validierung ausfuehren:
   - `bash scripts/validate_repo.sh`
4. Diffs pruefen (insbesondere Fixtures und Changelog).
5. Mit klarer, eng gefasster Message committen.

## Test-Policy

Blocking-Checks vor Merge/Release:

- `core`, `schema`, `versions`, `integrity`, `docs`, `migration`

Advisory-Checks:

- Live-`e2e`-Tests (`tests/e2e/test_llm_behavior_e2e.py`)

Live-E2E ist bewusst optional, da Modellverhalten probabilistisch und umgebungsabhaengig ist.

## Fixtures und Schemata

Wenn sich Vertragsverhalten aendert:

- Fixtures aktualisieren/generieren
- Migrationsmatrix konsistent halten
- Schemata nur bei beabsichtigten Struktur-Aenderungen anpassen
- beabsichtigte Breaking Changes im `CHANGELOG.md` dokumentieren

## Dokumentationsregeln

- EN- und DE-Doku synchron halten, wenn beide Fassungen existieren.
- Wenn sich Governance-Verhalten aendert, aktualisiere:
  - `README.md`
  - `README.de.md`
  - `CHANGELOG.md`
  - `docs/TESTING*.md` falls sich Test-Interpretation aendert

## Erwartungen an Commit/PR

- Kleine, gut reviewbare Commits sind bevorzugt.
- Commit-Messages sollen die Governance-Absicht beschreiben, nicht nur Dateiaenderungen.
- Bei nicht-trivialen Aenderungen kurz im PR begruenden:
  - Was wurde geaendert?
  - Warum?
  - Welche Tests belegen es?
