from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com")
print("Title1:", driver.title)

driver.get("https://www.wikipedia.org/")
print("Title2:", driver.title)

driver.back()
print("Back to:", driver.title)

driver.forward()
print("Forward:", driver.title)

driver.refresh()
print("Page refreshed")

time.sleep(2)
driver.quit()
