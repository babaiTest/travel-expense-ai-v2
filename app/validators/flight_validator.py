class FlightValidator:

    REQUIRED_FIELDS = [
        "travelerName",
        "departureCity",
        "arrivalCity",
        "travelDate"
    ]

    OPTIONAL_FIELDS = [
        "flightNumber",
        "seatNumber",
        "travelClass",
        "departureAirport",
        "arrivalAirport",
        "departureTime",
        "arrivalTime",
        "airline"
    ]

    @staticmethod
    def validate(data: dict):

        errors = []
        warnings = []

        for field in FlightValidator.REQUIRED_FIELDS:

            if not data.get(field):
                errors.append(f"{field} is missing")

        for field in FlightValidator.OPTIONAL_FIELDS:

            if not data.get(field):
                warnings.append(f"{field} is missing")

        return {
            "isValid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings
        }