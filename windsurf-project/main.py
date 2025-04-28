import asyncio
from agents.root_agent import create_root_agent

async def main():
    agent, _ = await create_root_agent()
    # You can pass initial state, e.g., topic and keywords
    state = {"topic": "AI and Automation", "keywords": ["AI", "automation", "productivity"]}
    result = await agent.run(state)
    print("Pipeline Result:\n", result)

if __name__ == "__main__":
    asyncio.run(main())

