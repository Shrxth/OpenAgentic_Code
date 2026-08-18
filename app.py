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

    try:
        result = controller.execute(task)

        if hasattr(result, "final_result"):
            print("\nResult:")
            print(result.final_result())
        else:
            print(f"\nAgent: {result.get('selected_agent', 'unknown')}")
            print(f"Status: {result.get('status', 'unknown')}")

    except Exception as e:
        print(f"\nAgent error: {e}")
