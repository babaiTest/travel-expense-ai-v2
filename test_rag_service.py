from app.services.rag_service import RAGService


question = "Which hotel did EMP1001 stay at in Chicago?"


result = RAGService.ask(question)


print()
print("Question:")
print(result["question"])

print()
print("Answer:")
print(result["answer"])

print()
print("Sources:")
for source in result["sources"]:
    print(source)