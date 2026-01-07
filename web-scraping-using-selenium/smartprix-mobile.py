from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()     # auto-manages correct driver

driver.get("https://www.smartprix.com/mobiles")

time.sleep(2)

old_height = driver.execute_script("return document.body.scrollHeight")
counter = 1


while True:

    driver.find_element(By.XPATH, '//*[@id="app"]/main/div[1]/div[3]/div[3]').click()
    time.sleep(1)

    new_height = driver.execute_script("return document.body.scrollHeight")
    print(counter)
    counter += 1
    print(old_height)
    print(new_height)

    if new_height == old_height:
        break

    old_height = new_height

html = driver.page_source

with open('smartprix.html', 'w', encoding='utf-8') as f:
    f.write(html)
