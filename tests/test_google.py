from seleyasha.models.web_pages_manager import browser, web

browser.open('/')

web.ecosia.query.assert_value('').type('selene').press_enter()
browser.back()
web.ecosia.query.type(' yashaka pull requests').press_enter()
web.ecosia.first_result_link.assert_text('https://github.com › yashaka › selene › pulls').click()

web.github_pull_requests.links.assert_amount(11)

browser.quit()
