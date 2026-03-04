# Release-Leitfaden

Dieser Leitfaden standardisiert die Release-Erstellung fuer Comm-SCI-Control.

## Voraussetzungen

Vor einem Release:

- Arbeitsbaum ist sauber
- deterministische Suite lokal gruen:
  - `bash scripts/validate_repo.sh`
- Doku und Metadaten sind synchron:
  - `README.md` / `README.de.md`
  - `CHANGELOG.md`
  - `CITATION.cff`
- Zielversion existiert in `JSON/`

## Empfohlene Reihenfolge

1. Letzte lokale Validierung:
   - `python3 scripts/generate_fixtures.py`
   - `bash scripts/validate_repo.sh`
2. Offene Aenderungen committen.
3. Branch pushen.
4. CI-Status pruefen (`validate.yml` gruen).
5. Release-Tag und GitHub-Release erstellen.

## Tag- und Release-Benennung

- Tag-Format: `v<major>.<minor>.<patch>` (Beispiel: `v20.2.0`)
- Release-Titel:
  - `Comm-SCI-Control V<major>.<minor>.<patch>`

## Quelle der Release-Notes

- Notes aus dem entsprechenden oberen Abschnitt in `CHANGELOG.md` uebernehmen.
- Notes knapp und governance-fokussiert halten:
  - Verhaltens-/Vertragsaenderungen
  - migrationsrelevante Aenderungen
  - Command-Surface-Aenderungen

## Optionales Live-E2E vor Release

Live-E2E kann fuer zusaetzliche Sicherheit laufen, ist aber kein harter Gate:

- `CSC_E2E_API_KEY=... bash scripts/run_e2e_llm_tests.sh`

Interpretation:

- pass: zusaetzliche Sicherheit
- fail: Modell-/Runtime-Sensitivitaet analysieren; deterministische Suite nicht pauschal ueberstimmen

## Nach dem Release

- Release-Metadaten pruefen (Titel, Tag, Notes)
- Sichtbarkeit des Latest-Tags pruefen
- falls noetig, Zitier-/Release-Verweise in der Doku aktualisieren
