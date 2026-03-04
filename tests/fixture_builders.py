from __future__ import annotations

from typing import Any

from tests.helpers import command_tokens, parse_semver_like, recursive_keys


def build_v20_2_0_contract_snapshot(document: dict[str, Any]) -> dict[str, Any]:
    normative_rule_ids = [rule["id"] for rule in document["normative_model"]["rules"]]
    preflight_ids = [entry["id"] for entry in document["preemptive_logic"]["preflight_checks"]]
    uncertainty_labels = sorted(
        document["contracts"]["uncertainty"]["taxonomy"]["labels"].keys()
    )
    csc_trigger_bridge = document["csc"]["trigger_bridge"]

    return {
        "schema": document["schema"],
        "source_version": document["source"]["version"],
        "source_canonical_version": document["source"]["canonical_version"],
        "execution_order": document["execution_order"],
        "preflight_ids": preflight_ids,
        "normative_rule_ids": normative_rule_ids,
        "rag_rule_ids": [rule_id for rule_id in normative_rule_ids if rule_id.startswith("R-RAG-")],
        "uncertainty_labels": uncertainty_labels,
        "command_tokens": sorted(set(command_tokens(document))),
        "csc_triggers_any_of": csc_trigger_bridge["triggers_any_of"],
        "csc_governance_triggered_semantics": csc_trigger_bridge[
            "governance_triggered_semantics"
        ],
        "has_phi_compliance_block": "phi_compliance" in set(recursive_keys(document)),
    }


def _uncertainty_labels(document: dict[str, Any]) -> list[str]:
    if "contracts" in document:
        labels = document["contracts"]["uncertainty"]["taxonomy"]["labels"]
        return sorted(labels.keys())
    labels = document["global_defaults"]["uncertainty_taxonomizer"]["labels"]
    return sorted(labels.keys())


def _preflight_ids(document: dict[str, Any]) -> list[str]:
    if "preemptive_logic" not in document:
        return []
    return [entry["id"] for entry in document["preemptive_logic"]["preflight_checks"]]


def _rule_ids(document: dict[str, Any]) -> list[str]:
    if "normative_model" in document:
        return [rule["id"] for rule in document["normative_model"]["rules"]]
    return []


def _has_retrieval_trigger(document: dict[str, Any]) -> bool:
    if "csc" in document:
        trigger_bridge = document["csc"]["trigger_bridge"]
        return "retrieval_check_active" in trigger_bridge.get("triggers_any_of", [])
    keys = set(recursive_keys(document))
    return "retrieval_check_active" in keys


def _artifact_type(document: dict[str, Any]) -> str:
    return "operational" if "schema" in document else "canonical"


def build_version_feature_snapshot(version: str, document: dict[str, Any]) -> dict[str, Any]:
    tokens = set(command_tokens(document))
    rules = _rule_ids(document)
    preflight = _preflight_ids(document)
    labels = _uncertainty_labels(document)
    keys = set(recursive_keys(document))

    return {
        "version": version,
        "artifact_type": _artifact_type(document),
        "has_comm_validate": "Comm Validate" in tokens,
        "has_anchor_auto_off": "Anchor auto off" in tokens,
        "has_comm_anchor_on": "Comm Anchor on" in tokens,
        "has_comm_anchor_off": "Comm Anchor off" in tokens,
        "has_phi_compliance_block": "phi_compliance" in keys,
        "has_u7": "U7" in labels,
        "has_u8": "U8" in labels,
        "has_retrieval_check_active": _has_retrieval_trigger(document),
        "preflight_ids": preflight,
        "rag_rule_ids": [rule_id for rule_id in rules if rule_id.startswith("R-RAG-")],
        "uncertainty_labels": labels,
    }


def build_migration_matrix_snapshot(versioned_documents: dict[str, dict[str, Any]]) -> dict[str, Any]:
    versions = sorted(versioned_documents.keys(), key=parse_semver_like)
    features = {
        version: build_version_feature_snapshot(version, versioned_documents[version])
        for version in versions
    }
    return {"ordered_versions": versions, "features_by_version": features}


def build_e2e_scenario_manifest(document: dict[str, Any]) -> dict[str, Any]:
    tokens = set(command_tokens(document))
    help_required = [
        token
        for token in [
            "Comm Start",
            "Comm State",
            "Comm Validate",
            "Profile Expert",
            "SCI on",
            "Color on",
        ]
        if token in tokens
    ]

    return {
        "version": document.get("source", {}).get("version", document.get("version")),
        "artifact_type": _artifact_type(document),
        "scenarios": [
            {
                "id": "help_command_coverage",
                "description": "Comm Help should expose the command surface with canonical tokens.",
                "input": "Comm Help",
                "required_tokens": help_required,
                "min_token_hits": max(4, len(help_required) - 1),
                "required_regex": [],
                "min_regex_hits": 0,
                "forbidden_regex": [],
            },
            {
                "id": "invalid_control_command_rejection",
                "description": "Control on should not be accepted as a canonical command token.",
                "input": "Control on",
                "required_tokens": ["Control on"],
                "min_token_hits": 1,
                "required_regex": [
                    r"(not|no|unknown|invalid|undefined|nicht|kein)[\s\S]{0,60}(command|token|canonical|kanonisch|kommando|definiert)",
                ],
                "min_regex_hits": 1,
                "forbidden_regex": [
                    r"(control\s+on)[\s\S]{0,40}(enabled|activated|ok|accepted)",
                ],
            },
            {
                "id": "anchor_command_response",
                "description": "Comm Anchor should mention anchor snapshot semantics.",
                "input": "Comm Anchor",
                "required_tokens": ["Comm Anchor"],
                "min_token_hits": 1,
                "required_regex": [r"(anchor)[\s\S]{0,60}(snapshot|state|session)"],
                "min_regex_hits": 1,
                "forbidden_regex": [],
            },
        ],
    }
