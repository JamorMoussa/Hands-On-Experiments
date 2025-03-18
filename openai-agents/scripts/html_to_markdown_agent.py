from agents import (
    Agent, OpenAIChatCompletionsModel, AsyncOpenAI, function_tool, Runner,
)
from openai.types.responses import ResponseTextDeltaEvent
import os
import requests
import asyncio
from markitdown import MarkItDown

os.environ["OPENAI_API_KEY"] = "ollama"

model = OpenAIChatCompletionsModel(
    model= "llama3.2:1b", # "llama3.2:1b",
    openai_client= AsyncOpenAI(base_url="http://localhost:11434/v1")
)

@function_tool
def extract_content_from_html(url: str) -> str:
    """
    This tool is used to extract webpage content as markdown.

    args:
        url: str - represent the url of webpage.

    returns:
        return the markdown text.   
    """    
    response = requests.get(url=url)

    md = MarkItDown()
    return md.convert(source=response).text_content

async def main():

    html_agent = Agent(
        name="Assistant",
        model=model,
        instructions= " ".join([
            "You a helpful Agent Assistant",
            "You are a markdown extractor, use only tools you've provided"
        ]),
        tools= [extract_content_from_html]
    )

    result = Runner.run_streamed(
        html_agent, input="extract the content of: https://www.geeksforgeeks.org/extracting-text-from-html-file-using-python/"
    )
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)


if __name__ == "__main__":
    asyncio.run(main())