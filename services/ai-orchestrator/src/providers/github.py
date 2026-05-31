import httpx
from config import settings

API_URL = "https://models.inference.ai.azure.com/chat/completions"

async def ask_github_model(message):
    headers = {
        "Authorization":
        f"Bearer {settings.GITHUB_MODELS_TOKEN}"
    }
    payload = {
        "model": settings.GITHUB_MODEL,
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