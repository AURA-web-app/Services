from qdrant_client import QdrantClient
from qdrant_client import (
    VectorParams,
    Distance
)

client = QdrantClient(":memory:")
COLLECTION_NAME = "juststudy_knowledge"

def setup_collection():
    collections = client.get_collections()
    existing = [
        c.name for c in collections.collections
    ]
    if COLLECTION_NAME not in existing:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )