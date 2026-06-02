from pages.chat_page import (ChatPage)

def test_chatbot_ui(page):
    chat_page = (
        ChatPage(page)
    )

    chat_page.open()
    chat_page.send_message(
        "refund my payment"
    )

    response = (
        chat_page.get_response()
    )

    assert (
        "refund" in response.lower()
    )