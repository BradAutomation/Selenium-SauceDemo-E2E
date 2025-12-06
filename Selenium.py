from selenium import webdriver
import time

from selenium.webdriver.common.by import By

print( "test case started...")

driver = webdriver.Chrome()

driver.delete_all_cookies()

driver.maximize_window()

driver.get("https://www.gmail.com")
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "#identifierId").send_keys("skychrist.yb@gmail.com")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "#identifierNext > div > button > span").click()
time.sleep(3)
#driver.find_element(By.CSS_SELECTOR, "#password").send_keys("")
driver.close()

print("sample test case successfully completed...")

