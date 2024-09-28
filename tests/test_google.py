from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from seleyasha.managing import Browser, Config

browser = Browser(driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())),
                  config=Config(timeout=2, base_url='https://www.ecosia.org'))
browser.open('/')

query = browser.element('[name=q]')
query.type('selene' + Keys.ENTER)
browser.back()
query.type(' yashaka pull requests' + Keys.ENTER)
browser.element('[data-test-id=mainline-result-web]:nth-of-type(1) a').click()

browser.all('[id^=issue_]:not([id$=_link])').assert_amount(11)

browser.quit()
