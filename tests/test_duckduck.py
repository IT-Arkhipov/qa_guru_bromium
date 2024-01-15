
from selenium.common import WebDriverException
from selenium.webdriver import Keys

from selenium.webdriver.common.by import By


from bromium.browser import Browser
from bromium.conditions import element, type_request, click, number_of_elements, driver, assert_that

# 2
browser = Browser(driver)

driver.get('https://duckduckgo.com')

'''
# in Selene:
browser.element('[name=q]').type('selene').press_enter()
# in Selenium WebDriver:
driver.find_element(By.CSS_SELECTOR, '[name=q]').send_keys('selene', Keys.ENTER)
# OR with wait
def find_element(driver):
    return driver.find_element(By.CSS_SELECTOR, '[name=q]')
wait.until(find_element).send_keys('selene', Keys.ENTER)
# OR with built-in expected condition
wait.until(visibility_of_element_located((By.NAME, 'q'))).send_keys('selene yashaka', Keys.ENTER)
# OR with custom expected condition
wait.until(element('[name=q]')).send_keys('selene yashaka', Keys.ENTER)
'''

query = '[name=q]'
# wait.until(type_request(query, value='selene' + Keys.ENTER))
# 1
# type_request(query, value='selene' + Keys.ENTER)
# 2
browser.type_request(query, value='selene' + Keys.ENTER)
# 3
# element('[name=q]').type('selene' + Keys.ENTER)
# ...
# query = element('[name=q]')
# query.type('selene' + Keys.ENTER)

driver.back()

# wait.until(type(query, value=' yashaka' + Keys.ENTER))
# 1
# type_request(query, ' yashaka' + Keys.ENTER)
# 2
browser.type_request(query, ' yashaka' + Keys.ENTER)
# 3
# query.type(' yashaka' + Keys.ENTER)

# wait.until(click('.react-results--main>li:nth-of-type(1) [data-testid="result-title-a"]'))
# 1
# click('.react-results--main>li:nth-of-type(1) [data-testid="result-title-a"]')
# 2
browser.click('.react-results--main>li:nth-of-type(1) [data-testid="result-title-a"]')

# wait.until(number_of_elements('.md-content img', value=13))
# 1
# assert_that('.md-content img', value=13)
# 2
browser.assert_that('.md-content img', value=13)
'''
# less stable version:
number_of_pulls = len(driver.find_elements(By.CSS_SELECTOR, '[id^=issue_]:not([id$=_link])'))
assert number_of_pulls == 4
'''

driver.quit()
