from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from seleyasha.conditions import that
from seleyasha.managing import Browser, Config

browser = Browser(driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())),
                  config=Config(timeout=2, base_url='https://www.ecosia.org'))
browser.open('/')

query = '[name=q]'
browser.type(query, value='selene' + Keys.ENTER)
browser.back()
browser.type(query, value=' yashaka pull requests' + Keys.ENTER)
browser.click('[data-test-id=mainline-result-web]:nth-of-type(1) a')

browser.assert_(that.number_of_elements('[id^=issue_]:not([id$=_link])', value=11))

browser.quit()
