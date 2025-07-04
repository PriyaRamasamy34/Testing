from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/login")

wait=WebDriverWait(driver,10)
with open('data.csv','r') as file:
    reader=csv.DictReader(file)
    for row in reader:
        user_input=wait.until(EC.visibility_of_element_located((By.ID,"userName")))
        driver.execute_script("arguments[0].scrollIntoView(true)",user_input)
        ActionChains(driver).move_to_element(user_input).perform()
        user_input.clear()
        user_input.send_keys(row['username'])

        user2_input=wait.until(EC.visibility_of_element_located((By.ID,"password")))
        ActionChains(driver).move_to_element(user2_input).perform()
        user2_input.clear()
        user2_input.send_keys(row['password'])

        user3_input=wait.until(EC.visibility_of_element_located((By.ID,"login")))
        ActionChains(driver).move_to_element(user3_input).perform()
        user3_input.click()
        time.sleep(2)          
        driver.get("https://demoqa.com/login")

driver.quit()