# AI Agents - OpenAI SDK + Ollama 

**OpenAI Agents SDK** is library made by OpenAI, that enables use to build agentic application, where LLMs can leverage tools, to answer the user's query.

The Agents SDK is designed around these core primitives:

| **Component**   | **Purpose**                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| **Agent**       | An LLM configured with instructions, tools, handoffs, guardrails, etc.      |
| **Tool**        | Functions the agent can call for external help (e.g., APIs, calculations, file access). |
| **Context**     | A (mutable) object you create and pass along, storing state or shared resources. |
| **Output Types**| Allows you to specify structured final outputs (or default to free-form text). |
| **Handoffs**    | Mechanism for delegating or switching the conversation to a different agent. |
| **Streaming**   | Emits partial/delta output events as the agent thinks or calls tools (useful for real-time UIs). |
| **Tracing**     | Automatically captures a detailed trace of each “agentic run” for debugging, analytics, or record-keeping. |
| **Guardrails**  | Validate inputs or outputs, check policy, or halt execution if something is off-limits. |


## Scripts  

- [Weather Agent](./scripts/weather-openai-agent-ollama.py):  
  A weather agent equipped with the `get_weather` tool. It retrieves weather information when a user asks for the weather of a city. The output is formatted according to the `WeatherModel`.  

- [Streamed Agent](./scripts/openai-agent-stream-with-ollama.py):  
  Generates responses token by token for real-time interaction.  

## Notebooks  

- [Function Calling with Qwen2.5-1B Instruct](./notebooks/function_calling_with_qween2_5_1b_instruct.ipynb):  Demonstrates how to use function calling with the Qwen2.5-1B Instruct model using Hugging Face API, allowing the LLM to invoke external tools and APIs for structured outputs.  


