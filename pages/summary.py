import streamlit as st

from backend.embeddings import EmbeddingModel
from backend.vector_store import VectorStoreManager
from backend.rag_pipeline import RAGPipeline

st.title("📝 Research Paper Summary")

try:
    embeddings = EmbeddingModel.get_embeddings()

    vector_store = VectorStoreManager.load_store(
        embeddings
    )

    rag = RAGPipeline(vector_store)

except Exception:
    st.error(
        "No indexed paper found. Please upload a PDF first."
    )
    st.stop()

if st.button("Generate Summary"):

    with st.spinner("Generating summary..."):

        result = rag.ask(
            """
            Provide a structured summary of the paper:

            1. Overview
            2. Research Problem
            3. Methodology
            4. Key Findings
            5. Limitations
            6. Future Work

            Use clear headings.
            """,k=10
        )

    st.markdown(result["answer"])