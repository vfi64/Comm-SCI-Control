import unittest

from tests.helpers import load_json


class TestCommandOutputContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.v20_1 = load_json("JSON/Comm-SCI-v20.1.0.json")
        cls.v20_2 = load_json("JSON/Comm-SCI-v20.2.0.json")

    def test_sci_menu_requires_table_format(self) -> None:
        menu_20_1 = self.v20_1["global_defaults"]["output_contract"]["sci_variant_menu_contract"]
        menu_20_2 = self.v20_2["contracts"]["output_contract"]["sci_variant_menu_contract"]

        for menu in (menu_20_1, menu_20_2):
            with self.subTest(schema=menu.get("block_title_source_path", "unknown")):
                self.assertEqual(["table"], menu["acceptable_formats"])
                self.assertEqual(
                    ["Variant", "Name", "Focus / Method"],
                    menu["required_table_columns"],
                )
                self.assertIn("table", " ".join(menu["minimum_requirements"]).lower())

        rc_20_1 = self.v20_1["global_defaults"]["output_contract"]["response_contracts"]
        rc_20_2 = self.v20_2["contracts"]["output_contract"]["response_contracts"]
        self.assertIn("sci_variant_menu_table", rc_20_1["profile_switch_minimal_expert_sparring"]["required_blocks"])
        self.assertIn("sci_variant_menu_table", rc_20_2["profile_switch_minimal_expert_sparring"]["required_blocks"])

    def test_comm_help_is_exhaustive_structured_contract(self) -> None:
        help_policy_20_1 = self.v20_1["global_defaults"]["help_rendering_policy"]
        help_policy_20_2 = self.v20_2["command_model"]["help_rendering_policy"]

        self.assertFalse(help_policy_20_1["allow_filtering_or_omissions"])
        self.assertFalse(help_policy_20_2["allow_filtering_or_omissions"])
        self.assertEqual("table", help_policy_20_1["rendering_format"]["command_groups"])
        self.assertEqual("table", help_policy_20_2["rendering_format"]["command_groups"])

        self.assertEqual(
            "comm_help_full",
            self.v20_1["commands"]["help_and_codes"]["Comm Help"]["response_contract"],
        )
        self.assertEqual(
            "comm_help_full",
            self.v20_2["command_model"]["command_output_contract_overrides"]["Comm Help"],
        )

        rc_20_1 = self.v20_1["global_defaults"]["output_contract"]["response_contracts"]["comm_help_full"]
        rc_20_2 = self.v20_2["contracts"]["output_contract"]["response_contracts"]["comm_help_full"]
        for rc in (rc_20_1, rc_20_2):
            with self.subTest(trigger=rc["trigger"]):
                self.assertEqual("conversation_language", rc["language"])
                self.assertEqual(8, len(rc["required_structure"]["sections_in_order"]))
                self.assertEqual(
                    ["Command", "Function"],
                    rc["required_structure"]["command_group_table_columns"],
                )
                self.assertTrue(
                    rc["required_structure"]["accept_localized_section_labels_when_language_supported"]
                )
                self.assertEqual(
                    "Funktion",
                    rc["required_structure"]["command_group_table_columns_localized"]["de"][1],
                )
                self.assertEqual(
                    "Variante",
                    rc["required_structure"]["sci_variant_table_columns_localized"]["de"][0],
                )
                self.assertTrue(
                    rc["required_structure"][
                        "translate_command_descriptions_to_conversation_language_when_supported"
                    ]
                )

    def test_qc_footer_is_terminal(self) -> None:
        output_20_1 = self.v20_1["global_defaults"]["output_contract"]
        output_20_2 = self.v20_2["contracts"]["output_contract"]

        self.assertTrue(output_20_1["qc_footer_termination_contract"]["footer_must_be_last_line"])
        self.assertTrue(output_20_2["qc_footer_termination_contract"]["footer_must_be_last_line"])

        self.assertEqual(
            "whenever_footer_rendered_it_must_be_absolute_last_output_line",
            self.v20_1["qc_matrix"]["display"]["footer_position_rule"],
        )
        self.assertEqual(
            "whenever_footer_rendered_it_must_be_absolute_last_output_line",
            self.v20_2["contracts"]["qc_matrix"]["display"]["footer_position_rule"],
        )

    def test_command_turn_isolation_contract(self) -> None:
        self.assertEqual(
            "forbidden",
            self.v20_1["syntax_rules"]["command_turn_policy"]["retroactive_content_backfill"],
        )
        self.assertEqual(
            "forbidden",
            self.v20_2["parser_contract"]["command_turn_policy"]["retroactive_content_backfill"],
        )

        phi_checks = self.v20_1["global_defaults"]["phi_compliance"]["phi_check"]["checks"]
        self.assertIn("P7_COMMAND_TURN_TERMINAL", {entry["id"] for entry in phi_checks})

        rules = {entry["id"]: entry for entry in self.v20_2["normative_model"]["rules"]}
        self.assertIn("R-CMD-002", rules)
        self.assertEqual("MUST", rules["R-CMD-002"]["modality"])

    def test_language_policy_is_conversation_language_for_explanations(self) -> None:
        language_guard_20_1 = self.v20_1["control_layer"]["components"]["language_rendering_enforcement"]["validator"]
        self.assertFalse(language_guard_20_1["command_and_status_must_be_english"])

        language_contract_20_2 = self.v20_2["contracts"]["output_contract"]["dialog_language_contract"]
        self.assertEqual("conversation_language", language_contract_20_2["status_and_command_language"])

        localized_sources_20_1 = set(
            self.v20_1["global_defaults"]["output_contract"]["dialog_language_contract"]["localized_sources"]
        )
        self.assertIn("meta.rendering.l10n.comm_help", localized_sources_20_1)

        localized_sources_20_2 = set(language_contract_20_2["localized_sources"])
        self.assertIn("command_model.help_rendering_policy.localized", localized_sources_20_2)
        self.assertIn("command_model.command_descriptions_localized", localized_sources_20_2)

    def test_uncertainty_trigger_heuristics_are_defined(self) -> None:
        enforcement_20_1 = self.v20_1["global_defaults"]["uncertainty_enforcement"]
        enforcement_20_2 = self.v20_2["contracts"]["uncertainty"]["enforcement"]

        for enforcement in (enforcement_20_1, enforcement_20_2):
            with self.subTest(scope=enforcement.get("required_output_format", "unknown")):
                self.assertEqual(
                    "any_trigger_condition_or_heuristic_match",
                    enforcement["deterministic_trigger_policy"]["mode"],
                )
                self.assertEqual(
                    "emit_uncertainty_line_before_qc_footer",
                    enforcement["deterministic_trigger_policy"]["if_triggered"],
                )
                self.assertEqual(
                    "U4",
                    enforcement["default_label_mapping"]["temporal_instability_detected"],
                )
                self.assertIn("temporal_instability_detected", enforcement["trigger_heuristics"])
                self.assertIn(
                    "question_examples",
                    enforcement["trigger_heuristics"]["retrieval_metadata_gap_or_tool_unavailable"],
                )


if __name__ == "__main__":
    unittest.main()
