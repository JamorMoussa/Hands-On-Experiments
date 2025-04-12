from agents.mcp import (
    MCPServer, MCPServerStdio
)

from agents import (
    Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
)

from pathlib import Path
import asyncio

from dotenv import load_dotenv
from pprint import pprint

set_tracing_disabled(disabled=True)
load_dotenv()

async def run(server: MCPServer):

    model = OpenAIChatCompletionsModel(
        # Using Github Models:

        # model="gpt-4o-mini",
        # openai_client= AsyncOpenAI(base_url="https://models.inference.ai.azure.com", api_key=os.environ["OPENAI_API_KEY"]),

        # model="grok-2-latest",
        # openai_client= AsyncOpenAI(base_url="https://api.x.ai/v1", api_key=os.environ["GROK_API"]),

        # Using Ollama:
            model="llama3.2:1b",
            openai_client= AsyncOpenAI(base_url="http://127.0.0.1:8001/v1", api_key="ollama")
    )


    agent = Agent(
        name="Assistant",
        model=model,
        instructions="Use the tools to read the filesystem and answer questions based on those files.",
        mcp_servers=[server],
    )

    message = "give list of available files. give tools that you used to do so"
    print(f"Running: {message}")
    result = await Runner.run(starting_agent=agent, input=message)
    print(result.final_output)


async def main():

    samples_dir = Path("./sample_file")

    async with MCPServerStdio(
        params={
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-filesystem", str(samples_dir.absolute())],
        }
    ) as server:
        await run(server)
        # tools = await server.list_tools()
        # print(tools)

        # res = await server.call_tool(
        #     "list_directory", {"path": str(samples_dir.absolute())}
        # )



        # for c in res.content:
        #     print(c.text)


if __name__ == "__main__":
    asyncio.run(main())
