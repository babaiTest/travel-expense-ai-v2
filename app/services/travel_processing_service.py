from app.repositories.document_repository import DocumentRepository

from app.services.ocr_service import OCRService
from app.services.parser_service import ParserService
from app.services.validation_service import ValidationService
from app.services.timeline_service import TimelineService

from app.constants import (
    DOCUMENT_STATUS_UPLOADED,
    DOCUMENT_STATUS_OCR_COMPLETED,
    DOCUMENT_STATUS_PARSED,
    DOCUMENT_STATUS_VALIDATED,
    DOCUMENT_STATUS_FRAUD_ANALYZED
)


class TravelProcessingService:

    def __init__(self):

        self.repository = DocumentRepository()

        self.ocr_service = OCRService()
        self.parser_service = ParserService()
        self.validation_service = ValidationService()
        self.timeline_service = TimelineService()

    def process_single_document(self, document):

        document_id = document["documentId"]
        status = document.get("status", DOCUMENT_STATUS_UPLOADED)

        print(f"\nProcessing document : {document_id}")
        print(f"Current Status      : {status}")

        # -----------------------------
        # OCR
        # -----------------------------
        if status == DOCUMENT_STATUS_UPLOADED:

            print("Running OCR...")

            self.ocr_service.process_document(document_id)

            status = DOCUMENT_STATUS_OCR_COMPLETED

        # -----------------------------
        # Parser
        # -----------------------------
        if status == DOCUMENT_STATUS_OCR_COMPLETED:

            print("Running Parser...")

            self.parser_service.parse_document(document_id)

            status = DOCUMENT_STATUS_PARSED

        # -----------------------------
        # Validation
        # -----------------------------
        if status == DOCUMENT_STATUS_PARSED:

            print("Running Validation...")

            self.validation_service.validate_document(document_id)

            status = DOCUMENT_STATUS_VALIDATED

        if status == DOCUMENT_STATUS_VALIDATED:

            print("Document processing completed.")

        elif status == DOCUMENT_STATUS_FRAUD_ANALYZED:

            print("Document already fully processed.")

        else:

            print(f"Document stopped at status : {status}")

    def process_travel(self, user_id: str, travel_id: str):

        print(f"\nProcessing Travel : {travel_id}")

        documents = self.repository.get_documents_by_user_and_travel(
            user_id,
            travel_id
        )

        if not documents:

            return {
                "travelId": travel_id,
                "documentsProcessed": 0,
                "documentsSucceeded": 0,
                "documentsFailed": 0,
                "timeline": []
            }

        succeeded = 0
        failed = 0

        for document in documents:

            try:

                self.process_single_document(document)

                succeeded += 1

            except Exception as ex:

                failed += 1

                print(
                    f"Error processing document "
                    f"{document['documentId']} : {str(ex)}"
                )

        timeline = self.timeline_service.build_timeline(travel_id)

        return {

            "travelId": travel_id,

            "documentsProcessed": len(documents),

            "documentsSucceeded": succeeded,

            "documentsFailed": failed,

            "timeline": timeline
        }