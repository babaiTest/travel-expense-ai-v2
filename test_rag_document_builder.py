from app.infrastructure.mongodb import database
from app.builders.rag_document_builder import RAGDocumentBuilder


documents_collection = database["documents"]


documents = list(
    documents_collection.find({})
)


rag_documents = (
    RAGDocumentBuilder.build_from_documents(
        documents
    )
)


print()
print("======================================")
print("RAG DOCUMENTS")
print("======================================")


for index, document in enumerate(
    rag_documents,
    start=1
):

    print()
    print(f"========== Document {index} ==========")

    print()
    print("CONTENT:")
    print(document["content"])

    print()
    print("METADATA:")
    print(document["metadata"])