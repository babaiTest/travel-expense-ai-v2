from app.builders.rag_document_builder import RAGDocumentBuilder
from app.infrastructure.azure_openai import embeddings
from app.repositories.rag_repository import RAGRepository
from app.infrastructure.mongodb import document_collection


# Get one existing document from MongoDB
document = document_collection.find_one({
    "travelId": "TRV1002"
})

if not document:
    print("Document not found.")
    exit()


# Convert MongoDB document into our RAG format
rag_document = RAGDocumentBuilder.build_from_document(document)


# Generate embedding from the content
vector = embeddings.embed_query(
    rag_document["content"]
)


# Add embedding to RAG document
rag_document["embedding"] = vector


# Store in MongoDB
inserted_id = RAGRepository.insert_rag_document(
    rag_document
)


print("RAG document stored successfully.")
print("MongoDB ID:", inserted_id)
print("Vector dimension:", len(vector))