from selenium.webdriver import Keys
from bromium.browser import browser


browser.open('https://duckduckgo.com')

query = '[name=q]'
browser.type_request(query, value='selene' + Keys.ENTER)
browser.back()
browser.type_request(query, ' yashaka' + Keys.ENTER)
browser.click('.react-results--main>li:nth-of-type(1) [data-testid="result-title-a"]')
browser.assert_that('.md-content img', value=13)

browser.quit()
