import json


class FraudPrompt:

    @staticmethod
    def build(travel_context: dict) -> str:

        return f"""
You are an AI travel expense auditor.

Your responsibility is to analyze an employee's travel claim.

You will receive:

1. Trip Summary
2. Expense Lines
3. Timeline
4. Travel Documents

Your objectives are:

- Verify that expenses align with the itinerary.
- Detect duplicate claims.
- Detect unsupported expenses.
- Detect personal expenses.
- Detect suspicious locations.
- Detect inconsistent travel dates.
- Assess the overall fraud risk.

Return ONLY valid JSON.

Required JSON format:

{{
    "summary": "...",

    "riskAssessment": {{
        "riskLevel": "LOW | MEDIUM | HIGH",
        "fraudScore": 0,
        "recommendation": "APPROVE | MANUAL_REVIEW | REJECT"
    }},

    "observations": [],

    "potentialIssues": [],

    "confidence": 0.0
}}

Travel Context:

{json.dumps(travel_context, indent=2)}
"""