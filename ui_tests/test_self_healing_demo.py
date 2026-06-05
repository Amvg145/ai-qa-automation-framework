def test_locator_failure():

    failed_locator = "#submit-btn"

    html = """
    <button id="send-btn">
        Submit
    </button>
    """

    from agents.self_healing_agent import SelfHealingAgent

    agent = SelfHealingAgent()

    suggested = agent.suggest_locator(
        failed_locator,
        html
    )

    assert "send-btn" in suggested