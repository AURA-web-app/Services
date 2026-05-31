from fastapi import FastAPI
from pydantic import BaseModel
from router import route_request

app = FastAPI()
class ChatRequest(BaseModel):
    user_id: str
    message: str
@app.post("/chat")

async def chat(req: ChatRequest):
    result = await route_request(
        req.message,
        req.user_id
    )
    return result