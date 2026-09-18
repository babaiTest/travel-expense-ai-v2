from app.infrastructure.mongodb import rag_document_collection
from app.infrastructure.azure_openai import embeddings


class RAGRetriever:

    @staticmethod
    def retrieve(
        question: str,
        user_id: str = None,
        limit: int = 3
    ):

        # Convert the question into an embedding
        query_vector = embeddings.embed_query(question)

        vector_search = {
            "$vectorSearch": {
                "index": "rag_vector_index",
                "path": "embedding",
                "queryVector": query_vector,
                "numCandidates": 10,
                "limit": limit
            }
        }

        # Apply user-level filtering when user_id is provided
        if user_id:
            vector_search["$vectorSearch"]["filter"] = {
                "metadata.userId": {
                    "$eq": user_id
                }
            }

        pipeline = [
            vector_search,
            {
                "$project": {
                    "_id": 0,
                    "content": 1,
                    "metadata": 1,
                    "score": {
                        "$meta": "vectorSearchScore"
                    }
                }
            }
        ]

        results = rag_document_collection.aggregate(pipeline)

        return list(results)