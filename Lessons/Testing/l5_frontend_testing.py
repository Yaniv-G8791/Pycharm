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
a=123123

driver.get('http://127.0.0.1:5001/users/')
driver.find_element(By.XPATH , "//button[@class='Btn'] [@id='Get'] ").click()
driver.implicitly_wait(2)
driver.find_element(By.XPATH , "//textarea[@name='Get'] [@id='UserInput'] ").send_keys(a)
time.sleep(10)
driver.find_element(By.XPATH , "//input[@class='button'] [@type='button'] ").click()
time.sleep(5)