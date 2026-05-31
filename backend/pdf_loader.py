from langchain_community.document_loaders import PyPDFLoader


class PDFLoader:
    """
    Load PDF documents.
    """

    def load_pdf(self, pdf_path: str):
        loader = PyPDFLoader(pdf_path)
        return loader.load()