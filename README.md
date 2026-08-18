# OpenAgentic Code

### Local-first AI agent orchestration for intelligent task execution

OpenAgentic Code is an experimental AI agent orchestration system that routes user tasks to specialized agents and executes them using local AI models and browser automation.

> **User Task → Router → Controller → Specialized Agent → Tools → Verified Result**

---

## ⚡ What It Does

OpenAgentic Code provides a unified interface for interacting with different AI agents.

A task is classified by the router and delegated to the appropriate execution path.

```text
                         ┌─────────────────┐
                         │      User       │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │   Task Router   │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │ Agent Controller│
                         └────────┬────────┘
                                  │
                    ┌─────────────┼─────────────┐
                    ▼             ▼             ▼
              ┌──────────┐  ┌───────────┐  ┌──────────┐
              │  Coding  │  │  Browser  │  │ General  │
              │   Agent  │  │   Agent   │  │   Agent  │
              └──────────┘  └─────┬─────┘  └──────────┘
                                  │
                                  ▼
                           ┌─────────────┐
                           │   Ollama    │
                           │ Local LLM   │
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