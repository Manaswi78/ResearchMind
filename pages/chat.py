import streamlit as st

from backend.embeddings import EmbeddingModel
from backend.vector_store import VectorStoreManager
from backend.rag_pipeline import RAGPipeline

st.title("💬 Chat With Paper")

if "messages" not in st.session_state:
    st.session_state.messages = []

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

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

query = st.chat_input(
    "Ask a question about your paper"
)

if query:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message("user"):
        st.write(query)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            result = rag.ask(query)

            st.write(result["answer"])

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": result["answer"]
        }
    )