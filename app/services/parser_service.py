import logging

logger = logging.getLogger(__name__)

from app.repositories.document_repository import DocumentRepository
from app.infrastructure.structured_llm import invoke_structured
from app.services.document_type_detector import DocumentTypeDetector
from app.prompts.prompt_factory import PromptFactory


class ParserService:

    def __init__(self):

        self.document_repository = DocumentRepository()

    def parse_document(self, document_id: str):
        try:
            document = self.document_repository.get_document_by_id(document_id)

            if document is None:
                raise Exception("Document not found")

            ocr_text = document.get("ocrText")

            if not ocr_text:
                raise Exception("OCR not completed.")

            document_type = DocumentTypeDetector.detect(ocr_text)
            prompt = PromptFactory.get_prompt(document_type, ocr_text)
            schema = PromptFactory.get_schema(document_type)

            parsed_result = invoke_structured(prompt, schema)
            parsed_data = parsed_result.model_dump(mode="json")

            self.document_repository.update_document_parsed_data(
                document_id,
                parsed_data,
            )
            logger.info("Updated document parsed data in MongoDB.")
            print("Updated document parsed data in MongoDB.")
            return parsed_data
        except Exception as ex:
            print(
                f"Failed processing document "
                f"{document_id}: {str(ex)}"
            )


