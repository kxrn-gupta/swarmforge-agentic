# Project Context Overview

## Repository Root (`E:\swarmforge_events\swarmforge-agentic`)

| Directory / File | Purpose | Associated Hackathon / Event |
|------------------|---------|------------------------------|
| `PRESENTATION_SLIDES.html` | HTML slide deck (IBM Bob 2.0 pitch) | **IBM Bob 2.0 Hackathon** |
| `ibm_bob_session.json` | Exported session data for IBM Bob 2.0 bridge | **IBM Bob 2.0 Hackathon** |
| `ibm_bob_session.md` | Human‑readable context report for IBM Bob 2.0 | **IBM Bob 2.0 Hackathon** |
| `README.md` | General project description, setup, usage, and a brief IBM Bob 2.0 section | **IBM Bob 2.0 Hackathon** |
| `agents.json` | Agent registry; includes an entry for the `bob` bridge used in the IBM hackathon | **IBM Bob 2.0 Hackathon** |
| `swarmforge/` (package) | Core SwarmForge library – **shared** across all events | *All events* |
| `tests/` | Unit‑test suite (including `test_bob.py`) – validates functionality for every hackathon | *All events* |
| `docs/`, `examples/` | Documentation and example scripts – **shared** resources | *All events* |
| `publish.*`, `setup.*`, `pyproject.toml` | Build / publishing utilities – **shared** | *All events* |
| `.git/`, `.gitignore`, `LICENSE` | Standard repo metadata – **shared** | *All events* |

## Hackathon‑Specific Assets

### 1️⃣ IBM Bob 2.0 (Lablab.ai) – 21 Sep → 27 Sep 2026
- **Slide deck** – `PRESENTATION_SLIDES.html` (HTML) – also acceptable as PDF or PPTX after conversion.
- **Session export** – `ibm_bob_session.json` (machine‑readable) and `ibm_bob_session.md` (human‑readable).
- **Bridge code** – `swarmforge/bob.py` (provides `BobContextBridge`).
- **Tests** – `tests/test_bob.py` ensures the bridge works.

### 2️⃣ Dark Factory / Spotify Pitch – 28 Sep → 5 Oct 2026
> No dedicated files are present yet in this repository.  When assets are created (e.g., architecture diagrams, demo scripts, or a separate slide deck), place them in a new sub‑directory `dark_factory/` and update this `CONTEXT.md` accordingly.

## How to Use This File
- **Quick reference**: Open `CONTEXT.md` in any editor to see which files belong to which competition.
- **Avoid mix‑ups**: When working on a specific hackathon, filter your IDE view by the "Associated Hackathon / Event" column.
- **Future updates**: Add new rows for any additional files (e.g., `dark_factory/plan.pdf`) as the project evolves.

---
*Generated on 2026‑09‑24 by Antigravity to improve project clarity.*
