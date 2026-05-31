from qdrant_client import (
    client,
    COLLECTION_NAME
)
from embedding_pipeline import (
    generate_embedding
)

def search_documents(query, limit=3):
    embedding = generate_embedding(query)
    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=embedding,
        limit=limit
    )
    formatted = []
    for result in results:
        formatted.append({
            "score": result.score,
            "text": result.payload["text"]
        })
    return formatted