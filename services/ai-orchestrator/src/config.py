import os
from dotenv import load_dotenv

load_dotenv()
class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    OPENROUTER_API_KEY = os.getenv(
        "OPENROUTER_API_KEY"
    )
    GITHUB_MODELS_TOKEN = os.getenv(
        "GITHUB_MODELS_TOKEN"
    )
    MAX_DAILY_REQUESTS = 5

settings = Settings()