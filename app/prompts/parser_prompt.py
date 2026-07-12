def build_parser_prompt(ocr_text: str) -> str:

    return f"""
You are an AI assistant that extracts travel expense information.

Analyze the OCR text and return ONLY valid JSON.

Do not explain anything.

Do not include markdown.

If a value is missing, use null.

Return JSON in this exact format:

{{
    "documentType": "",
    "travelerName": "",
    "flightNumber": "",
    "departureCity": "",
    "arrivalCity": "",
    "travelDate": "",
    "departureTime": "",
    "seatNumber": ""
}}

OCR Text:

{ocr_text}
"""