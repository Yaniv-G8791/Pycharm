import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import  Service
import time


def test_PostUser(userid="-1", username="test"):
    a = requests.post('http://127.0.0.1:5000/users/' + str(userid), json={'user_name': username})
    return a

def test_GetUser(userid="-1"):
    a = requests.get('http://127.0.0.1:5000/users/' + str(userid))
    return a

uid=input("enter user id: ")
uname=input("enter user name: ")

p = test_PostUser(uid,uname)
p = p.json()
p1 = p["Status"]
p2 = p["Code"]
print(str(p1)+" code: "+str(p2))
try:
    driver = webdriver.Chrome(service=Service("C:/Programming/Selenium/chromedriver"))

    driver.maximize_window()

    wait = WebDriverWait(driver,40)

    driver.get('http://127.0.0.1:5001/users/')
    driver.find_element(By.XPATH , "//button[@class='Btn'] [@id='Get'] ").click()
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH , "//textarea[@name='Get'] [@id='UserInput'] ").send_keys(uid)
    time.sleep(5)
    driver.find_element(By.XPATH , "//input[@class='button'] [@type='button'] ").click()
    time.sleep(5)
    d=driver.find_element(By.ID,"user")
    print(d.text)
except:
    raise Exception("test failed")
