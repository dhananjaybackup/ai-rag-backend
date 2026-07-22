from rag.pdf_loader import PdfLoader
from rag.vector_store import VectorStore


class RagService:

    def __init__(self):

        self.loader = PdfLoader()

        self.vector_store = VectorStore()

    def chunk_text(self, text, chunk_size=500):

        chunks = []

        for i in range(0, len(text), chunk_size):

            chunks.append(text[i:i + chunk_size])

        return chunks
    
    def load_policy(self, pdf_path, document_name):

        text = self.loader.load_pdf(pdf_path)

        chunks = self.chunk_text(text)

        self.vector_store.add_documents(chunks, document_name)

        print("Policy Loaded")
        return chunks

    def search(self, document_name, question):

        documents = self.vector_store.search(document_name, question)

        return "\n".join(documents)