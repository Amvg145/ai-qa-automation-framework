import ollama

class FailureAnalyzer:

    def analyze_failure(self, log_text):
        prompt = f"""
        You are a Senior QA Automation Engineer.
        Analyze this pytest failure log.

        provide:

        1. Root Cause
        2. Possible Reasons
        3. Suggested Fixes
        4. Prevention Strategy

        Failure log:

        {log_text}
        """

        response = ollama.chat(
            model="llama3",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]