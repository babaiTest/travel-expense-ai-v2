import json

SUPPORTED_DOCUMENT_TYPES = [
    "FlightTicket",
    "HotelInvoice",
    "CabReceipt",
    "MealReceipt",
    "TrainTicket",
    "Other"
]


def build_parser_prompt(ocr_text: str) -> str:

    return f"""
You are an AI assistant that extracts structured information from travel expense documents.

Supported document types:

{json.dumps(SUPPORTED_DOCUMENT_TYPES, indent=2)}

Instructions:

1. Identify the document type.
2. Extract only the fields that actually exist.
3. Return ONLY valid JSON.
4. Do NOT include markdown.
5. Do NOT explain anything.
6. If a value cannot be determined, omit that field.
7. Put all extracted fields inside the 'data' object.

Expected response format:

{{
    "documentType": "...",
    "data":
    {{
    }}
}}

OCR Text:

{ocr_text}
"""