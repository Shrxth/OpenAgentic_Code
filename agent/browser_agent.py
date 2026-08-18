import os
import asyncio
from browser_use import Agent, ChatOpenAI


async def run_browser_agent(task: str):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not configured."
        )

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=api_key,
    )

    agent = Agent(
        task=task,
        llm=llm,
    )

    return await agent.run()
