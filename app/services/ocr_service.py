from app.repositories.document_repository import DocumentRepository
from app.services.storage_service import download_document
from app.infrastructure.document_intelligence import (
    document_intelligence_client
)


class OCRService:

    def __init__(self):
        self.document_repository = DocumentRepository()

    def process_document(self, document_id: str):

        document = self.document_repository.get_document_by_id(document_id)

        if document is None:
            raise Exception("Document not found")

        blob_name = document["blobName"]

        file_bytes = download_document(blob_name)

        poller = document_intelligence_client.begin_analyze_document(
        "prebuilt-read",
        body=file_bytes
    )

        result = poller.result()
        ocr_text = result.content
        self.document_repository.update_document_ocr(
            document_id,
            ocr_text
    )
        print("Document analysis result:", ocr_text)
        return ocr_text   # Return the extracted text content from the document