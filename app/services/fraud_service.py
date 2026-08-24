from app.repositories.document_repository import DocumentRepository
from app.services.timeline_service import TimelineService
from app.builders.travel_context_builder import TravelContextBuilder
from app.prompts.fraud_prompt import FraudPrompt
from app.infrastructure.structured_llm import invoke_structured
from app.schemas.fraud_output import FraudAnalysisResult
from app.repositories.travel_repository import TravelRepository


class FraudService:

    def __init__(self):

        self.repository = DocumentRepository()

        self.timeline_service = TimelineService()

        self.trvelRepository = TravelRepository()

    def analyze_travel(
        self,
        user_id: str,
        travel_id: str,
        expense_lines: list
    ):

        # -----------------------------
        # Load Documents
        # -----------------------------

        documents = self.repository.get_documents_by_user_and_travel(
            user_id,
            travel_id
        )

        # -----------------------------
        # Build Timeline
        # -----------------------------

        timeline = self.timeline_service.build_timeline(travel_id)

        # -----------------------------
        # Build Travel Context
        # -----------------------------

        travel_context = TravelContextBuilder.build(
            user_id=user_id,
            travel_id=travel_id,
            documents=documents,
            expense_lines=expense_lines,
            timeline=timeline
        )

        prompt = FraudPrompt.build(travel_context)

        fraud_result = invoke_structured(prompt, FraudAnalysisResult)
        validated = fraud_result.model_dump(mode="json")

        self.trvelRepository.update_fraud_analysis(
            travel_id,
            validated
        )

        return validated
