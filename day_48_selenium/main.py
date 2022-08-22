from selenium import webdriver

chrome_driver_path = "C:/Users/Chris/PycharmProjects/Utilities/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

upcoming_events_table = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul')

times = [element.get_attribute("datetime")[:10] for
         element in upcoming_events_table.find_elements_by_css_selector("time")]

events = [element.text for
         element in upcoming_events_table.find_elements_by_css_selector("a")]

event_dict = {}

for i in range(len(times)):
    event_dict[i] = {"time": times[i], "name": events[i]}

print(event_dict)

driver.quit()
