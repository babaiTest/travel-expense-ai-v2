from pydantic import BaseModel

from app.infrastructure.azure_openai import llm


def invoke_structured(prompt: str, schema: type[BaseModel]) -> BaseModel:
    structured_llm = llm.with_structured_output(schema)
    return structured_llm.invoke(prompt)
