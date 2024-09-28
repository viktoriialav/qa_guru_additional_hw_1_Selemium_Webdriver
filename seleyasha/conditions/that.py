from selenium.webdriver.remote.webdriver import WebDriver

from seleyasha.selector import to_locator


def number_of_elements(selector, value: int):
    def predicate(driver: WebDriver) -> bool:
        webelements = driver.find_elements(*to_locator(selector))
        actual_value = len(webelements)
        if actual_value != value:
            raise AssertionError(f'number of elements is not {value}\nActual value: {actual_value}')
        return webelements

    return predicate
