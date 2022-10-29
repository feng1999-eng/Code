from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
try:
    browser.get('https://www.python.org')
    assert "Python" in browser.title
    elem = browser.find_element_by_name("q")
    elem.clear()
    elem.send_keys("python")
    elem.send_keys(Keys.RETURN)


finally:
    browser.close()