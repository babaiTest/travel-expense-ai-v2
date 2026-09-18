from app.infrastructure.mongodb import rag_document_collection


class RAGRepository:

    @staticmethod
    def upsert_rag_document(rag_document: dict):

        document_id = rag_document["metadata"]["documentId"]

        result = rag_document_collection.update_one(
            {
                "metadata.documentId": document_id
            },
            {
                "$set": rag_document
            },
            upsert=True
        )

        return result