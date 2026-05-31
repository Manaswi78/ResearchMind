from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


class RAGPipeline:
    def __init__(self, vector_store):

        self.vector_store = vector_store

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.2
        )

    def ask(self, query: str,k: int =4):

        docs = self.vector_store.similarity_search(
            query,
            k=k
        )

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        prompt = f"""
You are a research assistant.

Answer ONLY using the provided context.

Context:
{context}

Question:
{query}

Answer:
"""

        response = self.llm.invoke(prompt)

        return {
            "answer": response.content,
            "sources": docs
        }