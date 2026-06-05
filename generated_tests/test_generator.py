import re
from pathlib import Path

class TestGenerator:

    def generate_pytest_file(self, ai_output, file_name="generated_tests/test_ai_generated.py"):
        lines = ai_output.split("\n")
        test_cases = []
        for line in lines:
            if line.strip().startswith("*") or line.strip().startswith("-"):
                test_cases.append(line.strip("*- "))
        code=[]
        code.append("import pytest\n")
        # extract quoted test_case_name
        matches = re.findall(
            r'"test_case_name":\s*"([^"]+)"',
            ai_output
        )
        if not matches:
            matches = [
                "positive_case",
                "negative_case",
                "edge_case"
            ]

        for case in matches:
            safe_name = re.sub(r'[^a-zA-Z0-9]+', '_', case.lower()).strip("_")
            code.append(
                f"\ndef test_{safe_name}():"
            )
            code.append(
                f'\n    print("{case}")'
            )
            code.append(
                f'\n    assert True\n'
            )
        Path(file_name).write_text("".join(code))
        print(
            f"Generated: {file_name}"
        )