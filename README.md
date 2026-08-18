<div align="center">

# ⚡ OpenAgentic Code

### Local-First AI Agent Orchestration

**Route tasks. Select specialized agents. Execute tools. Run AI locally.**

---

</div>

OpenAgentic Code is a local-first AI agent orchestration project exploring how specialized AI agents can be coordinated through a unified controller.

Instead of treating an AI system as a single chatbot, the project separates:

> Task Understanding → Routing → Agent Selection → Execution → Tool Interaction → Verification → Result

The current implementation demonstrates this architecture through Python-based task routing, a unified agent controller, Browser Use, Chrome automation, local Ollama inference, basic execution policies, and bounded browser-agent execution.

## 🎯 Project Goals

The project was created to explore the engineering challenges involved in building a practical AI-agent orchestration system.

- Route different types of tasks to specialized agents
- Separate orchestration from individual agent execution
- Integrate browser automation with AI agents
- Run the demonstrated workflow locally
- Reduce dependency on paid hosted LLM APIs
- Introduce basic execution policies
- Control potentially runaway agent execution
- Establish a foundation for future multi-agent capabilities
- Maintain a reproducible Git/GitHub development workflow
## 🏗️ Architecture

┌──────────────────┐
│       USER       │
└────────┬─────────┘
│
▼
┌──────────────────┐
│   TASK ROUTER    │
└────────┬─────────┘
│
▼
┌─────────────────────┐
│   AGENT CONTROLLER  │
└──────────┬──────────┘
│
┌─────────────┼─────────────┐
│             │             │
▼             ▼             ▼
┌──────────┐  ┌──────────┐  ┌──────────┐
│ Coding   │  │ Browser  │  │ General  │
│  Agent   │  │  Agent   │  │  Agent   │
└──────────┘  └────┬─────┘  └──────────┘
│
▼
┌─────────────┐
│   Ollama    │
│ Local Model │
└──────┬──────┘
│
▼
┌─────────────┐
│    Chrome   │
└──────┬──────┘
│
▼
┌─────────────┐
│    Result   │
└─────────────┘
## ✨ Current Capabilities

| Capability | Status |
|---|:---:|
| Task classification | ✅ |
| Agent routing | ✅ |
| Unified agent controller | ✅ |
| Browser agent | ✅ |
| Local Ollama integration | ✅ |
| Chrome automation | ✅ |
| Browser information extraction | ✅ |
| Bounded browser execution | ✅ |
| Basic execution policy layer | ✅ |
| Router tests | ✅ |
| End-to-end browser verification | ✅ |
| Advanced multi-agent collaboration | 🔬 Future |
| Production-grade sandboxing | 🔬 Future |
| Full autonomous coding-agent execution | 🔬 Future |

## 🧪 Verified End-to-End Execution

The final browser workflow was successfully verified locally.

Input
Open https://example.com and tell me the page title
Execution
Natural Language Task
↓
Task Router
↓
Browser Agent
↓
Ollama / Llama 3.1 8B
↓
- Browser Use
↓
- Chrome
↓
Page Information Extraction
↓
Final Result
Final Result
> The title of the webpage is 'Example Domain'.

This verified the complete local execution path:

> Task → Routing → Agent Selection → Local LLM → Browser Automation → Information Extraction → Final Response

## 🛠️ Engineering Journey

The project evolved through multiple stages of integration, debugging, and verification rather than being built as a single-pass application.

### Phase 1 — Open-Source Foundation

The project began from an existing open-source AI-agent ecosystem rather than attempting to recreate browser automation and agent infrastructure from scratch.

The project explored integration with technologies including:

- OpenHands
- Browser Use
- Ollama

The goal was to build an orchestration and integration layer around existing technologies while preserving upstream attribution.

### Phase 2 — Local Development Environment

Development was performed on Windows using:

- Python 3.12
- VS Code
- Git
- GitHub
- Python virtual environments
- Ollama
- Chrome

A dedicated Python virtual environment was created.

Windows PowerShell execution-policy restrictions initially prevented direct activation of the virtual environment.

Instead of changing system-wide security settings, the project was executed directly through the environment's Python executable:

`.\.venv\Scripts\python.exe`

This provided a reliable execution path without requiring shell activation.

### Phase 3 — Dependency Integration

The project required multiple AI-agent and automation dependencies.

During installation, dependency conflicts appeared across packages including:

- OpenAI
- AnyIO
- Browser Use
- LangChain-related packages
- OpenHands-related packages
- Streamlit-related packages
- Supporting libraries

This demonstrated a practical challenge with rapidly evolving AI-agent ecosystems:

> Different frameworks and versions can impose tightly coupled and sometimes incompatible dependency requirements.

The implementation was simplified around the components required for the demonstrated workflow instead of continuously adding unnecessary framework dependencies.

### Phase 4 — Task Router

