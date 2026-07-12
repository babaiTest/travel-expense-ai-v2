def build_flight_prompt(ocr_text: str):

    return f"""
Extract information from this flight ticket.

Return ONLY JSON.

{{
    "travelerName":"",
    "departureCity":"",
    "departureAirport":"",
    "arrivalCity":"",
    "arrivalAirport":"",
    "flightNumber":"",
    "travelDate":"",
    "departureTime":"",
    "seatNumber":"",
    "travelClass":""
}}

OCR Text:

{ocr_text}
"""