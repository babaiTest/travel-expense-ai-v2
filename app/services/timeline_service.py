from app.repositories.document_repository import DocumentRepository
from app.timeline.builders.event_factory import EventFactory

class TimelineService:

    def __init__(self):

        self.repository = DocumentRepository()

    def build_timeline(self, travel_id):

        documents = self.repository.get_documents_by_travel_id(travel_id)

        timeline = []

        for document in documents:

            validation = document.get("validation")

            if not validation:
                continue

            if not validation["isValid"]:
                continue

            event = EventFactory.create(
                document["parsedData"]
            )

            if event:
                timeline.append(event)

        timeline.sort(
            key=lambda x: (
                x["date"],
                x.get("time") or ""
            )
        )

        return timeline