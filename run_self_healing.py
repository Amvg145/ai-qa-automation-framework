from agents.self_healing_agent import SelfHealingAgent

html = """
<html>
<body>
    <button id="send-btn">
      Submit
    </button>
</body>
</html>
"""

agent = SelfHealingAgent()

new_locator = agent.suggest_locator(
    "submit-btn",
    html
)

print("\nSuggested Locator:")
print(new_locator)