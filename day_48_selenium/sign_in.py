from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import config

chrome_driver_path = "C:/Users/Chris/PycharmProjects/Utilities/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element_by_name("fName")
lname = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")

button = driver.find_element_by_css_selector("button")

fname.send_keys(config.first_name)
lname.send_keys(config.last_name)
email.send_keys(config.email)

button.click()
