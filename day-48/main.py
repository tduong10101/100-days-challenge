from selenium import webdriver
from datetime import datetime
chrome_driver_path = "D:\\Projects\\100-days\\day-48\\resources\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.python.org/")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

event_time = driver.find_elements_by_css_selector(".event-widget li time")
event_title = driver.find_elements_by_css_selector(".event-widget li a")
events = {}
for index, et in enumerate(event_time):
    dt_object = datetime.fromisoformat(event_time[index].get_attribute("datetime"))
    dt_format = datetime.strftime(dt_object,"%Y-%m-%d")
    print(et.text)
    events[index] = {
        "time" : dt_format,
        "name" : event_title[index].text
    }

print(events)
# driver.close()
driver.quit()