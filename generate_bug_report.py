from agents.bug_report_agent import BugReportAgent

with open("failure_log.txt", "r", encoding="utf-8") as file:
    log_text = file.read()

agent = BugReportAgent()
report = (
    agent.generate_bug_report(log_text)
)
print(report)