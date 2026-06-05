import ollama

class BugReportAgent:

    def generate_bug_report(self, failure_log):
        prompt = f"""
        Generate QA bug report.

        Failure:

        {failure_log}

        Include:
        - Title
        - Severity
        - Priority
        - Module
        - Steps to reproduce
        - Expected result
        - Actual result
        - Root cause
        - Recommendation
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

        return(
            response["message"]["content"]
        )