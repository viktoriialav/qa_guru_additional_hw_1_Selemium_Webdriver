from selenium.webdriver.remote.webdriver import WebDriver

from seleyasha import general
from seleyasha.selector import to_locator


def number_of_elements(selector, value: int):
    def predicate(driver: WebDriver) -> bool:
        webelements = driver.find_elements(*to_locator(selector))
        return len(webelements) == value

    return general.wait.until(predicate)