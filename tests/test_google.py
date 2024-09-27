import time

from selenium.webdriver import Keys

from seleyasha import general
from seleyasha.conditions import number_of_elements
from seleyasha.commands import type, click

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

general.driver.get('https://www.ecosia.org/')

query='[name=q]'
type(query, value='selene' + Keys.ENTER)

general.driver.back()

type(query, value=' yashaka pull requests' + Keys.ENTER)

click('[data-test-id=mainline-result-web]:nth-of-type(1) a')

number_of_elements('[id^=issue_]:not([id$=_link])', value=11)


time.sleep(2)


general.driver.quit()