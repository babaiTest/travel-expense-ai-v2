from pydantic import BaseModel

from app.prompts.flight_prompt import build_flight_prompt
from app.prompts.hotel_prompt import build_hotel_prompt
from app.schemas.parser_output import FlightParseResult, HotelParseResult
#from app.prompts.cab_prompt import build_cab_prompt


class PromptFactory:

    _SCHEMAS: dict[str, type[BaseModel]] = {
        "FlightTicket": FlightParseResult,
        "HotelInvoice": HotelParseResult,
    }

    @staticmethod
    def get_prompt(
        document_type: str,
        ocr_text: str
    ) -> str:

        if document_type == "FlightTicket":
            return build_flight_prompt(ocr_text)

        elif document_type == "HotelInvoice":
            return build_hotel_prompt(ocr_text)

        # elif document_type == "CabReceipt":
        #     return build_cab_prompt(ocr_text)

        raise ValueError(
            f"Unsupported document type: {document_type}"
        )

    @staticmethod
    def get_schema(document_type: str) -> type[BaseModel]:
        schema = PromptFactory._SCHEMAS.get(document_type)

        if schema is None:
            raise ValueError(
                f"Unsupported document type: {document_type}"
            )

        return schema