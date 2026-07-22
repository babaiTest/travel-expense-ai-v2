class FraudResponseValidator:

    REQUIRED_FIELDS = [

        "summary",

        "riskAssessment",

        "observations",

        "potentialIssues",

        "confidence"
    ]

    @staticmethod
    def validate(response: dict):

        missing = []

        for field in FraudResponseValidator.REQUIRED_FIELDS:

            if field not in response:

                missing.append(field)

        if missing:

            raise ValueError(
                f"Missing fields: {', '.join(missing)}"
            )

        return response