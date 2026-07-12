def build_document_type_prompt(ocr_text: str):

    return f"""
Identify the document type.

Supported document types:

- FlightTicket
- HotelInvoice
- CabReceipt
- MealReceipt
- TrainTicket
- Other

Return ONLY JSON.

{{
    "documentType":""
}}

OCR Text:

{ocr_text}
"""