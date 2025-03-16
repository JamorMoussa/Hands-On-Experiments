# Hands-On Experiments

## [01. OpenAI Agents SDK + Ollama](./openai-agents)

The **OpenAI Agents SDK** is a library developed by OpenAI that allows you to build agentic applications, where LLMs can utilize tools to answer user queries. For more information, refer to the corresponding [README file](./openai-agents/).

## Scripts  

- [Weather Agent](./openai-agents/scripts/weather-openai-agent-ollama.py):  
  A weather agent equipped with the `get_weather` tool. It retrieves weather information when a user asks for the weather of a city. The output is formatted according to the `WeatherModel`.  

- [Streamed Agent](./openai-agents/scripts/openai-agent-stream-with-ollama.py):  
  Generates responses token by token for real-time interaction.  

## Notebooks  

- [Function Calling with Qwen2.5-1B Instruct](./openai-agents/openai-agents/notebooks/function_calling_with_qween2_5_1b_instruct.ipynb):  Demonstrates how to use function calling with the Qwen2.5-1B Instruct model using Hugging Face API, allowing the LLM to invoke external tools and APIs for structured outputs.  

