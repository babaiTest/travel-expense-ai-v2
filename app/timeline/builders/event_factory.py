from app.timeline.builders.flight_event_builder import FlightEventBuilder


class EventFactory:

    @staticmethod
    def create(parsed):

        document_type = parsed["documentType"]

        data = parsed["data"]

        if document_type == "FlightTicket":
            return FlightEventBuilder.build(data)

        return None