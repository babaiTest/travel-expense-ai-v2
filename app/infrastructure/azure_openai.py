from langchain_openai import AzureChatOpenAI

from app import config


llm = AzureChatOpenAI(
    azure_endpoint=config.AZURE_OPENAI_ENDPOINT,
    api_key=config.AZURE_OPENAI_KEY,
    azure_deployment=config.AZURE_OPENAI_DEPLOYMENT,
    api_version=config.AZURE_OPENAI_API_VERSION,
    temperature=0
)