from selenium import webdriver
import time

chrome_driver_path = "C:/Users/Chris/PycharmProjects/Utilities/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://tinder.com/")

time.sleep(3)

log_in = driver.find_element_by_xpath('//*[@id="o41285377"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
log_in.click()

time.sleep(3)

google = driver.find_element_by_xpath('//*[@id="o-1687095699"]/div/div/div[1]/div/div[3]/span/div[1]/div/button')
google.click()

time.sleep(3)

base_window = driver.window_handles[0]
login_window = driver.window_handles[-1]
driver.switch_to.window(login_window)

email_window = driver.find_element_by_xpath('//*[@id="identifierId"]')
email_window.send_keys("cshinepython@gmail.com")

submit_email = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[3]')
submit_email.click()
