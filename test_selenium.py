from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from mongo_connect import mongo_connect
import os

""" Run web driver and open test page"""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome('.\\drivers\\chromedriver.exe', options=chrome_options)
if os.path.exists("env.py"):
    driver.get('http://127.0.0.1:5000/'

coll = mongo_connect()

""" Check if test data exists before tests run and delete it """
if coll.find_one({"email": "selenium_test@example.com"}):
    print("----")
    print("Duplicate test data found >> deleting")
    print("----")
    coll.delete_many({"email": "selenium_test@example.com"})

""" Submit test data via form """
driver.find_element_by_id('fname').clear()
driver.find_element_by_id('fname').send_keys("Selenium")
driver.find_element_by_id('sname').clear()
driver.find_element_by_id('sname').send_keys("Test")
driver.find_element_by_id('email').clear()
driver.find_element_by_id('email').send_keys("selenium_test@example.com")
driver.implicitly_wait(2)
driver.find_element_by_id('email').send_keys(Keys.ENTER)

""" Assertions to validate from and data"""
try:
    assert driver.find_element_by_css_selector(
        '.alert').text == "Your data has been submitted"  # Check if UI element exists
    assert coll.find_one({"email": "selenium_test@example.com"})  # Check if record is found in MongoDB
except AssertionError:
    print('>> There was an assertion error! <<')
    raise AssertionError
finally:
    driver.close()
