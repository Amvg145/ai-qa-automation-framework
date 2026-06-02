import json
import allure

from pages.chat_page import (ChatPage)
from ai_validators.relevance_validator import RelevanceValidator

@allure.feature(
    "End To End chat"
)
@allure.story(
    "UI API AI Validation"
)

def test_chat_end_to_end(page, api_client):
    chat_page = ChatPage(page)
    with allure.step("Open chatbot UI"):
        chat_page.open()
    with allure.step("Send message"):
        message = (
            "refund my payment"
        )
        chat_page.send_message(message)
    with allure.step("capture UI respone"):
        ui_response = chat_page.get_ui_response()
    with allure.step("call backend API"):
        payload = {
            "message": message
        }
        api_response = (
            api_client.post(
                "/chat", payload=payload
            )
        )
        backend_response = (
            api_response.json()["response"]
        )
    with allure.step("Validate UI and API response"):
        assert (ui_response == backend_response)
    with allure.step("AI relevance validation"):
        is_relevant = (
            RelevanceValidator.validate_refund_response(
                ui_response
            )
        )
        assert (is_relevant)