from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()

driver.get("https://dodo.quantumnique.tech/login")

username=driver.find_element(By.ID,"Email / Hallticket Number")
username.send_keys("717822L336")


password=driver.find_element(By.ID, "Password is required")
password.send_keys("Student@123")

submit_button=driver.find_element(By.TAG_NAME,"Sign in")
submit_button.click()
time.sleep(5)


msg=driver.find_element(By.TAG_NAME,'h4').text
print("Login successful")


driver.quit()
