from app.infrastructure.mongodb import database
from app.repositories.document_repository import DocumentRepository
from app.services.ocr_service import OCRService
from app.services.parser_service import ParserService
from app.infrastructure.azure_openai import llm
from app.services.validation_service import ValidationService
from app.services.timeline_service import TimelineService
from app.services.travel_processing_service import TravelProcessingService

#print("Connected successfully!")
#print("Database Name:", database.name)

#obj = DocumentRepository()
#document = obj.get_document_by_id("4279479d-8031-4e0b-aa13-f6776ff3fa57")
#print("Document:", document)

# ocr = OCRService()
# document = ocr.process_document("4279479d-8031-4e0b-aa13-f6776ff3fa57")
# print(document)
# file_bytes = ocr.process_document("4279479d-8031-4e0b-aa13-f6776ff3fa57")
# print(len(file_bytes))
# with open("downloaded_file.png", "wb") as file:
#     file.write(file_bytes)

# from app.infrastructure.document_intelligence import (
#     document_intelligence_client
# )

# print(document_intelligence_client)

# parser = ParserService()
# text = parser.parse_document("4279479d-8031-4e0b-aa13-f6776ff3fa57")
# print(text)

# response = llm.invoke("Reply with exactly: Azure OpenAI is working")
# print(response.content)

#validation test
# validation_service = ValidationService()
# validation_result = validation_service.validate_document("4279479d-8031-4e0b-aa13-f6776ff3fa57")
# print(validation_result)

#timeline test
# timeline_service = TimelineService()
# timeline = timeline_service.build_timeline("TRV1001")
# print(timeline)

service = TravelProcessingService()
result = service.process_travel(
    "EMP101",
    "TRV1001"
)
print(result)