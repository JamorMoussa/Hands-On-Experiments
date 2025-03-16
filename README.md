# Hands-On-Experiments 


## [01. Openai Agents SDK + Ollama](./openai-agents)

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

