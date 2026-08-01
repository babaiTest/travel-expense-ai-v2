def build_flight_prompt(ocr_text: str) -> str:

    return f"""
You are an expert AI specialized in extracting structured information from airline boarding passes and flight tickets.

Your task is to identify the document type first.

If the document is NOT a flight ticket or boarding pass, return:

{{
    "documentType": "Unknown",
    "data": {{}}
}}

Extraction Rules:

- Return ONLY valid JSON.
- Never explain your answer.
- Use null for missing values.
- Dates must use YYYY-MM-DD.
- Preserve airline name exactly.
- Preserve passenger name exactly.
- Extract airport codes separately from city names.
- Do not guess values.

Required JSON:

{{
    "documentType": "FlightTicket",
    "data": {{
        "travelerName": "",
        "departureCity": "",
        "departureAirport": "",
        "arrivalCity": "",
        "arrivalAirport": "",
        "flightNumber": "",
        "travelDate": "",
        "departureTime": "",
        "arrivalDate": null,
        "arrivalTime": null,
        "seatNumber": "",
        "travelClass": "",
        "airline": ""
    }}
}}

OCR Text:

{ocr_text}
"""