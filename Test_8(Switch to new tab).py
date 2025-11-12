from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")

main_window = driver.current_window_handle

driver.find_element(By.ID, "tabButton").click()
time.sleep(2)

all_windows = driver.window_handles

for handle in all_windows:
    if handle != main_window:
        driver.switch_to.window(handle)
        break

print("New tab title:", driver.title)

driver.close()

driver.switch_to.window(main_window)

print("Back to main window:", driver.title)

driver.quit()
