from agents.test_case_agent import (TestCaseAgent)
from generated_tests.test_generator import TestGenerator

agent = TestCaseAgent()
generator = (
    TestGenerator()
)

response = (
    agent.generate_test_cases(
        "refund chatbot"
    )
)

print("\nGenerated Test Cases:\n")
print(response)
generator.generate_pytest_file(response)

