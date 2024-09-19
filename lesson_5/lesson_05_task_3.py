from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

button = driver.find_element(By.CSS_SELECTOR, ".button-primary")
button.click()
button.click()
button.click()

sleep(3)

driver.quit()