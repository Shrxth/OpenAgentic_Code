import asyncio
from browser_use import Agent
from langchain_openai import ChatOpenAI


async def run_browser_agent(task: str):
    model = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
    )

    agent = Agent(
        task=task,
        llm=model,
    )

    return await agent.run()


if __name__ == "__main__":
    asyncio.run(
        run_browser_agent(
            "Open https://example.com and tell me the page title."
        )
    )
