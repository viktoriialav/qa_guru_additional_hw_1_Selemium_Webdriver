from typing import Union, Literal

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import _element_if_visible

def to_locator(selector: str) -> tuple[str, str]:
    return (By.XPATH, selector) if (
        selector.startswith('/')
        or selector.startswith('//')
        or selector.startswith('./')
        or selector.startswith('.')
        or selector.startswith('(')
    ) else (By.CSS_SELECTOR, selector)


def element(selector):

    def command(driver: WebDriver) -> Union[Literal[False], WebElement]:
        return _element_if_visible(driver.find_element(*to_locator(selector)))

    return command


def type_to_element(selector, value):

    def command(driver: WebDriver) -> WebElement:
        webelement = driver.find_element(*to_locator(selector))
        webelement.send_keys(value)
        return webelement

    return command


def click_on_element(selector):

    def command(driver: WebDriver) -> WebElement:
        webelement = driver.find_element(*to_locator(selector))
        webelement.click()
        return webelement

    return command

# def number_of_elements(selector, value: int):
#
#     def predicate(driver: WebDriver) -> bool:
#         webelements = driver.find_element(*to_locator(selector))
#         return len(webelements) == value
#
#     return predicate


class number_of_elements:
    def __init__(self, selector, value: int):
        self.selector = selector
        self.value = value

    def __call__(self, driver: WebDriver) -> bool:
        webelements = driver.find_element(*to_locator(self.selector))
        return len(webelements) == self.value

