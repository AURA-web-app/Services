from uuid import uuid4
from qdrant_client import models
from qdrant_client import (
    client,
    COLLECTION_NAME
)
from embedding_pipeline import (
    generate_embedding
)

def add_document(text, metadata={}):
    embedding = generate_embedding(text)
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            models.PointStruct(
                id=str(uuid4()),
                vector=embedding,
                payload={
                    "text": text,
                    "metadata": metadata
                }
            )
        ]
    )
    return True