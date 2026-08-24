def build_flight_prompt(ocr_text: str) -> str:

    return f"""
You are an expert AI specialized in extracting structured information from airline boarding passes and flight tickets.

If the document is NOT a flight ticket or boarding pass, set documentType to "Unknown" and leave data fields empty.

Extraction Rules:

- Use null for missing values.
- Dates must use YYYY-MM-DD.
- Preserve airline name exactly.
- Preserve passenger name exactly.
- Extract airport codes separately from city names.
- Do not guess values.

OCR Text:

{ocr_text}
"""