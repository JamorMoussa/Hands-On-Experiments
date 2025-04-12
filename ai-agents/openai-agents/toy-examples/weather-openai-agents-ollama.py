from agents import (
    Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, function_tool
)

import os
from pydantic import BaseModel, Field

os.environ["OPENAI_API_KEY"] = "ollama"

model = OpenAIChatCompletionsModel(
    model= "qwen2.5:1.5b", # "llama3.2:1b",
    openai_client= AsyncOpenAI(base_url="http://localhost:11436/v1")
)

@function_tool
def get_weather(city: str) -> str:
    """Gives the weather of given city as arguments."""
    return f"The weather in {city} is sunny"

#d structured output
class WeatherModel(BaseModel):
    city: str = Field(
        default= "Rabat", description="this field represents the city name.",
    )
    weather: str = Field(
        default= "Sunny", description="this field represents, the weather sunny ..."
    )

agent = Agent(
    name= "Assistant", model=model,
    instructions="You are helpful assistant, you provide helping tools.",
    tools= [get_weather],
    output_type=WeatherModel
)

response = Runner.run_sync(
    starting_agent=agent, input="What's the weather today in Casablanca?"
)
