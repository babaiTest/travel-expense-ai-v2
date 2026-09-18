from app.services.rag_retriever import RAGRetriever
from app.infrastructure.azure_openai import llm


class RAGService:

    @staticmethod
    def ask(question: str):

        # Step 1: Retrieve relevant documents
        results = RAGRetriever.retrieve(
            question,
            limit=3
        )

        # Step 2: Build context from retrieved documents
        context_parts = []

        for result in results:

            content = result.get("content", "")

            context_parts.append(content)

        context = "\n\n---\n\n".join(context_parts)

        # Step 3: Build the prompt
        prompt = f"""
You are an AI assistant for a Travel Expense system.

Answer the user's question using ONLY the information provided
in the context below.

If the answer cannot be found in the context, say:
"I could not find the answer in the available travel records."

Do not make up information.

Context:
{context}

User Question:
{question}

Answer:
"""

        # Step 4: Ask the LLM
        response = llm.invoke(prompt)

        return {
            "question": question,
            "answer": response.content,
            "sources": [
                result.get("metadata")
                for result in results
            ]
        }