from selenium import webdriver

chrome_driver_path = "D:\\Projects\\100-days\\day-48\\resources\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")

big_cookie = driver.find_element_by_id("bigCookie")

while True:
    big_cookie.click()
    upgrade = driver.find_elements_by_css_selector("div[class='crate upgrade']")
    unlocked_products = driver.find_elements_by_css_selector("div[class='product unlocked enabled']")    
    unlocked_upgrade = driver.find_elements_by_css_selector("div[class='crate upgrade enabled']")
    if len(unlocked_upgrade) > 0:
        unlocked_upgrade[-1].click()
    if len(unlocked_products) > 0:
        unlocked_products[-1].click()