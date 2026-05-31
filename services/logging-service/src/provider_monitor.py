provider_status = {
    "groq": "healthy",
    "openrouter": "healthy",
    "github": "healthy",
    "local": "healthy"
}

def update_provider_status(
    provider,
    status
):
    provider_status[provider] = status
    
def get_provider_status():
    return provider_status