from agents.failure_analyzer import FailureAnalyzer

try:
    with open("failure_log.txt", "r", encoding="utf-8") as file:
        log_text = file.read()

except UnicodeDecodeError:
    with open("failure_log.txt", "r", encoding="utf-16") as file:
        log_text = file.read()

# Extract only failure section
failure_lines = []
capture = False

for line in log_text.splitlines():
    if "Failed" in line:
        capture = True
    if capture:
        failure_lines.append(line)

failure_text = "\n".join(failure_lines)

analyzer = (FailureAnalyzer())
result = analyzer.analyze_failure(failure_text)

print(
    "\nAI failure Analysis:\n"
)

print(result)