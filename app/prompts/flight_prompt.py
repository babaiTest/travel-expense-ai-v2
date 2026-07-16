from app.schemas.flight_schema import FLIGHT_SCHEMA

def build_flight_prompt(ocr_text: str):

    return f"""
You are an AI assistant that extracts data from airline boarding passes and flight tickets.

Return ONLY valid JSON.

Use EXACTLY this schema:

{FLIGHT_SCHEMA}

Rules:

- Do not invent values.
- Use null when unavailable.
- Convert travelDate to YYYY-MM-DD.
- Convert arrivalDate to YYYY-MM-DD.
- Use 24-hour time.
- Split airports from cities when possible.

OCR Text:

{ocr_text}
"""