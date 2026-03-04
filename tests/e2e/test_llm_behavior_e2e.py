from __future__ import annotations

import json
import os
import re
import unittest
import urllib.error
import urllib.request
from typing import Any

from tests.helpers import load_json, load_text


class OpenAICompatibleChatClient:
    def __init__(self, api_base: str, api_key: str, model: str, timeout_seconds: int) -> None:
        self.api_base = api_base.rstrip("/")
        self.api_key = api_key
        self.model = model
        self.timeout_seconds = timeout_seconds

    def complete(self, messages: list[dict[str, str]]) -> str:
        url = f"{self.api_base}/chat/completions"
        payload = {
            "model": self.model,
            "temperature": 0,
            "messages": messages,
        }
        data = json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(
            url=url,
            data=data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout_seconds) as response:
                body = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            raw = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"HTTP error from LLM API ({exc.code}): {raw}") from exc
        except urllib.error.URLError as exc:
            raise RuntimeError(f"Network error while calling LLM API: {exc.reason}") from exc

        try:
            return body["choices"][0]["message"]["content"]
        except Exception as exc:  # pragma: no cover - defensive guard
            raise RuntimeError(f"Unexpected LLM API response structure: {body!r}") from exc


def evaluate_scenario(response: str, scenario: dict[str, Any]) -> dict[str, Any]:
    token_hits = 0
    for token in scenario.get("required_tokens", []):
        if token.lower() in response.lower():
            token_hits += 1

    regex_hits = 0
    for pattern in scenario.get("required_regex", []):
        if re.search(pattern, response, flags=re.IGNORECASE | re.DOTALL):
            regex_hits += 1

    forbidden_hits = []
    for pattern in scenario.get("forbidden_regex", []):
        if re.search(pattern, response, flags=re.IGNORECASE | re.DOTALL):
            forbidden_hits.append(pattern)

    passed = (
        token_hits >= scenario.get("min_token_hits", 0)
        and regex_hits >= scenario.get("min_regex_hits", 0)
        and not forbidden_hits
    )

    return {
        "passed": passed,
        "token_hits": token_hits,
        "regex_hits": regex_hits,
        "forbidden_hits": forbidden_hits,
    }


@unittest.skipUnless(
    os.environ.get("CSC_E2E_ENABLE") == "1",
    "Set CSC_E2E_ENABLE=1 to run live LLM behavior E2E tests.",
)
class TestLLMBehaviorE2E(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        api_key = os.environ.get("CSC_E2E_API_KEY")
        if not api_key:
            raise unittest.SkipTest("CSC_E2E_API_KEY is not set.")

        cls.client = OpenAICompatibleChatClient(
            api_base=os.environ.get("CSC_E2E_API_BASE", "https://api.openai.com/v1"),
            api_key=api_key,
            model=os.environ.get("CSC_E2E_MODEL", "gpt-4.1-mini"),
            timeout_seconds=int(os.environ.get("CSC_E2E_TIMEOUT_SECONDS", "120")),
        )
        cls.scenario_manifest = load_json("tests/fixtures/e2e_scenarios.v20.2.0.json")
        cls.ruleset = load_text("JSON/Comm-SCI-v20.2.0.min.json")
        cls.attempts = max(1, int(os.environ.get("CSC_E2E_ATTEMPTS", "2")))

    def _build_messages(self, scenario_input: str) -> list[dict[str, str]]:
        preface = (
            "Context for this conversation:\n"
            "I am providing an external governance ruleset for response structure and quality.\n"
            "Do not override platform safety rules. Treat the JSON as the normative ruleset.\n"
            "Return only the response to the standalone input.\n"
        )
        task_prompt = (
            f"{preface}\n"
            f"Ruleset JSON:\n{self.ruleset}\n\n"
            f"Standalone input to process:\n{scenario_input}\n"
        )
        return [{"role": "user", "content": task_prompt}]

    def test_live_scenarios(self) -> None:
        failures: list[str] = []
        scenarios = self.scenario_manifest["scenarios"]

        for scenario in scenarios:
            scenario_passed = False
            last_result: dict[str, Any] | None = None
            last_response = ""
            messages = self._build_messages(scenario["input"])

            for _ in range(self.attempts):
                response = self.client.complete(messages)
                result = evaluate_scenario(response, scenario)
                last_result = result
                last_response = response
                if result["passed"]:
                    scenario_passed = True
                    break

            if not scenario_passed:
                failures.append(
                    json.dumps(
                        {
                            "scenario_id": scenario["id"],
                            "result": last_result,
                            "response_excerpt": last_response[:700],
                        },
                        ensure_ascii=False,
                    )
                )

        if failures:
            self.fail("Live E2E scenario failures:\n" + "\n".join(failures))


if __name__ == "__main__":
    unittest.main()
