from langchain_core.documents import Document

from backend.embeddings import EmbeddingModel
from backend.vector_store import VectorStoreManager

docs = [
    Document(
        page_content="Artificial Intelligence is transforming healthcare."
    ),
    Document(
        page_content="Machine Learning improves predictive analytics."
    )
]

embeddings = EmbeddingModel.get_embeddings()

vector_store = VectorStoreManager.create_vector_store(
    docs,
    embeddings
)

results = vector_store.similarity_search(
    "AI in healthcare",
    k=1
)

print(results[0].page_content)