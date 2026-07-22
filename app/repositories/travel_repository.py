from datetime import datetime

class TravelRepository:

    def create_travel(
        self,
        user_id: str,
        travel_id: str
    ):

        travel = {

            "travelId": travel_id,

            "userId": user_id,

            "status": "PROCESSING",

            "documentSummary": {

                "totalDocuments": 0,

                "processedDocuments": 0,

                "validDocuments": 0,

                "invalidDocuments": 0
            },

            "timeline": [],

            "fraudAnalysis": None,

            "createdAt": datetime.utcnow(),

            "modifiedAt": datetime.utcnow()
        }

        self.collection.insert_one(travel)