from selenium.webdriver import Keys
from bromium.browser import Browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser = Browser(driver)

browser.driver.get('https://duckduckgo.com')

query = '[name=q]'
browser.type_request(query, value='selene' + Keys.ENTER)
# 3
# element('[name=q]').type('selene' + Keys.ENTER)
# ...
# query = element('[name=q]')
# query.type('selene' + Keys.ENTER)

driver.back()
browser.type_request(query, ' yashaka' + Keys.ENTER)
# 3
# query.type(' yashaka' + Keys.ENTER)

browser.click('.react-results--main>li:nth-of-type(1) [data-testid="result-title-a"]')

browser.assert_that('.md-content img', value=13)

driver.quit()
