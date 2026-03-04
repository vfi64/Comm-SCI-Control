# CI-Leitfaden

Dieses Dokument beschreibt die CI-Workflows und ihre beabsichtigte Rolle.

## Workflows

### `validate.yml` (deterministischer Gate)

Trigger:

- Push auf `main`
- Pull Request auf `main`
- manueller Start

Verhalten:

- fuehrt `bash scripts/validate_repo.sh` aus
- prueft deterministische Checks:
  - core, schema, versions, integrity, docs, migration
- sollte fuer Merge/Release als blocking gelten

### `e2e-llm.yml` (optionaler Live-Verhaltenscheck)

Trigger:

- nur manueller Start

Verhalten:

- generiert Fixtures neu
- fuehrt Live-LLM-E2E nur aus, wenn `CSC_E2E_API_KEY` als Secret gesetzt ist
- ueberspringt sauber, wenn kein API-Key konfiguriert ist

## Umgebung und Secrets

Live-E2E nutzt:

- Secret:
  - `CSC_E2E_API_KEY` (fuer Live-Ausfuehrung erforderlich)
- optionale Repository-Variablen:
  - `CSC_E2E_MODEL` (Default: `gpt-4.1-mini`)
  - `CSC_E2E_API_BASE` (Default: `https://api.openai.com/v1`)
  - `CSC_E2E_ATTEMPTS` (Default: `2`)

## Umgang mit Fehlern

Wenn `validate.yml` fehlschlaegt:

- als strukturelle/governance Regression behandeln
- vor Merge/Release beheben

Wenn `e2e-llm.yml` fehlschlaegt:

- Szenario-Details pruefen
- erneut laufen lassen, um transiente Modell-/Runtime-Varianz auszuschliessen
- Schwellwerte nur mit expliziter Begruendung anpassen

## Local-First-Regel

Vor dem Push:

1. `python3 scripts/generate_fixtures.py`
2. `bash scripts/validate_repo.sh`

So bleiben CI-Fehler selten und nachvollziehbar.
