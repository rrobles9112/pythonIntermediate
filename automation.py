from selenium import webdriver


chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()
chrome_browser.get(
    'https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title
button = chrome_browser.find_element_by_class_name('btn-default').click()
button.click()

print(chrome_browser.find_element_by_id('sum1').text)
