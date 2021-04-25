import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

rent_url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.6753715415039%2C%22east%22%3A-122.1912864584961%2C%22south%22%3A37.32836272570824%2C%22north%22%3A38.21953465274086%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }
response = requests.get(url=rent_url,headers=HEADERS)
soup = BeautifulSoup(response.text,'html.parser')

cards = soup.find_all("div",class_="list-card-info")
rental_list = []
for card in cards:
    address = card.find("address",class_="list-card-addr").text
    address = address.split(" | ")[-1]
    link = card.find("a")['href']
    if not "https://" in link:
        link = f"https://www.zillow.com{link}"
    price = card.find("div",class_="list-card-price").text
    price = price.split("+")[0]
    price = price.split("/")[0]
    rental_list.append(
        {
            "address":f"{address}",
            "price":f"{price}",
            "link":f"{link}"
        }
    )

print(rental_list)

form_url = "https://forms.gle/yfNHym3ANj8LCKYu8"
chrome_driver_path = r"D:\Projects\100-days\day-53\resources\chromedriver.exe"


for r in rental_list:
    driver = webdriver.Chrome(chrome_driver_path)
    driver.get(form_url)
    time.sleep(2)
    
    address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
    address.send_keys(r['address'])
    price.send_keys(r['price'])
    link.send_keys(r['link'])
    submit_button.click()
    driver.quit()

