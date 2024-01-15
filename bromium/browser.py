from typing import Tuple

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class Browser:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=2, ignored_exceptions=(WebDriverException,))

    @staticmethod
    def to_locator(selector: str) -> Tuple[str, str]:
        return (By.XPATH, selector) if (
                selector.startswith('/')
                or selector.startswith('//')
                or selector.startswith('./')
                or selector.startswith('..')
                or selector.startswith('(')
        ) else (By.CSS_SELECTOR, selector)

    @staticmethod
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

    def type_request(self, selector, value):
        def command(driver: WebDriver) -> WebElement:
            web_element = driver.find_element(*self.to_locator(selector))
            web_element.send_keys(value)
            return web_element

        self.wait.until(command)

    def click(self, selector):
        def command(driver: WebDriver) -> WebElement:
            webelement = driver.find_element(*self.to_locator(selector))
            if self.is_overlapped(driver, webelement):
                raise WebDriverException
            webelement.click()
            return webelement

        self.wait.until(command)

    def assert_that(self, selector, value: int):
        def predicate(driver: WebDriver):
            webelements = driver.find_elements(*self.to_locator(selector))
            return len(webelements) == value

        self.wait.until(predicate)
