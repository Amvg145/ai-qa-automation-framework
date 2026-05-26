import requests

BASE_URL = "http://127.0.0.1:8000"

def test_chat_api():
    response = requests.post(
        f"{BASE_URL}/chat"
    )
    assert response.status_code == 200
    response_json = response.json()
    assert "refund" in response_json[
        "response"
    ].lower()
