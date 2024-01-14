import time

from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from bromium.conditions import element


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, timeout=2, ignored_exceptions=(WebDriverException,))


driver.get('https://duckduckgo.com')

wait.until(element(By.CSS_SELECTOR, '#searchbox_input')).send_keys('bromium', Keys.ENTER)

wait.until(element(
    By.CSS_SELECTOR, '.react-results--main li:nth-child(2) [data-testid="result-title-a"]')
).click()

time.sleep(3)

driver.quit()
