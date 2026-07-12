class DocumentTypeDetector:

    @staticmethod
    def detect(ocr_text: str):

        text = ocr_text.upper()

        if "BOARDING PASS" in text:
            return "FlightTicket"

        if "HOTEL" in text:
            return "HotelInvoice"

        if "UBER" in text or "OLA" in text:
            return "CabReceipt"

        if "RESTAURANT" in text:
            return "MealReceipt"

        return "Other"