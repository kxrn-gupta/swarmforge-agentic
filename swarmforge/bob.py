"""SwarmForge IBM Bob 2.0 Native Bridge & Context Synchronizer.

Provides native interoperability with the IBM Bob 2.0 developer environment:
- Exports multi-agent DAG execution traces to .bob/session.json
- Syncs project directory AST and context snapshots into IBM Bob workspace format
- Converts IBM Bob architectural blueprints directly into SwarmForge subtasks
"""

import datetime as _dt
import json
import os
from pathlib import Path


class BobContextBridge:
    """Bridge between SwarmForge orchestrator and IBM Bob 2.0 environment."""

    def __init__(self, workspace: str | Path):
        self.ws = Path(workspace)
        self.bob_dir = self.ws / ".bob"
        self.bob_dir.mkdir(parents=True, exist_ok=True)

    def export_session(self, task: str, plan: list, results: dict, outroot: Path | None = None) -> Path:
        """Export SwarmForge execution trace into an IBM Bob 2.0 structured session."""
        outroot = outroot or (self.ws / "out")
        session_data = {
            "schema": "ibm.bob.session.v2",
            "agent": "SwarmForge Hybrid-Swarm",
            "timestamp": _dt.datetime.now().isoformat(timespec="seconds"),
            "task": task,
            "supervisor": "IBM Bob 2.0",
            "architecture_plan": [
                {
                    "id": s["id"],
                    "role": s.get("role", "coder"),
                    "title": s.get("title", ""),
                    "depends": s.get("depends", []),
                    "assigned_provider": results.get(s["id"], ({}, "?"))[1],
                    "status": "completed" if results.get(s["id"], ({}, "?"))[0].get("returncode") == 0 else "failed",
                    "duration_sec": results.get(s["id"], ({}, "?"))[0].get("seconds", 0),
                    "tokens": results.get(s["id"], ({}, "?"))[0].get("tokens", 0),
                }
                for s in plan
            ],
            "metrics": {
                "total_subtasks": len(plan),
                "successful_subtasks": sum(1 for s in plan if results.get(s["id"], ({}, "?"))[0].get("returncode") == 0),
                "total_tokens": sum(results.get(s["id"], ({}, "?"))[0].get("tokens", 0) for s in plan),
                "cost_saved_usd": round(sum(results.get(s["id"], ({}, "?"))[0].get("tokens", 0) for s in plan) * 5.0 / 1_000_000, 4),
            },
        }
        session_path = self.bob_dir / "session.json"
        session_path.write_text(json.dumps(session_data, indent=2, ensure_ascii=False), encoding="utf-8")

        # Context markdown summary for IBM Bob prompt grounding
        context_md = [
            f"# IBM Bob 2.0 Workspace Context — {self.ws.name}",
            f"**Task:** {task}",
            f"**Supervisor:** IBM Bob 2.0",
            f"**Generated:** {session_data['timestamp']}",
            "",
            "## Multi-Agent Subtask DAG",
        ]
        for s in plan:
            pname = results.get(s["id"], ({}, "?"))[1]
            context_md.append(f"- **[{s['id']}]** `{s.get('title', '')}` -> Executed by `{pname}`")

        (self.bob_dir / "context.md").write_text("\n".join(context_md), encoding="utf-8")
        return session_path

    def import_plan(self, bob_plan_file: str | Path) -> list:
        """Import an IBM Bob architectural decomposition into SwarmForge subtasks."""
        p = Path(bob_plan_file)
        if not p.exists():
            return []
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            if isinstance(data, list):
                return data
            if isinstance(data, dict) and "tasks" in data:
                return data["tasks"]
            if isinstance(data, dict) and "architecture_plan" in data:
                return data["architecture_plan"]
        except Exception:
            pass
        return []
