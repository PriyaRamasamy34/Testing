from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

wait = WebDriverWait(driver, 10)

firstname = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@type='text'])[1]")))
firstname.send_keys("Priya")
time.sleep(2)

second_name = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@type='text'])[2]")))
second_name.send_keys("R")
time.sleep(2)

driver.quit()
