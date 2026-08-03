from app.repositories.document_repository import DocumentRepository
from app.services.storage_service import download_document
from app.infrastructure.document_intelligence import (
    document_intelligence_client
)
import io
from PIL import Image


class OCRService:

    MAX_IMAGE_SIZE_MB = 4

    def __init__(self):
        self.document_repository = DocumentRepository()

    def process_document(self, document_id: str):

        document = self.document_repository.get_document_by_id(document_id)

        if document is None:
            raise Exception("Document not found")

        blob_name = document["blobName"]

        file_bytes = download_document(blob_name)
        image_bytes: bytes | None = file_bytes
        content_type = document["contentType"]

        if content_type.startswith("image/"):
            if self._is_image_too_large(file_bytes):
                print("Large image detected.")

                image_bytes = self._compress_image(
                    file_bytes
                )
                print(
                    f"Compressed Size = {len(image_bytes)/(1024*1024):.2f} MB"
                )
        elif content_type == "application/pdf":
            image_bytes = file_bytes
        poller = document_intelligence_client.begin_analyze_document(
        "prebuilt-read",
        body=image_bytes
    )

        result = poller.result()
        ocr_text = result.content
        self.document_repository.update_document_ocr(
            document_id,
            ocr_text
    )
        print("Document analysis result:", ocr_text)
        return ocr_text   # Return the extracted text content from the document

    def _is_image_too_large(
        self,
        image_bytes: bytes
) -> bool:

        size_mb = len(image_bytes) / (1024 * 1024)
        print(f"Image Size = {size_mb:.2f} MB")
        return size_mb > self.MAX_IMAGE_SIZE_MB

    def _compress_image(
    self,
    image_bytes: bytes
) -> bytes:

        image = Image.open(
            io.BytesIO(image_bytes)
        )

        # Convert RGBA / PNG to RGB
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")

        # Resize if width is very large
        max_width = 1600

        if image.width > max_width:

            ratio = max_width / image.width

            new_height = int(
                image.height * ratio
            )

            image = image.resize(
                (max_width, new_height)
            )

        output = io.BytesIO()

        image.save(
            output,
            format="JPEG",
            quality=85,
            optimize=True
        )

        return output.getvalue()