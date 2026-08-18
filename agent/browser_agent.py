import os
import asyncio
from browser_use import Agent
from langchain_openai import ChatOpenAI


async def run_browser_agent(task: str):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not configured."
        )

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        api_key=api_key,
    )

    agent = Agent(
        task=task,
        llm=llm,
    )

    return await agent.run()


if __name__ == "__main__":
    asyncio.run(
        run_browser_agent(
            "Open https://example.com and report the page title."
        )
    )
