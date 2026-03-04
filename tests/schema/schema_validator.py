from __future__ import annotations

import re
from typing import Any


def _is_type(value: Any, type_name: str) -> bool:
    if type_name == "object":
        return isinstance(value, dict)
    if type_name == "array":
        return isinstance(value, list)
    if type_name == "string":
        return isinstance(value, str)
    if type_name == "boolean":
        return isinstance(value, bool)
    if type_name == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if type_name == "number":
        return (isinstance(value, int) and not isinstance(value, bool)) or isinstance(
            value, float
        )
    if type_name == "null":
        return value is None
    return True


def validate_json(instance: Any, schema: dict[str, Any], path: str = "$") -> list[str]:
    errors: list[str] = []

    schema_type = schema.get("type")
    if schema_type and not _is_type(instance, schema_type):
        errors.append(f"{path}: expected type '{schema_type}', got '{type(instance).__name__}'")
        return errors

    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: expected const value {schema['const']!r}, got {instance!r}")

    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: value {instance!r} not in enum {schema['enum']!r}")

    if isinstance(instance, str) and "pattern" in schema:
        if not re.search(schema["pattern"], instance):
            errors.append(f"{path}: value {instance!r} does not match pattern {schema['pattern']!r}")

    if isinstance(instance, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in instance:
                errors.append(f"{path}: missing required key '{key}'")

        min_props = schema.get("minProperties")
        if min_props is not None and len(instance) < min_props:
            errors.append(f"{path}: expected at least {min_props} properties")

        properties = schema.get("properties", {})
        for key, child_schema in properties.items():
            if key in instance:
                errors.extend(validate_json(instance[key], child_schema, f"{path}.{key}"))

        additional = schema.get("additionalProperties", True)
        if additional is False:
            allowed = set(properties.keys())
            for key in instance.keys():
                if key not in allowed:
                    errors.append(f"{path}: additional property '{key}' is not allowed")

    if isinstance(instance, list):
        min_items = schema.get("minItems")
        if min_items is not None and len(instance) < min_items:
            errors.append(f"{path}: expected at least {min_items} items")

        max_items = schema.get("maxItems")
        if max_items is not None and len(instance) > max_items:
            errors.append(f"{path}: expected at most {max_items} items")

        if schema.get("uniqueItems"):
            seen = {repr(item) for item in instance}
            if len(seen) != len(instance):
                errors.append(f"{path}: expected unique items")

        item_schema = schema.get("items")
        if item_schema:
            for idx, item in enumerate(instance):
                errors.extend(validate_json(item, item_schema, f"{path}[{idx}]"))

    return errors
