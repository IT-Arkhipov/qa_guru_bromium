from selenium.webdriver import Keys
from bromium.conditions import element, type_request, click, number_of_elements, driver, assert_that


driver.get('https://duckduckgo.com')

query = '[name=q]'
type_request(query, value='selene' + Keys.ENTER)

driver.back()
type_request(query, ' yashaka' + Keys.ENTER)
click('.react-results--main>li:nth-of-type(1) [data-testid="result-title-a"]')
assert_that('.md-content img', value=13)

driver.quit()
