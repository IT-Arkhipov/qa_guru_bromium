from typing import Tuple

from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import _element_if_visible


def is_overlapped(driver, _element) -> bool:
    _is_overlapped = driver.execute_script(
        '''
        var element = arguments[0];
        var rect = element.getBoundingClientRect();
        var x = rect.left + rect.width/2;
        var y = rect.top + rect.height/2;
        var elementByXnY = document.elementFromPoint(x,y);
        if (elementByXnY === null) {
          return false;
        } else {
          return !element.isSameNode(elementByXnY);
        }
        ''', _element)
    return _is_overlapped


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
        if is_overlapped(driver, webelement):
            raise WebDriverException
        webelement.click()
        return webelement

    return command


def number_of_elements(selector, value: int):

    def predicate(driver: WebDriver):
        webelements = driver.find_elements(*to_locator(selector))
        return len(webelements) == value

    return predicate
