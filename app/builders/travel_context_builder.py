class TravelContextBuilder:

    @staticmethod
    def build(
        user_id: str,
        travel_id: str,
        documents: list,
        expense_lines: list,
        timeline: list
    ):

        valid_documents = []

        for document in documents:

            validation = document.get("validation", {})

            if not validation.get("isValid", False):
                continue

            parsed_data = document.get("parsedData", {})

            valid_documents.append({

                "documentType": parsed_data.get("documentType"),

                "data": parsed_data.get("data", {})
            })

        trip_summary = TravelContextBuilder.build_trip_summary(
            valid_documents,
            timeline
        )

        return {

            "userId": user_id,

            "travelId": travel_id,

            "tripSummary": trip_summary,

            "expenseLines": expense_lines,

            "timeline": timeline,

            "documents": valid_documents
        }

    @staticmethod
    def build_trip_summary(documents, timeline):

        summary = {

            "travelerName": None,

            "startDate": None,

            "endDate": None,

            "visitedCities": [],

            "documentCount": len(documents)
        }

        # ----------------------------
        # Traveler Name
        # ----------------------------

        for document in documents:

            data = document.get("data", {})

            traveler = data.get("travelerName")

            if traveler:

                summary["travelerName"] = traveler

                break

        # ----------------------------
        # Travel Dates
        # ----------------------------

        dates = []

        for event in timeline:

            if event.get("date"):

                dates.append(event["date"])

        if dates:

            dates.sort()

            summary["startDate"] = dates[0]

            summary["endDate"] = dates[-1]

        # ----------------------------
        # Cities
        # ----------------------------

        cities = set()

        for document in documents:

            data = document.get("data", {})

            departure = data.get("departureCity")

            arrival = data.get("arrivalCity")

            if departure:
                cities.add(departure)

            if arrival:
                cities.add(arrival)

        summary["visitedCities"] = sorted(list(cities))

        return summary