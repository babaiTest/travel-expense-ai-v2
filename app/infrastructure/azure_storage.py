from azure.storage.blob import BlobServiceClient

from app.config import (
    AZURE_STORAGE_CONNECTION_STRING,
    AZURE_STORAGE_CONTAINER
)

blob_service_client = BlobServiceClient.from_connection_string(
    AZURE_STORAGE_CONNECTION_STRING
)
container_client = blob_service_client.get_container_client(
    AZURE_STORAGE_CONTAINER
)