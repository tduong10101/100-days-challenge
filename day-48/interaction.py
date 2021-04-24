from selenium import webdriver

chrome_driver_path = "D:\\Projects\\100-days\\day-48\\resources\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element_by_name("fName")
lname = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")

fname.send_keys("Terry")
lname.send_keys("Duong")
email.send_keys("tduong10101@gmail.com")

sign_up = driver.find_element_by_css_selector(".btn")
sign_up.click()
