import logging
logger = logging.getLogger(__name__)

from app.repositories.document_repository import DocumentRepository
from app.prompts.parser_prompt import build_parser_prompt
from app.infrastructure.azure_openai import llm
from app.services.document_type_detector import DocumentTypeDetector
from app.prompts.prompt_factory import PromptFactory
from app.validators.parser_response_validator import ParserResponseValidator
import json

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
        document_type = DocumentTypeDetector.detect(ocr_text)
        prompt = PromptFactory.get_prompt(document_type, ocr_text)
        response = llm.invoke(prompt)
        parsed_data = json.loads(response.content)

        ParserResponseValidator.validate(parsed_data)

        self.document_repository.update_document_parsed_data(document_id, parsed_data)
        logger.info("Updated document parsed data in MongoDB.")
        print("Updated document parsed data in MongoDB.")
        #return ocr_text
        return parsed_data