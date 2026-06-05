import ollama

class TestCaseAgent:

    def generate_test_cases(self, feature):
        prompt = """
                Generate QA test cases for:
                {feature} 
                 Include:
                - positive cases
                - negative cases
                - edge cases
                - security cases

                Return structured list.
                """
        response = (
            ollama.chat(
                model= "llama3",
                messages= [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
        )
        return (
            response["message"]["content"]
        )