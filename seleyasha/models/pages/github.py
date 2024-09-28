from seleyasha.managing import Browser


class GithubPullRequests:
    def __init__(self, browser: Browser):
        self.links = browser.all('[id^=issue_]:not([id$=_link])')