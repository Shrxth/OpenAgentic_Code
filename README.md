# OpenAgentic Code

> A local-first agent orchestration prototype for routing tasks to specialized agents, executing browser workflows, and evaluating agent behavior with explicit execution boundaries.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python\&logoColor=white)](https://www.python.org/)
[![Local LLM](https://img.shields.io/badge/LLM-Ollama-black?logo=ollama)](https://ollama.com/)
[![Browser Automation](https://img.shields.io/badge/Browser-Browser%20Use-111827)](https://github.com/browser-use/browser-use)
[![License](https://img.shields.io/badge/License-TBD-lightgrey)](#license)

OpenAgentic Code is an experimental, local-first framework for coordinating multiple AI agents through a simple execution pipeline:

```text
User Task
   ↓
Task Router
   ↓
Agent Controller
   ├── Coding Agent
   ├── Browser Agent ──→ Ollama / Llama 3.1 8B ──→ Chrome
   └── General Agent
   ↓
Result
```

The project focuses on **clear separation of concerns, bounded execution, lightweight command safety checks, and benchmark-oriented development** rather than a single monolithic agent.

## Why This Project?

As agentic systems become more capable, a practical challenge is deciding **which agent should handle a task, how execution should be constrained, and how behavior should be evaluated**.

OpenAgentic Code explores that problem with a deliberately small architecture that can be extended toward a more production-oriented multi-agent platform.

## Core Capabilities

* **Task routing** — classifies incoming tasks into coding, browser, or general workflows using a lightweight rule-based router.
* **Centralized orchestration** — coordinates classification, policy checks, and agent execution through an `AgentController`.
* **Browser automation** — delegates browser-oriented tasks to Browser Use with a locally hosted Ollama model.
* **Local LLM inference** — uses `llama3.1:8b` through Ollama for browser-agent reasoning.
* **Bounded execution** — browser runs are constrained by a maximum number of steps and a failure limit to reduce runaway behavior.
* **Command policy layer** — blocks a small set of potentially destructive shell commands before execution.
* **Configuration-driven design** — agent assignments, security policy, and evaluation settings are represented in YAML.
* **Initial evaluation suite** — includes representative routing tasks and unit tests for core classification behavior.

## Architecture

### 1. Task Router

`agent/router.py` performs lightweight intent classification by matching task text against coding and browser-oriented keywords. Unmatched requests fall back to the general agent.

### 2. Agent Controller

`agent/controller.py` acts as the orchestration layer. It:

1. Classifies the task.
2. Exposes command-policy validation.
3. Dispatches browser tasks to the browser agent.
4. Returns structured execution metadata for non-browser routes.

### 3. Browser Agent

`agent/browser_agent.py` integrates Browser Use with `ChatOllama` and configures the browser agent for bounded, answer-focused execution.

The browser task is explicitly instructed to stop once the requested answer is obtained, while execution is capped at **4 steps** with **2 allowed failures**.

### 4. Policy Layer

`agent/policies.py` provides a minimal safety boundary by rejecting commands containing configured destructive patterns such as `rm -rf`, `shutdown`, and recursive Windows deletion commands.

> This is intentionally lightweight and should be treated as a prototype policy layer, not a complete sandbox or security boundary.

### 5. Evaluation

`evaluation/benchmark.py` contains an initial representative task set spanning coding, browser, and general requests. `tests/test_router.py` validates the three routing outcomes.

## Repository Structure

```text
OpenAgentic_Code/
├── agent/
│   ├── browser_agent.py     # Browser Use + Ollama execution
│   ├── controller.py        # Central orchestration layer
│   ├── policies.py          # Command safety checks
│   └── router.py            # Task classification and routing
│
├── config/
│   └── settings.yaml        # Project, agent, security, evaluation config
│
├── evaluation/
│   └── benchmark.py         # Initial benchmark task set
│
├── tests/
│   └── test_router.py       # Routing unit tests
│
├── app.py                   # CLI entry point
├── browser_agent.py         # Browser-agent entry/helper module
├── requirements.txt         # Python dependencies
└── README.md
```

## Getting Started

### Prerequisites

You will need:

* Python 3.x
* Google Chrome or a Chromium-based browser
* [Ollama](https://ollama.com/)
* A local Ollama model matching the project configuration (`llama3.1:8b`)

### 1. Clone the repository

```bash
git clone https://github.com/Shrxth/OpenAgentic_Code.git
cd OpenAgentic_Code
```

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare Ollama

Install Ollama, then make sure the configured model is available locally:

```bash
ollama pull llama3.1:8b
```

Start Ollama if it is not already running, then launch the application:

```bash
python app.py
```

You should see an interactive prompt similar to:

```text
OpenAgentic Code
Type a task. Type 'exit' to quit.

Task:
```

Example prompts:

```text
Task: Search this website for the latest product price
Task: Fix this Python bug
Task: Explain recursion
```

Type `exit` to close the application.

## Running Tests

The repository includes routing tests for coding, browser, and general requests.

```bash
pytest -q
```

## Design Principles

### Local-first

The project is designed around local model inference rather than requiring a hosted LLM API for the browser agent.

### Modular orchestration

Routing, execution, policy checks, and evaluation are separated into focused modules so components can evolve independently.

### Bounded autonomy

Browser-agent execution is deliberately constrained to reduce unnecessary exploration and runaway loops.

### Evaluation before expansion

The repository includes a benchmark task set and routing tests, creating a foundation for broader agent evaluation as capabilities grow.

### Explicit safety boundaries

Command filtering is treated as a first-class orchestration concern, even though the current implementation is intentionally minimal.

## Current Scope

OpenAgentic Code is a **prototype / research-oriented implementation**, not a production-ready autonomous agent platform.

Current limitations include:

* Rule-based task routing rather than model-based intent classification.
* A small command blacklist rather than a hardened execution sandbox.
* Browser execution is implemented, while coding and general routes currently return structured routing status rather than executing fully autonomous workflows.
* Evaluation is currently a small task set and routing test suite rather than a comprehensive benchmark.
* Configuration is present, but some runtime values are still defined directly in Python modules.

These constraints are intentional starting points for future iterations.

## Roadmap

Potential next steps include:

* Replace keyword routing with a structured intent classifier.
* Add real coding-agent execution and tool isolation.
* Introduce explicit agent/tool capability schemas.
* Add persistent task state and execution traces.
* Expand benchmark coverage with success, latency, failure, and cost metrics.
* Add stronger command isolation using OS/container-level sandboxes.
* Add structured logging and observability.
* Add CI for tests, linting, type checking, and security checks.
* Support additional local models and model-selection policies.
* Add human approval gates for higher-risk actions.

## Technology Stack

| Layer               | Technology                      |
| ------------------- | ------------------------------- |
| Language            | Python                          |
| Agent orchestration | Custom Python controller/router |
| Browser automation  | Browser Use                     |
| LLM runtime         | Ollama                          |
| Local model         | Llama 3.1 8B                    |
| Configuration       | YAML                            |
| Testing             | pytest                          |
| Browser execution   | Chrome / Chromium               |

## Project Status

**Status:** Active prototype / experimental architecture

The repository is intentionally compact so the orchestration model can be iterated quickly. The primary engineering focus is establishing a clean foundation for **multi-agent routing, constrained execution, evaluation, and local inference** before adding broader autonomous capabilities.

## Contributing

Contributions, architecture discussions, and experiments are welcome. For substantial changes, consider opening an issue first so the proposed change can be discussed before implementation.

## License

No license file is currently included in the repository. Until a license is added, the repository should be treated as **all rights reserved** and reused only according to the author's explicit permission.

## Author

**Shrxth**

GitHub: [@Shrxth](https://github.com/Shrxth)

Repository: [OpenAgentic Code](https://github.com/Shrxth/OpenAgentic_Code)
