from selenium.webdriver import Keys

from seleyasha.models.web_pages_manager import browser, web

browser.open('/')

web.ecosia.query.type('selene' + Keys.ENTER)
browser.back()
web.ecosia.query.type(' yashaka pull requests' + Keys.ENTER)
web.ecosia.first_result_link.click()

web.github_pull_requests.links.assert_amount(11)

browser.quit()
