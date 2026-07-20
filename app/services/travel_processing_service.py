from app.repositories.document_repository import DocumentRepository
from app.services.ocr_service import OCRService
from app.services.parser_service import ParserService
from app.services.validation_service import ValidationService
from app.services.timeline_service import TimelineService


class TravelProcessingService:

    def __init__(self):

        self.repository = DocumentRepository()

        self.ocr_service = OCRService()

        self.parser_service = ParserService()

        self.validation_service = ValidationService()

        self.timeline_service = TimelineService()

    def process_single_document(self, document_id: str):
        self.ocr_service.process_document(document_id)
        self.parser_service.parse_document(document_id)
        self.validation_service.validate_document(document_id)

    def process_travel(
    self,
    user_id: str,
    travel_id: str
):

        documents = self.repository.get_documents_by_user_and_travel(
            user_id,
            travel_id
        )

        for document in documents:

            self.process_single_document(
                document["documentId"]
            )

        timeline = self.timeline_service.build_timeline(
            travel_id
        )

        return {
            "travelId": travel_id,
            "documentsProcessed": len(documents),
            "timeline": timeline
        }