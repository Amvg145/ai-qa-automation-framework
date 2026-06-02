class ChatPage:

    def __init__(self, page):

        self.page = page

        self.message_input = (
            "#message-input"
        )
        self.send_button = (
            "#send-btn"
        )

        self.response_text = (
            "#response"
        )

    def open(self):
        self.page.goto("http://127.0.0.1:8000")

    def send_message(self, message):
        self.page.fill(self.message_input, message)
        self.page.click(self.send_button)

    def get_response(self):

        self.page.wait_for_selector(
            self.response_text
        )
        self.page.wait_for_timeout(
            1000
        )

        return (
            self.page.locator(self.response_text).inner_text()
        )
    
    def get_ui_response(self):
        locator = self.page.locator(
            self.response_text
        )
        locator.wait_for()
        self.page.wait_for_function(
            """
            ()=> document
            .querySelector('#response')
            .innerText.length>0
            """
        )
        return locator.inner_text()