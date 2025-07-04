from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
simple_alert=driver.switch_to.alert
print(simple_alert.text)
time.sleep(2)
simple_alert.accept()

driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
confirm_alert=driver.switch_to.alert
print(confirm_alert.text)
time.sleep(2)
confirm_alert.accept()

driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
prompt_alert=driver.switch_to.alert
print(prompt_alert.text)
time.sleep(2)
prompt_alert.send_keys("Hi I'm Priya")
time.sleep(2)
prompt_alert.accept()

print("All alerts handled successfully")
time.sleep(2)
driver.quit()
