class FlightEventBuilder:

    @staticmethod
    def build(data):

        return {

            "eventType": "Flight",

            "date": data["travelDate"],

            "time": data.get("departureTime"),

            "title": "Flight",

            "description":
                f'{data["departureCity"]} → {data["arrivalCity"]}',

            "details": data
        }