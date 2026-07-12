from app.infrastructure.mongodb import database
from app.repositories.document_repository import DocumentRepository
from app.services.ocr_service import OCRService
from app.services.parser_service import ParserService
from app.infrastructure.azure_openai import llm

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

parser = ParserService()
text = parser.parse_document("4279479d-8031-4e0b-aa13-f6776ff3fa57")
print(text)

# response = llm.invoke("Reply with exactly: Azure OpenAI is working")
# print(response.content)