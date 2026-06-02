class RelevanceValidator:

    @staticmethod
    def validate_refund_response(response_text):
        keywords = [
            "refund",
            "payment",
            "transactions"
        ]
        return any(
            word in response_text.lower()
            for word in keywords
        )