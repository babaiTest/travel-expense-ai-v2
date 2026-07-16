class ParserResponseValidator:

    @staticmethod
    def validate(parsed_document: dict):

        if "documentType" not in parsed_document:
            raise Exception("documentType missing")

        if "data" not in parsed_document:
            raise Exception("data missing")