import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# ==============================
# Azure Blob Storage
# ==============================
AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
AZURE_STORAGE_CONTAINER = os.getenv("AZURE_STORAGE_CONTAINER")

# ==============================
# MongoDB collection for documents
# ==============================
MONGODB_CONNECTION_STRING = os.getenv("MONGODB_CONNECTION_STRING")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE")
MONGODB_DOCUMENT_COLLECTION = os.getenv("MONGODB_DOCUMENT_COLLECTION")

# ==============================
# MongoDB collection for documents
# ==============================
MONGODB_TRAVEL_COLLECTION = os.getenv("MONGODB_TRAVEL_COLLECTION")

# ==============================
# Azure Document Intelligence
# ==============================
AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT = os.getenv("AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT")
AZURE_DOCUMENT_INTELLIGENCE_KEY = os.getenv("AZURE_DOCUMENT_INTELLIGENCE_KEY")

# ==============================
# Azure OpenAI
# ==============================
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
