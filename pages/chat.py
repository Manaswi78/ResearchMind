import streamlit as st

from backend.embeddings import EmbeddingModel
from backend.vector_store import VectorStoreManager
from backend.rag_pipeline import RAGPipeline

st.title("💬 Chat With Paper")

try:
    embeddings = EmbeddingModel.get_embeddings()

    vector_store = VectorStoreManager.load_store(
        embeddings
    )

    rag = RAGPipeline(vector_store)

except Exception as e:
    st.error(
        "No indexed paper found. Please upload a PDF first."
    )
    st.stop()

query = st.text_input(
    "Ask a question about your paper"
)

if query:

    with st.spinner("Thinking..."):

        result = rag.ask(query)

    st.subheader("Answer")

    st.write(result["answer"])

    with st.expander("Sources Used"):

        for i, doc in enumerate(
            result["sources"],
            start=1
        ):
            st.write(f"Source {i}")
            st.write(doc.page_content[:500])
            st.divider()