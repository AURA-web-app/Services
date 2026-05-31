from fastapi import FastAPI
from metrics import generate_metrics
from analytics import top_requested_topics
from provider_monitor import (get_provider_status)

app = FastAPI()
@app.get("/metrics")

async def metrics():
    return generate_metrics()

@app.get("/topics")

async def topics():
    return {
        "top_topics":
        top_requested_topics()
    }

@app.get("/providers")

async def providers():
    return get_provider_status()