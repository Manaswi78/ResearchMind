from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextChunker:
    """
    Splits documents into smaller chunks for RAG.
    """

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", " ", ""]
        )

    def split_documents(self, documents):
        """
        Split LangChain documents into chunks.
        """
        return self.splitter.split_documents(documents)