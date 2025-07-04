from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/droppable/")

iframe = driver.find_element(By.CSS_SELECTOR, ".demo-frame")
driver.switch_to.frame(iframe)

source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()

time.sleep(2)

dropped_text = target.text
if dropped_text== "Dropped!":
    print("Drag and drop successful")
else:
    print("Drag and drop not successful")

driver.switch_to.default_content()


driver.quit()
