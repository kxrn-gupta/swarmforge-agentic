import json
import tempfile
import unittest
from pathlib import Path
from swarmforge.bob import BobContextBridge


class TestBobBridge(unittest.TestCase):
    def test_export_session_creates_valid_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            bridge = BobContextBridge(tmp)
            plan = [
                {"id": "t1", "role": "coder", "title": "Subtask 1", "depends": []}
            ]
            results = {
                "t1": ({"returncode": 0, "seconds": 1.5, "tokens": 120}, "opencode")
            }
            out_file = bridge.export_session("Test Task", plan, results)
            self.assertTrue(out_file.exists())
            data = json.loads(out_file.read_text(encoding="utf-8"))
            self.assertEqual(data["schema"], "ibm.bob.session.v2")
            self.assertEqual(data["supervisor"], "IBM Bob 2.0")
            self.assertEqual(len(data["architecture_plan"]), 1)
            self.assertEqual(data["metrics"]["total_subtasks"], 1)
            self.assertEqual(data["metrics"]["total_tokens"], 120)

    def test_import_plan_from_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            bridge = BobContextBridge(tmp)
            plan_file = Path(tmp) / "plan.json"
            plan_data = [{"id": "b1", "title": "Bob Task", "depends": []}]
            plan_file.write_text(json.dumps(plan_data), encoding="utf-8")
            imported = bridge.import_plan(plan_file)
            self.assertEqual(len(imported), 1)
            self.assertEqual(imported[0]["id"], "b1")


if __name__ == "__main__":
    unittest.main()
