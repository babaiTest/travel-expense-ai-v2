from app.repositories.document_repository import DocumentRepository


class ParserService:

    def __init__(self):

        self.document_repository = DocumentRepository()

    def parse_document(self, document_id: str):
        document = self.document_repository.get_document_by_id(document_id)

        if document is None:
            raise Exception("Document not found")

        ocr_text = document.get("ocrText")

        if not ocr_text:
            raise Exception("OCR not completed.")
        return ocr_text