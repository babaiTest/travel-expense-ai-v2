from pydantic import BaseModel
from uuid import UUID

class UploadedDocument(BaseModel):

    document_id: UUID
    file_name: str
    blob_name: str
    blob_url: str
    content_type: str