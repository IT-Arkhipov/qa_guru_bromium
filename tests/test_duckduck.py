from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from bromium.conditions import click, number_of_elements, type

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, timeout=2, ignored_exceptions=(WebDriverException,))

driver.get('https://duckduckgo.com')

query = '[name=q]'
wait.until(type(query, value='selene' + Keys.ENTER))
driver.back()
wait.until(type(query, value=' yashaka' + Keys.ENTER))
wait.until(click('.react-results--main>li:nth-of-type(1) [data-testid="result-title-a"]'))
wait.until(number_of_elements('.md-content img', value=13))

driver.quit()
