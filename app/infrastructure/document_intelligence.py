from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential

from app import config


document_intelligence_client = DocumentIntelligenceClient(
    endpoint=config.AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT,
    credential=AzureKeyCredential(
        config.AZURE_DOCUMENT_INTELLIGENCE_KEY
    )
)