from browser_use import Agent, ChatOllama

async def run_browser_agent(task: str):
    llm = ChatOllama(model="llama3.1:8b")

    task = f"""
{task}

IMPORTANT:
This is a single-answer extraction task.
Once you have the requested answer, STOP immediately.
Do not investigate related websites.
Do not click links unless absolutely required.
Do not perform additional research.
Return the answer you found.
"""

    agent = Agent(
        task=task,
        llm=llm,
        use_vision=False,
        flash_mode=True,
        max_failures=2,
    )

    return await agent.run(max_steps=4)
