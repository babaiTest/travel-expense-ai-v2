from app.builders.rag_document_builder import RAGDocumentBuilder
from app.infrastructure.azure_openai import embeddings
from app.infrastructure.mongodb import document_collection
from app.repositories.rag_repository import RAGRepository


# Get all source documents
documents = document_collection.find({})

total = 0

for document in documents:

    total += 1

    print()
    print("Processing document:", document.get("documentId"))

    # Convert MongoDB document into RAG document
    rag_document = RAGDocumentBuilder.build_from_document(document)

    # Generate embedding from the RAG content
    vector = embeddings.embed_query(
        rag_document["content"]
    )

    print("Embedding dimension:", len(vector))

    # Add embedding to RAG document
    rag_document["embedding"] = vector

    # Store/update in MongoDB
    result = RAGRepository.upsert_rag_document(
        rag_document
    )

    if result.upserted_id:
        print("RAG document inserted.")
    else:
        print("RAG document updated.")


print()
print("RAG indexing completed.")
print("Total source documents processed:", total)