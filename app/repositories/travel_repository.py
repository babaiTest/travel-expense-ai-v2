from datetime import datetime, timezone

from app.infrastructure.mongodb import travel_collection
from app.constants import (
    TRAVEL_STATUS_PROCESSING,
    TRAVEL_STATUS_COMPLETED,
    TRAVEL_STATUS_FAILED,
    TRAVEL_STATUS_MANUAL_REVIEW
)


class TravelRepository:

    def __init__(self):
        self.collection = travel_collection

    # ---------------------------------------------------------
    # Create Travel
    # ---------------------------------------------------------

    def create_travel(
        self,
        user_id: str,
        travel_id: str
    ):
        """
        Creates a travel record if it does not already exist.

        Parameters:
            user_id (str): Employee/User ID
            travel_id (str): Travel ID

        Returns:
            dict: Travel document
        """

        existing = self.collection.find_one(
            {
                "travelId": travel_id
            }
        )

        if existing:
            return existing

        now = datetime.now(timezone.utc)

        travel = {

            "travelId": travel_id,
            "userId": user_id,
            "status": TRAVEL_STATUS_PROCESSING,
            "documentSummary": {
                "totalDocuments": 0,
                "processedDocuments": 0,
                "validDocuments": 0,
                "invalidDocuments": 0
            },

            "timeline": [],
            "fraudAnalysis": None,
            "createdAt": now,
            "modifiedAt": now
        }

        result = self.collection.insert_one(travel)

        travel["_id"] = result.inserted_id

        return travel

    # ---------------------------------------------------------
    # Get Travel
    # ---------------------------------------------------------

    def get_travel(
        self,
        travel_id: str
    ):
        """
        Returns travel by travel id.
        """

        return self.collection.find_one(
            {
                "travelId": travel_id
            }
        )

    # ---------------------------------------------------------
    # Update Document Summary
    # ---------------------------------------------------------

    def update_document_summary(
        self,
        travel_id: str,
        summary: dict
    ):
        """
        Updates document summary.
        """

        return self.collection.update_one(
            {
                "travelId": travel_id
            },
            {
                "$set": {
                    "documentSummary": summary,
                    "modifiedAt": datetime.now(timezone.utc)
                }
            }
        )

    # ---------------------------------------------------------
    # Update Timeline
    # ---------------------------------------------------------

    def update_timeline(
        self,
        travel_id: str,
        timeline: list
    ):
        """
        Updates generated travel timeline.
        """

        return self.collection.update_one(
            {
                "travelId": travel_id
            },
            {
                "$set": {
                    "timeline": timeline,
                    "modifiedAt": datetime.now(timezone.utc)
                }
            }
        )

    

    # ---------------------------------------------------------
    # Update Status
    # ---------------------------------------------------------

    def update_status(
        self,
        travel_id: str,
        status: str
    ):
        """
        Updates travel processing status.
        """

        return self.collection.update_one(
            {
                "travelId": travel_id
            },
            {
                "$set": {
                    "status": status,
                    "modifiedAt": datetime.now(timezone.utc)
                }
            }
        )

    # ---------------------------------------------------------
    # Delete Travel (Optional Utility)
    # ---------------------------------------------------------

    def delete_travel(
        self,
        travel_id: str
    ):
        """
        Deletes a travel document.
        Useful during development/testing.
        """

        return self.collection.delete_one(
            {
                "travelId": travel_id
            }
        )

    # ---------------------------------------------------------
    # Update Fraud Analysis
    # ---------------------------------------------------------
    def update_fraud_analysis(
    self,
    travel_id: str,
    fraud_result: dict
):
        """
        Updates fraud analysis for a travel.

        Parameters:
            travel_id (str): Travel ID
            fraud_result (dict): AI generated fraud analysis

        Returns:
            UpdateResult
        """

        return self.collection.update_one(
            {
                "travelId": travel_id
            },
            {
                "$set": {
                    "fraudAnalysis": fraud_result,
                    "modifiedAt": datetime.now(timezone.utc)
                }
            }
        )