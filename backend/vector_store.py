from langchain_community.vectorstores import FAISS


class VectorStoreManager:

    @staticmethod
    def create_vector_store(documents, embeddings):
        return FAISS.from_documents(
            documents,
            embeddings
        )

    @staticmethod
    def save_store(
        vector_store,
        path="data/faiss_index"
    ):
        vector_store.save_local(path)

    @staticmethod
    def load_store(
        embeddings,
        path="data/faiss_index"
    ):
        return FAISS.load_local(
            path,
            embeddings,
            allow_dangerous_deserialization=True
        )