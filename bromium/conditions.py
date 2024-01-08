from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import _element_if_visible


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
        webelement = driver.find_element(*to_locator(selector))
        webelement.send_keys(value)
        return webelement

    return command


def click(selector):
    def command(driver: WebDriver) -> WebElement:
        webelement = driver.find_element(*to_locator(selector))
        webelement.click()
        return webelement

    return command


def number_of_elements(selector, value: int):

    def predicate(driver: WebDriver):
        webelements = driver.find_elements(*to_locator(selector))
        return len(webelements) == value

    return predicate
