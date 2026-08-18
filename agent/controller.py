from agent.router import route_task


class AgentController:
    """Central controller for OpenAgentic Code."""

    def execute(self, task: str) -> dict:
        route = route_task(task)

        return {
            "task": task,
            "route": route,
            "status": "routed",
        }
