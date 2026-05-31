import httpx
from config import settings

API_URL = "https://api.groq.com/openai/v1/chat/completions"
async def ask_groq(message):
    headers = {
        "Authorization":
        f"Bearer {settings.GROQ_API_KEY}"
    }
    payload = {
        "model": settings.GROQ_MODEL,
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ]
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=20
        )

    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]