A dedicated task router was introduced to classify incoming tasks and select an appropriate agent.

The routing model became:

User Task
│
┌─────────────┼─────────────┐
▼             ▼             ▼
Coding        Browser        General
│             │             │
▼             ▼             ▼
Coding Agent  Browser Agent  General Agent

Representative routing tests included:

Fix this Python bug
Search this website
Explain how an API works

This established the first working layer of task specialization.

### Phase 5 — Unified Agent Controller

A central AgentController was introduced to separate:

Task classification
Policy checks
Agent selection
Agent execution

Conceptually:

AgentController
│
├── classify()
├── check_command()
└── execute()

This created a single orchestration interface instead of coupling the CLI directly to individual agents.

### Phase 6 — Browser Agent Integration

Browser automation was connected to the controller using Browser Use.

The initial implementation attempted to use a LangChain/OpenAI integration.

This produced an import failure because langchain_openai was not available in the environment.

The dependency approach was subsequently simplified to avoid adding unnecessary framework dependencies to the browser execution path.

### Phase 7 — Transition to Local Ollama

The project was moved toward a local-first execution model.

Ollama was installed and verified locally.

The selected model was:

Llama 3.1 8B

The model was successfully downloaded and made available locally.

This enabled the demonstrated browser-agent workflow to run without requiring a paid hosted LLM API.

### Phase 8 — Model Compatibility Problem

The first local browser-agent execution exposed a multimodal compatibility issue.

Browser Use attempted to provide multimodal information to the selected model, producing an error equivalent to:

Multimodal data provided, but model does not support multimodal requests.

The issue was caused by a mismatch between the browser agent's vision requirements and the capabilities of the selected local model configuration.

The browser agent was therefore configured for text-based execution:

`use_vision=False`

This allowed the browser workflow to operate using browser state and extracted text instead of unsupported multimodal requests.

### Phase 9 — Browser-Agent Loop Problem

After the multimodal issue was addressed, another problem became apparent.

The agent could continue acting after it had effectively found the requested information.

Observed behavior included:

- Repeated clicks
- Attempts to interact with unavailable elements
- Repeated navigation
- Additional exploration
- Stale browser-state interactions
- Continued reasoning after the answer had already been found

The resulting pattern could become:

Task Completed
↓
Agent Continues
↓
Unnecessary Action
↓
Action Fails
↓
Retry
↓
Another Action
↓
Potential Loop

This became an important agent-control problem.

### Phase 10 — Bounded Agent Execution

To prevent uncontrolled execution, explicit execution boundaries were introduced.

The browser agent was configured with:

`max_steps=4`

and:

`max_failures=2`

The task prompt was also strengthened with explicit completion instructions:

> This is a single-answer extraction task.

> Once you have the requested answer, STOP immediately.

> Do not investigate related websites.

> Do not click links unless absolutely required.

> Do not perform additional research.

> Return the answer you found.

The resulting execution strategy became:

Perform Requested Task
↓
Extract Answer
↓
Stop Within Step Budget

rather than allowing the agent to continue exploring indefinitely.

### Phase 11 — Successful Browser Execution

After the execution boundaries were introduced, the browser workflow successfully completed the example task.

The agent:

1. Identified the target URL
2. Navigated to example.com
3. Loaded the webpage
4. Extracted the page title
5. Recognized that the requested information had been found
6. Returned the final answer
7. Terminated the browser session cleanly

Final output:

> The title of the webpage is 'Example Domain'.

This became the primary end-to-end verification of the local browser-agent pipeline.

### Phase 12 — Git & GitHub Development

The project was developed using incremental Git commits and pushed to GitHub throughout the implementation.

Repository:

