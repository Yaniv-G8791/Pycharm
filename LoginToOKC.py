from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
def pause():
    import os
    os.system("pause")


driver = webdriver.ChromiumEdge()
driver.maximize_window()

wait = WebDriverWait(driver,40)

driver.get('https://www.okcupid.com/login')

driver.execute_script('arguments[0].click();',wait.until(EC.element_to_be_clickable((By.ID, 'username'))))
wait.until(EC.element_to_be_clickable((By.ID, 'username'))).send_keys("Ganyaniv@gmail.com")

driver.execute_script('arguments[0].click();',wait.until(EC.element_to_be_clickable((By.ID, 'username'))))
wait.until(EC.element_to_be_clickable((By.ID, 'password'))).send_keys("LevelUp43!")

# Find login button
login_button = driver.find_elements("login-actions-button")
# Click login
login_button.click()
time.sleep(1)

pause()
time.sleep(5)
listWEB=driver.find_element_by_xpath("//div[@class='code-inputs-digits']");
print(list)
time.sleep(10)