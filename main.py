gform_url = "https://docs.google.com/forms/d/e/1FAIpQLSdiU4zbVxdp3UHYniVMn2PupJ7ydl45F76pGaR5agi6Pn3zLQ/viewform?usp=sf_link"

from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
soup = BeautifulSoup(response.text , 'html.parser')


address_raw_list = soup.select(selector = ".StyledPropertyCardDataArea-anchor address ")
link_raw_list = soup.select(selector = ".StyledPropertyCardDataWrapper a ")
price_raw_list = soup.select(selector = ".PropertyCardWrapper span ")
address = []
link = []
price= []
for i in address_raw_list:
    address.append(i.get_text().strip())
for i in link_raw_list:
    link.append(i.get(key="href"))
for i in price_raw_list:
    price.append(i.get_text()[0:6])


# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

def fillform(i):
    driver.get(gform_url)
    text_box_address = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    text_box_address.send_keys(address[i])
    text_box_price = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    text_box_price.send_keys(price[i])
    text_box_link = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    text_box_link.send_keys(link[i])

    submit = driver.find_element(by = By.XPATH , value = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()

    if i == len(address):
        driver.close()
    else:
        another = driver.find_element(by = By.LINK_TEXT , value = "Submit another response")
        another.click()


for i in range(len(address)):
    fillform(i)

