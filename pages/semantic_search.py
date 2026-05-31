import streamlit as st

from backend.embeddings import EmbeddingModel
from backend.vector_store import VectorStoreManager

st.title("🔍 Semantic Search")

try:
    embeddings = EmbeddingModel.get_embeddings()

    vector_store = VectorStoreManager.load_store(
        embeddings
    )

except Exception:
    st.error(
        "No indexed paper found. Please upload a PDF first."
    )
    st.stop()

query = st.text_input(
    "Search concepts in the paper"
)

if query:

    with st.spinner("Searching..."):

        docs = vector_store.similarity_search(
            query,
            k=5
        )

    st.subheader("Results")

    for i, doc in enumerate(
        docs,
        start=1
    ):

        st.markdown(f"### Result {i}")

        st.write(doc.page_content)

        if "page" in doc.metadata:
            st.caption(
                f"Page: {doc.metadata['page']}"
            )

        st.divider()