from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")
input_field = driver.find_element(By.XPATH, "//input[@type='number']")

input_field.send_keys("1000")
time.sleep(3)
input_field.clear()
time.sleep(3)
input_field.send_keys("999")

driver.quit()