import time

from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from bromium.browser import Browser
from bromium.conditions import element, type, click, number_of_elements


def find_element(*args):
    return driver.find_element(By.CSS_SELECTOR, '#searchbox_input')


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, timeout=2, ignored_exceptions=(WebDriverException,))


driver.get('https://duckduckgo.com')

# driver.find_element(By.CSS_SELECTOR, '#searchbox_input').send_keys('bromium', Keys.ENTER)
wait.until(find_element).send_keys('bromium', Keys.ENTER)
time.sleep(3)

driver.quit()
