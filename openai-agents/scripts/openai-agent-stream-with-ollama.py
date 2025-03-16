import asyncio
from openai.types.responses import ResponseTextDeltaEvent
from agents import (
    Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI)
import os 

os.environ["OPENAI_API_KEY"] = "ollama"

model = OpenAIChatCompletionsModel(
    model= "qwen2.5:1.5b", # "llama3.2:1b",
    openai_client= AsyncOpenAI(base_url="http://localhost:11434/v1")
)

async def main():
    agent = Agent(
        name="Joker",
        model=model,
        instructions="You are a helpful assistant.",
    )

    result = Runner.run_streamed(agent, input="Please tell me 5 jokes.")
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)


if __name__ == "__main__":
    asyncio.run(main())