from backend.pdf_loader import PDFLoader
from backend.chunker import TextChunker
from backend.embeddings import EmbeddingModel
from backend.vector_store import VectorStoreManager
from backend.rag_pipeline import RAGPipeline

loader = PDFLoader()

docs = loader.load_pdf("sample.pdf")

chunker = TextChunker()

chunks = chunker.split_documents(docs)

embeddings = EmbeddingModel.get_embeddings()

vector_store = VectorStoreManager.create_vector_store(
    chunks,
    embeddings
)

rag = RAGPipeline(vector_store)

response = rag.ask(
    "What is this paper about?"
)

print(response["answer"])