[**github.com/Shrxth/OpenAgentic_Code**](https://github.com/Shrxth/OpenAgentic_Code)

The development history includes changes covering:

- Initial project setup
- Agent dependencies
- Task routing
- Unified controller
- Browser-agent integration
- Local Ollama integration
- Browser execution
- Execution bounding
- Testing
- Documentation

The incremental Git history provides a traceable record of the project's development.

## 📁 Project Structure

`OpenAgentic_Code/`
│
├── agent/
`│   ├── controller.py`
`│   ├── router.py`
`│   ├── policies.py`
`│   └── browser_agent.py`
│
├── tests/
`│   └── test_router.py`
│
`├── app.py`
`├── test_agent.py`
`├── config.py`
`├── requirements.txt`
`├── .gitignore`
`└── README.md`
## 🔐 Safety & Execution Policies

A basic policy layer was introduced to provide an initial boundary around potentially unsafe command execution.

The current policy implementation is intentionally lightweight.

It should not be considered a production security boundary.

A production-grade autonomous-agent platform would require stronger controls including:

- Sandboxed execution
- Process isolation
- Capability-based permissions
- Filesystem restrictions
- Network restrictions
- Credential protection
- Audit logging
- Human approval for privileged actions
- Stronger command classification
- Tool-level authorization

These remain future engineering opportunities.

## 🧠 Technical Lessons

### 1. Agent frameworks are not plug-and-play

AI-agent frameworks can have tightly coupled and rapidly changing dependency requirements.

Integrating multiple frameworks requires careful version management and a clear separation between essential and optional dependencies.

### 2. Model capability matters

A browser automation framework may support multimodal workflows while a selected local model does not.

The orchestration layer therefore needs to account for the actual capabilities of the selected model.

### 3. Agent autonomy requires boundaries

An agent may continue acting even after it has effectively completed the task.

Step budgets, failure limits, and explicit completion conditions provide practical control over execution.

### 4. Browser state is dynamic

Element indexes can become invalid when pages change.

Browser agents therefore need to tolerate stale state and execution failures.

### 5. Local-first AI introduces different engineering trade-offs

Local inference reduces dependence on hosted APIs but introduces additional considerations around:

- Hardware
- Model capabilities
- Package compatibility
- Inference performance
- Runtime configuration
## 🧩 Technology Stack

| Layer | Technology |
|---|---|
| Programming Language | Python 3.12 |
| Local LLM Runtime | Ollama |
| Model | Llama 3.1 8B |
| Browser Automation | Browser Use |
| Browser | Chrome / Chromium |
| Environment | Python virtual environment |
| Version Control | Git + GitHub |
| Development Environment | VS Code |

## 🚀 Quick Start

Requirements
Python 3.12+
- Ollama
Chrome / Chromium
- Git
Clone
`git clone https://github.com/Shrxth/OpenAgentic_Code.git`
`cd OpenAgentic_Code`
Create Virtual Environment
`python -m venv .venv`
Install Dependencies
`.\.venv\Scripts\python.exe -m pip install -r requirements.txt`
Download Local Model
`ollama pull llama3.1:8b`
Run
`.\.venv\Scripts\python.exe app.py`

Then enter a natural-language task.

Example:

`Task: Open https://example.com and tell me the page title`
## 📊 Current Architecture vs. Future Direction

Current
User
↓
Router
↓
Controller
↓
Browser Agent
↓
- Ollama
↓
- Browser Use
↓
- Chrome
↓
Result
Future Direction
┌──────────────┐
│    Planner   │
└──────┬───────┘
│
▼
┌──────────────┐
│ Smart Router │
└──────┬───────┘
│
┌─────────────────┼─────────────────┐
▼                 ▼                 ▼
Coding Agent      Browser Agent     Research Agent
│                 │                 │
└─────────────────┼─────────────────┘
▼
Verification Layer
│
▼
Safety / Policy
│
▼
Final Result

> The future architecture is intentionally shown as future direction, not as functionality already implemented.

## 🚧 Current Limitations

The current system is a functional prototype, not a production autonomous-agent platform.

Current limitations include:

- Basic task routing
- Basic policy enforcement
- Limited agent specialization
- Limited recovery strategies
- Local-model capability constraints
- No production sandbox
- No comprehensive benchmark framework
- No advanced observability system
- No graphical interface
- Limited multi-agent collaboration
## 🗺️ Roadmap

- [ ] Advanced task planning
- [ ] More specialized agents
- [ ] Smarter routing
- [ ] Agent-to-agent collaboration
- [ ] Stronger tool permissions
- Sandboxed execution
- [ ] Human approval workflows
- [ ] Automated evaluation framework
- [ ] Execution tracing and observability
- [ ] Improved failure recovery
- [ ] Additional local models
- [ ] Optional graphical interface
- [ ] Production deployment architecture
## 🌐 Open-Source Foundation & Attribution

OpenAgentic Code integrates and builds upon open-source technologies including:

- OpenHands
- Browser Use
- Ollama

The respective upstream projects, authors, and licenses remain acknowledged.

This repository represents an integration, adaptation, and experimentation project and does not claim authorship of the underlying upstream technologies.

Upstream licenses and attribution requirements should be preserved when redistributing relevant components.

## 📌 Project Status

🟢 Functional Prototype — Verified Locally

The current implementation successfully demonstrates:

Natural Language Task
↓
Task Routing
↓
Agent Selection
↓
Local LLM
↓
Browser Automation
↓
Information Extraction
↓
Bounded Execution
↓
Final Result

The browser-agent workflow has been successfully executed end-to-end using a local Ollama model and Chrome.

## 👤 Author

Shrxth

Areas explored through this project:

AI Agents · LLMs · Local AI · Browser Automation · Task Routing · Python · Agent Orchestration · AI Safety

<div align="center">
⚡ OpenAgentic Code

Explore → Route → Execute → Verify

Built with Python, Ollama, Browser Use, and open-source AI technologies.

</div>
