import json
import allure

from utils.response_models import (ChatResponseModel)
from ai_validators.relevance_validator import RelevanceValidator

@allure.feature(
    "Chat API"
)
@allure.story(
    "Refund validation"
)

def test_chat_api(api_client):

    
    with allure.step(
        "Load Payload"
    ):
        with open("test_data/chat_payload.json") as file:
            payload = json.load(file)
    with allure.step(
        "Send chat request"
    ):
        response = api_client.post(
            "/chat", payload
        )
    with allure.step(
         "Validate status code"
    ):
            assert (
                response.status_code == 200
            )

    response_json = response.json()
    with allure.step(
        "Validate schema"
    ):
            validate_response = (
                ChatResponseModel(**response_json)
            )
    
    with allure.step(
         "Validate AI relevance"
    ):
        is_relevant = (
            RelevanceValidator.validate_refund_response(
                validate_response.response
            )
        )

    assert (
        is_relevant
        ), (
        "AI response "
        "is not relevant"
    )
