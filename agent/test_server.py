import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

PROJECT_PATH = "D:/SideProject/spec-wingman"


async def main():
    params = StdioServerParameters(
        command=".venv/Scripts/python.exe",
        args=["server.py"],
    )
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 1. List tools
            tools = await session.list_tools()
            print("=== Registered Tools ===")
            for t in tools.tools:
                print(f"  · {t.name}")

            # 2. Call swm_status
            print("\n=== swm_status ===")
            result = await session.call_tool("swm_status", {"project_path": PROJECT_PATH})
            print(result.content[0].text)

            # 3. Call swm_discover_context
            print("\n=== swm_discover_context (first 300 chars) ===")
            result = await session.call_tool("swm_discover_context", {"project_path": PROJECT_PATH})
            print(result.content[0].text[:300] + "...")


asyncio.run(main())
