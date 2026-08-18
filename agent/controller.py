import asyncio

from agent.router import route_task
from agent.policies import is_command_allowed
from agent.browser_agent import run_browser_agent


class AgentController:
    """Unified controller for OpenHands and Browser Use."""

    def classify(self, task: str) -> str:
        return route_task(task)

    def check_command(self, command: str) -> bool:
        return is_command_allowed(command)

    def execute(self, task: str):

        agent = self.classify(task)

        if agent == "browser":
            return asyncio.run(
                run_browser_agent(task)
            )

        return {
            "task": task,
            "selected_agent": agent,
            "status": "ready",
        }
