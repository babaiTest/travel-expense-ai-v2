from app.repositories.document_repository import DocumentRepository

from app.services.ocr_service import OCRService
from app.services.parser_service import ParserService
from app.services.validation_service import ValidationService
from app.services.timeline_service import TimelineService
from app.services.fraud_service import FraudService

from app.constants.document_status import (
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
        self.fraud_service = FraudService()

    # ---------------------------------------------------------
    # Process a single document
    # ---------------------------------------------------------

    def process_single_document(self, document_id: str):

        document = self.repository.get_document_by_id(document_id)

        if not document:
            raise Exception(f"Document {document_id} not found.")

        status = document.get("status", DOCUMENT_STATUS_UPLOADED)

        print(f"\nProcessing Document : {document_id}")
        print(f"Current Status      : {status}")

        # -----------------------------------------------------
        # OCR
        # -----------------------------------------------------

        if status == DOCUMENT_STATUS_UPLOADED:

            print("Running OCR...")

            self.ocr_service.process_document(document_id)

            document = self.repository.get_document_by_id(document_id)
            status = document.get("status")

        # -----------------------------------------------------
        # Parser
        # -----------------------------------------------------

        if status == DOCUMENT_STATUS_OCR_COMPLETED:

            print("Running Parser...")

            self.parser_service.parse_document(document_id)

            document = self.repository.get_document_by_id(document_id)
            status = document.get("status")

        # -----------------------------------------------------
        # Validation
        # -----------------------------------------------------

        if status == DOCUMENT_STATUS_PARSED:

            print("Running Validation...")

            self.validation_service.validate_document(document_id)

            document = self.repository.get_document_by_id(document_id)
            status = document.get("status")

        # -----------------------------------------------------
        # Finished
        # -----------------------------------------------------

        if status == DOCUMENT_STATUS_VALIDATED:

            print("Document processing completed successfully.")

        elif status == DOCUMENT_STATUS_FRAUD_ANALYZED:

            print("Document already processed.")

        else:

            print(f"Document stopped at status : {status}")

        return document

    # ---------------------------------------------------------
    # Process entire travel
    # ---------------------------------------------------------

    def process_travel(
        self,
        user_id: str,
        travel_id: str,
        expense_lines: list
    ):

        print(f"\n========== Processing Travel {travel_id} ==========")

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

                "timeline": [],

                "fraudAnalysis": None
            }

        succeeded = 0
        failed = 0

        # -----------------------------------------------------
        # Process every document
        # -----------------------------------------------------

        for document in documents:

            try:

                self.process_single_document(
                    document["documentId"]
                )

                succeeded += 1

            except Exception as ex:

                failed += 1

                print(
                    f"Failed processing document "
                    f"{document['documentId']}: {str(ex)}"
                )

        # -----------------------------------------------------
        # Build Timeline
        # -----------------------------------------------------

        print("\nBuilding Timeline...")

        timeline = self.timeline_service.build_timeline(
            travel_id
        )

        # -----------------------------------------------------
        # Fraud Detection
        # -----------------------------------------------------

        print("\nRunning Fraud Detection...")

        fraud_analysis = self.fraud_service.analyze_travel(

            user_id=user_id,

            travel_id=travel_id,

            expense_lines=expense_lines
        )

        print("\nTravel processing completed successfully.")

        return {

            "travelId": travel_id,

            "documentsProcessed": len(documents),

            "documentsSucceeded": succeeded,

            "documentsFailed": failed,

            "timeline": timeline,

            "fraudAnalysis": fraud_analysis
        }