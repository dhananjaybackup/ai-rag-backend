import chromadb

from rag.embedding_service import EmbeddingService


class VectorStore:

    def __init__(self):

        self.embedding_service = EmbeddingService()

        self.client = chromadb.PersistentClient(path="chroma_db")

        self.collection = self.client.get_or_create_collection(
            name="policies"
        )
    def add_documents(self, chunks, document_name):

        for index, chunk in enumerate(chunks):

            embedding = self.embedding_service.create_embedding(chunk)

            self.collection.add(

                ids=[f"{document_name}_{index}"],

                documents=[chunk],

               embeddings=[embedding],

               metadatas=[
                {
                    "document": document_name
                }
            ]

            )

    def search(self, document_name, question):

        embedding = self.embedding_service.create_embedding(question)

        results = self.collection.query(

            query_embeddings=[embedding],
            where={"document": document_name},
            n_results=3

        )

        return results["documents"][0]
    