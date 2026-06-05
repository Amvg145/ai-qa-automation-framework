import ollama

class SelfHealingAgent:

    def suggest_locator(self, failed_locator, html_source):
        prompt = f"""
        Locator failed:
        {failed_locator}

        HTML:

        {html_source}

        Find best replacement locator

        Return only Locator
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