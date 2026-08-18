from browser_use import Agent, ChatOllama

async def run_browser_agent(task: str):
    llm = ChatOllama(model="llama3.1:8b")

    agent = Agent(
        task=task,
        llm=llm,
        use_vision=False,
        max_failures=3,
    )

    return await agent.run()
