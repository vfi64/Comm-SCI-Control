# Security Policy

This repository provides governance rules and quality-control workflows for Comm-SCI-Control.

## Supported Versions

| Version line | Supported |
|---|---|
| `v20.2.x` | yes |
| `< v20.2.0` | no |

## Reporting a Vulnerability

Please report security issues privately:

1. Prefer GitHub Private Vulnerability Reporting:
   - `https://github.com/vfi64/Comm-SCI-Control/security/advisories/new`
2. Do not publish exploit details in public issues first.
3. Include:
   - affected file/path and version/tag
   - impact and attack scenario
   - reproducible steps or proof-of-concept
   - suggested mitigation (if available)

If private reporting is not available in your GitHub UI, open a minimal public issue without exploit details and request a private channel.

## Response Targets

- Initial triage response: within 7 days
- Status update cadence: at least every 14 days while open
- Critical issues: prioritized for fastest possible patch/release

## Disclosure Process

1. Triage and reproduce
2. Prepare fix and tests/docs updates
3. Coordinate disclosure timing
4. Publish patch release and advisory notes

## Scope Notes

In-scope examples:
- bypasses of governance enforcement that materially alter security-relevant behavior
- vulnerabilities in scripts/workflows that expose secrets or enable unsafe execution
- integrity issues that can silently falsify validation/audit outputs

Out-of-scope examples:
- generic model hallucinations without a concrete implementation flaw
- purely theoretical issues without reproducible impact
- support requests and feature proposals

## Safe Harbor

Good-faith security research is welcome. Please avoid privacy violations, destructive testing, or service disruption.

## Hinweis (DE)

Sicherheitsmeldungen bitte bevorzugt ueber GitHub Security Advisories (privat) einreichen und keine Exploit-Details zuerst oeffentlich posten.
