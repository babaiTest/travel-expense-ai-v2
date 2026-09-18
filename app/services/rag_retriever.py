from app.infrastructure.mongodb import rag_document_collection
from app.infrastructure.azure_openai import embeddings


class RAGRetriever:

    @staticmethod
    def retrieve(
        question: str,
        limit: int = 3
    ):

        # Step 1: Convert the user's question into an embedding
        query_vector = embeddings.embed_query(question)

        # Step 2: Perform vector search in MongoDB
        pipeline = [
            {
                "$vectorSearch": {
                    "index": "rag_vector_index",
                    "path": "embedding",
                    "queryVector": query_vector,
                    "numCandidates": 10,
                    "limit": limit
                }
            },
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

        # Step 3: Execute the aggregation pipeline
        results = rag_document_collection.aggregate(pipeline)

        return list(results)