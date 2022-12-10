from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import  Service
import time
def pause():
    import os
    os.system("pause")


driver = webdriver.Chrome(service=Service("C:/Programming/Selenium/chromedriver"))

driver.maximize_window()

wait = WebDriverWait(driver,40)

driver.get('https://translate.google.com/')

driver.find_element(By.XPATH , "//span[@class='VfPpkd-YVzG2b'] [@jsname='ksKsZd'] ").click()
time.sleep(2)
a=driver.find_element(By.LINK_TEXT, 'fr')
time.sleep(2)
a.click()
b='hombre','pequena','pescado','emparedado','bano','caballeo','holla'
for d in b:
    time.sleep(1)
    btn=driver.find_element(By.CLASS_NAME,"er8xn").send_keys(d)

    driver.implicitly_wait(4)
    t=driver.find_element(By.CLASS_NAME,"ryNqvb").text
    print("the translated word for "+str(d)+" is "+str(t))

    driver.find_element(By.CLASS_NAME,"er8xn").clear()

print(driver.current_url)
print(driver.title)

for d in driver.window_handles:
    print(str(d))


