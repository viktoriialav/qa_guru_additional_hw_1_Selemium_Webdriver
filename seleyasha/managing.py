from typing import Union, Literal

from selenium.common import WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from seleyasha.selector import to_locator
from seleyasha.wait import WebDriverWait


class Browser:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(
            driver, timeout=2,
            poll_frequency=0.25,
            ignored_exceptions=(WebDriverException,)
        )

    def open(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def back(self):
        self.driver.back()

    def element(self, selector):
        def command(driver: WebDriver) -> Union[Literal[False], WebElement]:
            webelement = driver.find_element(*to_locator(selector))
            if not webelement.is_displayed():
                raise AssertionError(f'Element is not displayed: {webelement.get_attribute("outerHTML")}')
            return webelement

        return self.wait.until(command)

    def type(self, selector, value):
        def command(driver: WebDriver) -> WebElement:
            webelement = driver.find_element(*to_locator(selector))
            webelement.send_keys(value)
            return webelement

        return self.wait.until(command)

    def click(self, selector):
        def command(driver: WebDriver) -> WebElement:
            webelement = driver.find_element(*to_locator(selector))
            webelement.click()
            return webelement

        return self.wait.until(command)

    def assert_(self, condition):
        return self.wait.until(condition)
