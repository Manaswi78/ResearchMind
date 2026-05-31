import streamlit as st
import os
import time

st.title("📄 Upload Research Paper")

uploaded_file = st.file_uploader(
    "Choose a PDF",
    type=["pdf"]
)

if uploaded_file:

    # Import only when needed
    from backend.pdf_loader import PDFLoader
    from backend.chunker import TextChunker
    from backend.embeddings import EmbeddingModel
    from backend.vector_store import VectorStoreManager

    os.makedirs("uploads", exist_ok=True)

    pdf_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF uploaded successfully")

    start_time = time.time()

    with st.spinner("Processing paper and building vector index..."):

        loader = PDFLoader()
        docs = loader.load_pdf(pdf_path)

        chunker = TextChunker()
        chunks = chunker.split_documents(docs)

        embeddings = EmbeddingModel.get_embeddings()

        vector_store = VectorStoreManager.create_vector_store(
            chunks,
            embeddings
        )

        VectorStoreManager.save_store(vector_store)

    end_time = time.time()

    st.success("Paper indexed successfully ✅")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Pages Loaded", len(docs))

    with col2:
        st.metric("Chunks Created", len(chunks))

    with col3:
        st.metric(
            "Processing Time",
            f"{end_time - start_time:.2f}s"
        )

    st.info(
        "Your paper has been indexed and is ready for search/chat."
    )