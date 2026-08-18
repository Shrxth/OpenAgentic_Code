# OpenAgentic Code

### Local-First AI Agent Orchestration

OpenAgentic Code is an experimental AI-agent orchestration system that routes user tasks to specialized agents and executes browser tasks using a locally hosted LLM.

## Overview

The project separates task understanding, routing, agent selection, execution, browser automation, and result generation.

**Workflow:**

`User Task → Router → Controller → Specialized Agent → Tools → Result`

## Features

- Task classification and routing
- Central agent controller
- Specialized agent architecture
- Browser automation with Browser Use
- Local LLM inference with Ollama
- Llama 3.1 8B support
- Chrome browser execution
- Information extraction from webpages
- Basic execution policies
- Bounded agent execution
- Failure limits to prevent runaway loops
- Local-first architecture

## Architecture

```text
User Task
   |
   v
Task Router
   |
   v
Agent Controller
   |
   +----------------+----------------+
   |                |                |
   v                v                v
Coding Agent   Browser Agent   General Agent
                     |
                     v
                  Ollama
                     |
                     v
              Llama 3.1 8B
                     |
                     v
                  Chrome
                     |
                     v
                  Result
