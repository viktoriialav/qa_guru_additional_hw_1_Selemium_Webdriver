from typing import Union, Literal

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from seleyasha import general
from seleyasha.selector import to_locator


def element(selector):

    def command(driver: WebDriver) -> Union[Literal[False], WebElement]:
        webelement = driver.find_element(*to_locator(selector))
        if not webelement.is_displayed():
            raise AssertionError(f'Element is not displayed: {webelement.get_attribute("outerHTML")}')
        return webelement

    return general.wait.until(command)


def type(selector, value):

    def command(driver: WebDriver) -> WebElement:
        webelement = driver.find_element(*to_locator(selector))
        webelement.send_keys(value)
        return webelement

    return general.wait.until(command)


def click(selector):

    def command(driver: WebDriver) -> WebElement:
        webelement = driver.find_element(*to_locator(selector))
        webelement.click()
        return webelement

    return general.wait.until(command)