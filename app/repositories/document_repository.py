from datetime import datetime

from app.infrastructure.mongodb import document_collection
from app.constants import DOCUMENT_STATUS_OCR_COMPLETED,DOCUMENT_STATUS_PARSED
import json


class DocumentRepository:

    def save_document(self,document: dict):

        document["created_at"] = datetime.utcnow()

        result = document_collection.insert_one(document)

        return str(result.inserted_id)

    def get_document_by_id(self, document_id: str):
        #print("Searching for:", document_id)
        document = document_collection.find_one(
        {
            "documentId": document_id
        }
    )

        #print("Result:", document)
        return document
    

    def update_document_ocr(
        self,
        document_id: str,
        ocr_text: str
    ):

        document_collection.update_one(
            {
                "documentId": document_id
            },
            {
                "$set":
                {
                    "ocrText": ocr_text,
                    "status":  DOCUMENT_STATUS_OCR_COMPLETED,
                    "modified_at": datetime.utcnow()
                }
            }
        )

    def update_document_parsed_data(
        self,
        document_id: str,
        parsed_data: dict
    ):

        result = document_collection.update_one(
            {
                "documentId": document_id
            },
            {
                "$set": {
                    "model": "gpt-4.1-mini",
                    "version": "1.0",
                    "parsedAt": datetime.utcnow(),
                    "modified_at": datetime.utcnow()
                }
            }
        )
        return result.modified_count == 1