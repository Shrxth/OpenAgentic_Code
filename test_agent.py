from agent.controller import AgentController

controller = AgentController()

tasks = [
    "Fix this Python bug",
    "Search this website",
    "Explain how an API works",
]

for task in tasks:
    result = controller.execute(task)
    print(result)
