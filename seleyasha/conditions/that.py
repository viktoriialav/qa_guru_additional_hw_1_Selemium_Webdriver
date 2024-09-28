from selenium.webdriver.remote.webdriver import WebDriver

from seleyasha.selector import to_locator


def number_of_elements(selector, value: int):
    def condition(driver: WebDriver) -> bool:
        webelements = driver.find_elements(*to_locator(selector))
        actual_value = len(webelements)
        if actual_value != value:
            raise AssertionError(f'number of elements is not {value}\nActual value: {actual_value}')
        return webelements

    return condition


def text_of_element(selector, value: str):
    def condition(driver: WebDriver) -> bool:
        webelement = driver.find_element(*to_locator(selector))
        actual_value = webelement.text.strip()
        if actual_value != value:
            raise AssertionError(f'text of element is not {value}\nActual value: {actual_value}')
        return webelement

    return condition


def value_of_element(selector, value: str):
    def condition(driver: WebDriver) -> bool:
        webelement = driver.find_element(*to_locator(selector))
        actual_value = webelement.get_attribute('value')
        if actual_value != value:
            raise AssertionError(f'value attribute of element is not {value}\nActual value: {actual_value}')
        return webelement

    return condition
