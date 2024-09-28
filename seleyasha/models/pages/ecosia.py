from seleyasha.browser import Browser


class Ecosia:
    def __init__(self, browser: Browser):
        self.query = browser.element('[name=q]')
        self.first_result_link = browser.element('[data-test-id=mainline-result-web]:nth-of-type(1) a')
