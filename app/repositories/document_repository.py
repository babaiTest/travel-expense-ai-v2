from datetime import datetime

from app.infrastructure.mongodb import document_collection
from app.constants import DOCUMENT_STATUS_OCR_COMPLETED,DOCUMENT_STATUS_PARSED
import json


class DocumentRepository:

    

    def save_document(self,document: dict):

        document["processing"] = {
        "ocrCompleted": False,
        "parserCompleted": False,
        "validationCompleted": False,
        "timelineCompleted": False,
        "fraudCompleted": False,
        "embeddingCompleted": False
        }

        document["modified_at"] = datetime.utcnow()

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
                "$set":
                    {
                        "parsedData": parsed_data,

                        "status": DOCUMENT_STATUS_PARSED,                        

                        "modified_at": datetime.utcnow()
                    }
            }
        )
        return result.modified_count == 1
    
    def update_validation_result(
        self,
        document_id: str,
        validation_result: dict
):

        document_collection.update_one(
            {
                "documentId": document_id
            },
            {
                "$set":
                {
                    "validation": validation_result,
                    "modified_at": datetime.utcnow()
                }
            }
        )

    def get_documents_by_travel_id(
    self,
    travel_id: str
    ):
        return list(
        document_collection.find(
            {
                "travelId": travel_id
            }
        )
    )

    def get_documents_by_user_and_travel(
    self,
    user_id: str,
    travel_id: str
):

        return list(
            document_collection.find(
                {
                    "userId": user_id,
                    "travelId": travel_id
                }
            )
        )