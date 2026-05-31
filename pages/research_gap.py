import streamlit as st

from backend.embeddings import EmbeddingModel
from backend.vector_store import VectorStoreManager
from backend.rag_pipeline import RAGPipeline

st.title("🎯 Research Gap Finder")

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

if st.button("Find Research Gaps"):

    with st.spinner("Analyzing paper..."):

        result = rag.ask(
            """
            Analyze this research paper and identify:

            1. Research limitations
            2. Unanswered questions
            3. Potential future work
            4. Methodological weaknesses
            5. Opportunities for further research

            Present the output under clear headings.
            """, k=12
        )

    st.markdown(result["answer"])