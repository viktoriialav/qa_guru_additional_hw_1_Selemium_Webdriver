from dataclasses import dataclass
from typing import Union, Literal

from selenium.common import WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from seleyasha.selector import to_locator
from seleyasha.wait import WebDriverWait


@dataclass
class Config:
    timeout: int = 2
    base_url: str = ''


class Browser:
    def __init__(self, driver: WebDriver, config=Config()):
        self.driver = driver
        self.config = config
        self.wait = WebDriverWait(
            driver=driver,
            timeout=config.timeout,
            poll_frequency=0.25,
            ignored_exceptions=(WebDriverException,)
        )

    def open(self, relative_url):
        self.driver.get(self.config.base_url + relative_url)

    def quit(self):
        self.driver.quit()

    def back(self):
        self.driver.back()

    def element(self, selector):
        def command(driver: WebDriver) -> Union[Literal[False], WebElement]:
            webelement = driver.find_element(*to_locator(selector))
            if not webelement.is_displayed():
                raise AssertionError(f'element is not displayed: {webelement.get_attribute("outerHTML")}')
            return webelement

        return self.wait.until(command, message=f'element by {selector} is not ready')

    def type(self, selector, value):
        def command(driver: WebDriver) -> WebElement:
            webelement = driver.find_element(*to_locator(selector))
            webelement.send_keys(value)
            return webelement

        return self.wait.until(command, message=f'failed to type «{value}» into element by {selector}')

    def click(self, selector):
        def command(driver: WebDriver) -> WebElement:
            webelement = driver.find_element(*to_locator(selector))
            webelement.click()
            return webelement

        return self.wait.until(command, message=f'failed to click on element by {selector}')

    def assert_(self, condition):
        return self.wait.until(condition)
