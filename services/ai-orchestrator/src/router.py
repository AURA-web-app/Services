from providers.groq import ask_groq
from providers.openrouter import ask_openrouter
from providers.github import ask_github_model
from providers.fallback import ask_local_model
from logger import log_event

from memory.conversation_memory import (
    daily_request_count
)

from config import settings

async def route_request(
    message,
    user_id
):
    if (
        daily_request_count[user_id]
        >= settings.MAX_DAILY_REQUESTS
    ):
        return (
            "Daily request limit reached."
        )
    providers = [
        ("groq", ask_groq),
        ("openrouter", ask_openrouter),
        ("github", ask_github_model),
        ("local", ask_local_model)
    ]

    for provider_name, provider_func in providers:
        try:
            response = await provider_func(
                message
            )
            daily_request_count[user_id] += 1
            return {
                "provider": provider_name,
                "response": response
            }

        except Exception as e:
            log_event(
                "ai_request",
                {
                    "provider": provider_name,
                    "user_id": user_id,
                    "topic": "physics"
                }
            )
            log_event(
                "provider_failure",
                {
                    "provider": provider_name,
                    "error": str(e)
                }
            )
            continue
    return {
        "provider": "none",
        "response":
        "All AI providers unavailable."
    }