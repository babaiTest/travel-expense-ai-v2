from fastapi import UploadFile
from typing import List
import uuid
from app.models.schemas import UploadedDocument
from app.infrastructure.azure_storage import container_client
#from app.repositories.document_repository import save_document
from app.repositories.document_repository import DocumentRepository 
from app.constants import DOCUMENT_STATUS_UPLOADED


repository = DocumentRepository()
async def upload_documents(
    user_id: str,
    travel_id: str,
    files: List[UploadFile]
) -> List[UploadedDocument]:
    """
    Upload documents to Azure Blob Storage.

    Parameters:
        user_id (str): Employee/User ID
        travel_id (str): Travel ID
        files (List[UploadFile]): Files uploaded from FastAPI

    Returns:
        List[dict]: Metadata of uploaded documents
    """
    print("Inside upload_documents()")
    uploaded_documents = []

    for file in files:

        # --------------------------------------------------
        # Generate a unique document id
        # --------------------------------------------------
        document_id = str(uuid.uuid4())

        # --------------------------------------------------
        # Create blob path
        # Example:
        # EMP101/TRV1001/7d6b0f1e-flight.pdf
        # --------------------------------------------------
        print(f"Uploading: {file.filename}")
        blob_name = (
            f"{user_id}/"
            f"{travel_id}/"
            f"{document_id}-{file.filename}"
        )

        # --------------------------------------------------
        # Create Blob Client
        # --------------------------------------------------
        blob_client = container_client.get_blob_client(blob_name)

        # --------------------------------------------------
        # Ensure stream starts from beginning
        # --------------------------------------------------
        await file.seek(0)

        # --------------------------------------------------
        # Upload file to Azure Blob Storage
        # --------------------------------------------------
        blob_client.upload_blob(
            file.file,
            overwrite=False
        )

        # --------------------------------------------------
        # Save document metadata to MongoDB
        # --------------------------------------------------
        document_metadata = {
            "documentId": document_id,
            "userId": user_id,
            "travelId": travel_id,
            "fileName": file.filename,
            "blobName": blob_name,
            "blobUrl": blob_client.url,
            "contentType": file.content_type,
            "status": DOCUMENT_STATUS_UPLOADED
        }
        repository.save_document(document_metadata)

        # --------------------------------------------------
        # Store metadata for downstream services
        # --------------------------------------------------
        uploaded_documents.append(
            UploadedDocument(
            document_id=document_id,
            file_name=file.filename,
            blob_name=blob_name,
            blob_url=blob_client.url,
            content_type=file.content_type
            )
        )

    return uploaded_documents

def download_document(blob_name: str):

    blob_client = container_client.get_blob_client(blob_name)

    download_stream = blob_client.download_blob()

    file_bytes = download_stream.readall()

    return file_bytes