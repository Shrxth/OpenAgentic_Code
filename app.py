from agent.controller import AgentController

controller = AgentController()

print("OpenAgentic Code")
print("Type a task. Type 'exit' to quit.")

while True:
    task = input("\nTask: ").strip()

    if task.lower() == "exit":
        break

    if not task:
        continue

    result = controller.execute(task)

    print(f"Agent: {result['selected_agent']}")
    print(f"Status: {result['status']}")
