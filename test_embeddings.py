# test_embeddings.py

from backend.embeddings import EmbeddingModel

embeddings = EmbeddingModel.get_embeddings()

vector = embeddings.embed_query(
    "Artificial Intelligence"
)

print(len(vector))