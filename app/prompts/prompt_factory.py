from app.prompts.flight_prompt import build_flight_prompt
from app.prompts.hotel_prompt import build_hotel_prompt
from app.prompts.cab_prompt import build_cab_prompt
from app.prompts.generic_prompt import build_generic_prompt


class PromptFactory:

    @staticmethod
    def get_prompt(document_type: str, ocr_text: str):

        if document_type == "FlightTicket":
            return build_flight_prompt(ocr_text)

        elif document_type == "HotelInvoice":
            return build_hotel_prompt(ocr_text)

        elif document_type == "CabReceipt":
            return build_cab_prompt(ocr_text)

        return build_generic_prompt(ocr_text)