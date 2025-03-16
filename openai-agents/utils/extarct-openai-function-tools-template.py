from fastapi import FastAPI, Request, Response
import json 

app = FastAPI()


# simulate the openai's chat/completions endpoint.
@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    
    json_request = await request.json()

    with open("./openai-agent-function-calling-template.json", "w") as f:
        json.dump(json_request, f)

    return {}
