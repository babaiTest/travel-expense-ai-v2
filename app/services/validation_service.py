from app.repositories.document_repository import DocumentRepository
from app.validators.flight_validator import FlightValidator


class ValidationService:

    def __init__(self):

        self.repository = DocumentRepository()

    def validate_document(self, document_id: str):

        document = self.repository.get_document_by_id(document_id)

        parsed_data = document.get("parsedData")

        if parsed_data is None:
            raise Exception("Document has not been parsed.")

        document_type = parsed_data["documentType"]

        data = parsed_data["data"]

        if document_type == "FlightTicket":
            result = FlightValidator.validate(data)
            self.repository.update_validation_result(
            document_id,
            result
        )

        else:

            raise Exception(f"Unsupported document type: {document_type}")

        return result