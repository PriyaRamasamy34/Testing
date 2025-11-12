from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://dodo.quantumnique.tech/")
driver.maximize_window()

menu_links={
    "ASSESSMENTS":"Assessments",
    "COURSES":"Courses",
    "CODE":"Code",
    "PRACTICE":"Practice",
    "LSRW":"LSRW",
    "BLOGS":"Blogs",
    "DASHBOARD":"Dashboard"
}
for link_text,expected_url_part in menu_links.items():
    try:
        menu_link=driver.find_element(By.LINK_TEXT,link_text)
        menu_link.click()
        time.sleep(2)
        current_url=driver.current_url

        if expected_url_part in current_url:
            print("Redirect correctly")
        else:
            print("Doesn't redirect correctly")

        driver.get("https://dodo.quantumnique.tech/")
        time.sleep(2)
    except Exception as e:
        print("Error navigating to")

driver.quit()

