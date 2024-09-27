import time

from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from seleyasha.conditions import type_to_element, click_on_element, number_of_elements

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, timeout=2, poll_frequency=0.25, ignored_exceptions=(WebDriverException, ))
driver.get('https://www.ecosia.org/')

'''
# ___ in Selenium Webdriver
driver.find_element(By.CSS_SELECTOR, '[name=q]').send_keys('selene', Keys.ENTER)

# ____ with wait

wait.until(
    lambda driver: driver.find_element(By.CSS_SELECTOR, '[name=q]')
).send_keys('selene yashaka', Keys.ENTER)

wait.until(
    lambda driver: driver.find_element(By.CSS_SELECTOR, '[data-test-id=mainline-result-web]:nth-of-type(1) a')
).click()

# ____ OR with build-in expected condition

wait.until(
    visibility_of_element_located((By.CSS_SELECTOR, '[name=q]'))
).send_keys('selene yashaka', Keys.ENTER)

wait.until(
    visibility_of_element_located((By.CSS_SELECTOR, '[data-test-id=mainline-result-web]:nth-of-type(1) a'))
).click()

number_of_pulls = len(driver.find_elements(By.CSS_SELECTOR, '[id^=issue_]:not([id$=_link])'))
assert number_of_pulls == 11

'''

wait.until(type_to_element('[name=q]', value='selene yashaka pull requests' + Keys.ENTER))

wait.until(click_on_element('[data-test-id=mainline-result-web]:nth-of-type(1) a'))

wait.until(number_of_elements('[id^=issue_]:not([id$=_link])', value=4))


time.sleep(2)
