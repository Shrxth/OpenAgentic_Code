# OrchestAgent

> A local-first AI agent orchestration prototype for routing tasks to specialized agents, executing browser workflows, and evaluating agent behavior with explicit execution boundaries.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python\&logoColor=white)](https://www.python.org/)
[![Local LLM](https://img.shields.io/badge/LLM-Ollama-black?logo=ollama)](https://ollama.com/)
[![Browser Automation](https://img.shields.io/badge/Browser-Browser%20Use-111827)](https://github.com/browser-use/browser-use)
[![License](https://img.shields.io/badge/License-TBD-lightgrey)](#license)

**OrchestAgent** is an experimental, local-first framework for coordinating specialized AI agents through a modular execution pipeline.

The system is designed around a simple principle:

> **Understand the task → route it to the appropriate agent → execute within defined boundaries → return the result.**

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

The project focuses on **separation of concerns, modular agent orchestration, bounded execution, lightweight command safety, local inference, and evaluation-driven development** rather than relying on a single monolithic AI agent.

---

## Why OrchestAgent?

As AI systems move from simple question-answering toward autonomous task execution, an important engineering challenge emerges:

**How should a system decide which agent should handle a task, what tools that agent should have access to, and how its execution should be constrained and evaluated?**

OrchestAgent explores this problem through a deliberately modular architecture that can evolve toward a more capable multi-agent platform.

---

## Core Capabilities

* **Task routing** — classifies incoming tasks into coding, browser, or general workflows using a lightweight rule-based router.
* **Centralized orchestration** — coordinates task classification, policy checks, and agent execution through an `AgentController`.
* **Browser automation** — delegates browser-oriented tasks to Browser Use with a locally hosted Ollama model.
* **Local LLM inference** — uses `llama3.1:8b` through Ollama for browser-agent reasoning.
* **Bounded execution** — browser-agent runs are constrained by a maximum number of steps and a failure limit to reduce unnecessary or runaway execution.
* **Command policy layer** — provides an initial safety boundary against a small set of potentially destructive shell commands.
* **Configuration layer** — represents agent assignments, security settings, and evaluation settings through YAML.
* **Initial evaluation suite** — includes representative task definitions and unit tests for core routing behavior.

---

## Architecture

### 1. Task Router

`agent/router.py` provides the initial task-classification layer.

It analyzes the user's task and checks for coding- and browser-related keywords.

For example:

```text
"Fix this Python bug"
        ↓
     coding
```

```text
"Search this website"
        ↓
     browser
```

Tasks that do not match the defined categories fall back to:

```text
general
```

The current implementation intentionally uses deterministic keyword-based routing, making the behavior simple to understand and test.

---

### 2. Agent Controller

`agent/controller.py` provides the central orchestration layer.

The controller is responsible for:

1. Receiving a task from the application.
2. Asking the router to classify the task.
3. Providing access to command-policy validation.
4. Dispatching browser tasks to the browser agent.
5. Returning structured routing information for routes that do not yet have autonomous execution implemented.

The controller provides the central coordination point between the application's input layer and its agent capabilities.

---

### 3. Browser Agent

`agent/browser_agent.py` integrates Browser Use with `ChatOllama`.

The browser agent receives a high-level task and is configured for focused, bounded execution.

The current implementation instructs the agent to:

* Obtain the requested answer.
* Avoid unnecessary investigation.
* Avoid unrelated websites.
* Avoid unnecessary navigation.
* Stop once the requested answer has been obtained.

Execution is currently limited to:

* **Maximum steps:** 4
* **Maximum failures:** 2

This provides an initial form of **bounded agent autonomy**.

---

### 4. Local LLM Runtime

OrchestAgent uses **Ollama** as the local inference runtime.

The browser agent connects to:

```text
llama3.1:8b
```

The architecture is therefore:

```text
Browser Use
     ↓
ChatOllama
     ↓
Ollama
     ↓
Llama 3.1 8B
```

Ollama is responsible for running the model locally, while Llama 3.1 8B provides the underlying language-model reasoning.

---

### 5. Browser Execution

Browser Use operates against a local Chrome/Chromium browser environment.

The overall browser-agent flow is:

```text
User Task
    ↓
Task Router
    ↓
Agent Controller
    ↓
Browser Agent
    ↓
Browser Use
    ↓
Ollama
    ↓
Llama 3.1 8B
    ↓
Browser Action
    ↓
Chrome / Chromium
    ↓
Webpage
    ↓
Result
```

This separation allows the model to reason about the task while Browser Use and the browser environment handle the actual web interaction.

---

### 6. Policy Layer

`agent/policies.py` provides a lightweight command-safety layer.

The current implementation blocks configured destructive command patterns such as:

```text
rm -rf
shutdown
del /s
format
```

> **Important:** This is a prototype policy mechanism, not a production-grade security sandbox. Robust agent execution would require stronger isolation mechanisms such as containers, OS-level permissions, sandboxing, resource limits, and explicit approval controls.

---

### 7. Evaluation

`evaluation/benchmark.py` provides an initial set of representative tasks covering:

* Coding
* Browser
* Navigation
* General knowledge

`tests/test_router.py` provides unit tests for the routing layer.

Together, these establish the initial foundation for evaluating both **software correctness** and, eventually, **agent task performance**.

---

## Repository Structure

```text
OrchestAgent/
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
├── browser_agent.py         # Browser-agent helper module
├── requirements.txt         # Python dependencies
└── README.md
```

---

## Getting Started

### Prerequisites

You will need:

* Python 3.x
* Google Chrome or a Chromium-based browser
* [Ollama](https://ollama.com/)
* A local Ollama model matching the project configuration: `llama3.1:8b`

---

### 1. Clone the Repository

```bash
git clone https://github.com/Shrxth/OrchestAgent.git
cd OrchestAgent
```

---

### 2. Create a Virtual Environment

#### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Prepare Ollama

Install Ollama and make sure the configured model is available locally:

```bash
ollama pull llama3.1:8b
```

Ensure Ollama is running, then start OrchestAgent:

```bash
python app.py
```

You should see:

```text
OrchestAgent
Type a task. Type 'exit' to quit.

Task:
```

Example tasks:

```text
Task: Search this website for the latest product price
```

```text
Task: Fix this Python bug
```

```text
Task: Explain recursion
```

Type:

```text
exit
```

to close the application.

---

## Running Tests

The repository includes routing tests covering coding, browser, and general task classification.

Run the test suite with:

```bash
pytest -q
```

---

## Design Principles

### Local-First

The project prioritizes local model inference rather than requiring a hosted LLM API for the browser-agent workflow.

This provides a foundation for:

* Local experimentation
* Reduced dependence on external model APIs
* Greater control over the inference environment
* Potentially improved data privacy

---

### Modular Orchestration

Task routing, agent control, browser execution, policy checks, configuration, and evaluation are separated into focused components.

This makes the architecture easier to extend and maintain.

---

### Bounded Autonomy

Agentic systems can potentially continue taking actions until they reach their objective.

OrchestAgent introduces explicit execution limits to reduce unnecessary exploration and runaway execution.

---

### Deterministic Routing

The initial router intentionally uses simple rule-based classification.

This provides:

* Predictable behavior
* Easy debugging
* Fast execution
* Straightforward unit testing

A future implementation can replace this with structured model-based intent classification.

---

### Evaluation Before Expansion

The project establishes initial benchmark tasks and automated tests before expanding the number of agents and capabilities.

This provides a foundation for measuring whether future changes actually improve system behavior.

---

### Explicit Safety Boundaries

Command filtering is treated as an explicit part of the orchestration architecture.

The current implementation is intentionally minimal and is expected to evolve toward stronger execution isolation.

---

## Current Scope

OrchestAgent is currently an **experimental prototype**, not a production-ready autonomous agent platform.

The current implementation has several intentional limitations:

* Task routing is keyword-based rather than model-based.
* Browser-agent execution is the primary autonomous execution path.
* Coding and general routes currently return structured routing/status information rather than executing fully autonomous workflows.
* The command policy is a lightweight blacklist rather than a hardened execution sandbox.
* The evaluation suite is currently small and primarily focused on routing behavior.
* Some runtime configuration remains defined directly within Python modules rather than being fully driven by YAML.

These limitations provide clear areas for future engineering development.

---

## Roadmap

### Agent Orchestration

* Replace keyword routing with structured intent classification.
* Introduce explicit agent capability definitions.
* Add additional specialized agents.
* Support dynamic agent selection based on task requirements.

### Execution

* Implement a dedicated coding-agent execution path.
* Implement a general-purpose agent.
* Introduce persistent task state.
* Add execution traces and structured agent memory.

### Security

* Replace basic command blacklisting with stronger execution isolation.
* Introduce container-based execution.
* Add permission and resource controls.
* Add human approval gates for high-risk operations.

### Evaluation

* Expand benchmark coverage.
* Measure task success rate.
* Measure execution latency.
* Track failure rate.
* Track resource/model usage.
* Compare different routing strategies and models.

### Engineering

* Add structured logging.
* Add observability.
* Add continuous integration.
* Add linting and type checking.
* Add automated security checks.
* Improve configuration management.

---

## Technology Stack

| Layer                | Technology                        |
| -------------------- | --------------------------------- |
| Programming Language | Python                            |
| Agent Orchestration  | Custom Python Controller / Router |
| Browser Automation   | Browser Use                       |
| LLM Runtime          | Ollama                            |
| Local Model          | Llama 3.1 8B                      |
| Configuration        | YAML                              |
| Testing              | pytest                            |
| Browser Execution    | Chrome / Chromium                 |

---

## Project Status

**Status:** Active Prototype / Experimental Architecture

OrchestAgent is intentionally compact at its current stage.

The primary engineering focus is establishing a clean foundation for:

* Multi-agent routing
* Specialized agent execution
* Local model inference
* Bounded autonomy
* Safety controls
* Benchmark-driven evaluation

The architecture is designed to evolve incrementally toward a more capable and production-oriented agent orchestration platform.

---

## Contributing

Contributions, architecture discussions, experiments, and improvements are welcome.

For substantial changes, consider opening an issue first to discuss the proposed architecture or implementation before submitting a change.

---

## License

No license file is currently included in the repository.

Until a license is added, the repository should be treated as **all rights reserved** and reused only with the author's explicit permission.

---

## Author

**Shrxth**

GitHub: [@Shrxth](https://github.com/Shrxth)

Repository: [OrchestAgent](https://github.com/Shrxth/OrchestAgent)
