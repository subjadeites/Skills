import os
import sys
import unittest


SCRIPT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, SCRIPT_DIR)

import codeflow_skill_flow


class CodeflowSkillFlowTests(unittest.TestCase):
    def test_parse_control_action(self):
        self.assertEqual(codeflow_skill_flow.parse_control_action("/codeflow"), "activate")
        self.assertEqual(codeflow_skill_flow.parse_control_action("/codeflow on"), "activate")
        self.assertEqual(codeflow_skill_flow.parse_control_action("/codeflow status"), "status")
        self.assertEqual(codeflow_skill_flow.parse_control_action("/codeflow off"), "deactivate")
        self.assertEqual(codeflow_skill_flow.parse_control_action("callback_data: cfe:install"), "install")
        self.assertEqual(codeflow_skill_flow.parse_control_action("/other"), "unsupported")

    def test_infer_message_route_for_telegram(self):
        direct = codeflow_skill_flow.infer_message_route("agent:main:telegram:direct:123")
        self.assertEqual(direct, {"channel": "telegram", "target": "123"})

        topic = codeflow_skill_flow.infer_message_route("agent:main:telegram:group:-1001:topic:55")
        self.assertEqual(
            topic,
            {"channel": "telegram", "target": "-1001", "threadId": "55"},
        )

        self.assertIsNone(codeflow_skill_flow.infer_message_route("agent:main:discord:thread:abc"))

    def test_build_control_reply_keeps_buttons_when_supported(self):
        status = {
            "guard": {"active": True, "bindingKey": "telegram:-1001:55"},
            "recommendation": {
                "action": "install",
                "message": "Soft mode is active.",
                "buttons": [[{"text": "Install Enforcer", "callback_data": "cfe:install"}]],
            },
            "installCommand": "bash /tmp/codeflow enforcer install --restart",
        }

        reply = codeflow_skill_flow.build_control_reply("activate", status, buttons_supported=True)

        self.assertEqual(reply["buttons"], [[{"text": "Install Enforcer", "callback_data": "cfe:install"}]])
        self.assertIn("Codeflow guard activated", reply["message"])
        self.assertIn("Binding: telegram:-1001:55", reply["message"])
        self.assertNotIn("Install: bash /tmp/codeflow", reply["message"])

    def test_build_control_reply_falls_back_to_install_command_without_buttons(self):
        status = {
            "guard": {"active": False, "state": "unbound"},
            "recommendation": {
                "action": "install",
                "message": "Soft mode is active.",
                "buttons": [[{"text": "Install Enforcer", "callback_data": "cfe:install"}]],
            },
            "installCommand": "bash /tmp/codeflow enforcer install --restart",
        }

        reply = codeflow_skill_flow.build_control_reply("status", status, buttons_supported=False)

        self.assertEqual(reply["buttons"], [])
        self.assertIn("Codeflow guard is not active", reply["message"])
        self.assertIn("Install: bash /tmp/codeflow enforcer install --restart", reply["message"])


if __name__ == "__main__":
    unittest.main()
