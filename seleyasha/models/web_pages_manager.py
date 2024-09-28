from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from seleyasha.managing import Browser, Config
from seleyasha.models.pages.ecosia import Ecosia
from seleyasha.models.pages.github import GithubPullRequests


class WebManager:
    def __init__(self, browser: Browser):
        self.ecosia = Ecosia(browser)
        self.github_pull_requests = GithubPullRequests(browser)


browser = Browser(driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())),
                  config=Config(timeout=2, base_url='https://www.ecosia.org'))

web = WebManager(browser)