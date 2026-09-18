from app.services.rag_retriever import RAGRetriever


question = "Which hotel did EMP1001 stay at in Chicago?"


results = RAGRetriever.retrieve(
    question,
    user_id="EMP1001",
    limit=3
)


print()
print("Question:")
print(question)

print()
print("Retrieved documents:")
print("---------------------")


for index, result in enumerate(results, start=1):

    print()
    print(f"Result {index}")
    print("Score:", result.get("score"))

    print("Metadata:")
    print(result.get("metadata"))

    print("Content:")
    print(result.get("content"))