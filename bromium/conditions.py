from typing import Tuple

from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import _element_if_visible


def is_covered(driver, _element) -> bool:
    script = """
    function isElementOverlapped(element) {
        var rect = element.getBoundingClientRect();
        var elements = document.elementsFromPoint(rect.x, rect.y);
        var isOverlapped = false;
    
        for (var i = 0; i < elements.length; i++) {
            if (elements[i] !== element && elements[i].contains(element)) {
                isOverlapped = true;
                break;
            }
        }
    
        return isOverlapped;
    }
    """

    _is_covered = driver.execute_script(script + """
    var is_covered = isElementOverlapped(arguments[0]);
    return is_covered;
    """, _element)

    return _is_covered


def to_locator(selector: str) -> Tuple[str, str]:
    return (By.XPATH, selector) if (
        selector.startswith('/')
        or selector.startswith('//')
        or selector.startswith('./')
        or selector.startswith('..')
        or selector.startswith('(')
    ) else (By.CSS_SELECTOR, selector)


def element(selector):
    def predicate(driver):
        return _element_if_visible(driver.find_element(*to_locator(selector)))

    return predicate


def type(selector, value):
    def command(driver: WebDriver) -> WebElement:
        web_element = driver.find_element(*to_locator(selector))
        web_element.send_keys(value)
        return web_element

    return command


def click(selector):
    def command(driver: WebDriver) -> WebElement:
        webelement = driver.find_element(*to_locator(selector))
        if is_covered(driver, webelement):
            raise WebDriverException
        webelement.click()
        return webelement

    return command


def number_of_elements(selector, value: int):

    def predicate(driver: WebDriver):
        webelements = driver.find_elements(*to_locator(selector))
        return len(webelements) == value

    return predicate
