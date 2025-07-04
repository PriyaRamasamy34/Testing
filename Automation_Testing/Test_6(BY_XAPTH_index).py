from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")


username=driver.find_element(By.ID,"username")
username.send_keys("student")

pwd=""
password=driver.find_element(By.ID,"password")
password.send_keys(pwd)

submit_button=driver.find_element(By.ID,"submit")
submit_button.click()
time.sleep(2)

try:
    msg=driver.find_element(By.TAG_NAME,'h1').text

    if "Logged In Successfully" in msg:
        print("Login successful")
    else:
        print("Login Failed")
except:
    print("Login failed no other message found")


if pwd.strip()=="":
    print("Please enter a valid password")
    
driver.quit()

