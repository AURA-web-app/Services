from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="Qwen/Qwen2-0.5B-Instruct"
)

async def ask_local_model(message):
    prompt = f"""
    Student Question:
    {message}
    Educational Answer:
    """
    output = generator(
        prompt,
        max_new_tokens=60
    )
    return output[0]["generated_text"]