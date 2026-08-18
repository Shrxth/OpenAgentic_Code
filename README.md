<div align="center">

# ⚡ OpenAgentic Code

### Local-First AI Agent Orchestration

**Route tasks. Select specialized agents. Execute tools. Run AI locally.**

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black?style=for-the-badge&logo=ollama&logoColor=white)
![Browser Use](https://img.shields.io/badge/Browser%20Use-Automation-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Functional%20Prototype-2ea44f?style=for-the-badge)

</div>

---

## 🧠 Overview

**OpenAgentic Code** is a local-first AI agent orchestration project that explores how multiple specialized AI agents can be coordinated through a unified controller.

Instead of treating an AI system as a single chatbot, the project separates task understanding, routing, agent selection, execution, tool interaction, and result generation.

The current implementation demonstrates this architecture through:

- Python-based task routing
- A unified agent controller
- Browser Use browser automation
- Chrome execution
- Local Ollama inference
- Llama 3.1 8B
- Basic execution policies
- Bounded browser-agent execution
- End-to-end task verification

### Core Workflow

```text
User Task
    ↓
Task Router
    ↓
Agent Controller
    ↓
Specialized Agent
    ↓
Tools / Local LLM
    ↓
Execution
    ↓
Verification
    ↓
Final Result