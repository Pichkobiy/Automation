from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from base import *
from selenium import webdriver
driver = webdriver.Chrome()

def test_calculator_form(chrome_browser):
    delay_input = chrome_browser.find_element(By.ID,"delay")
    delay_input.clear()
    delay_input.send_keys(45)
driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.find_element(By.XPATH, "//span[text()='8']").click()
driver.find_element(By.XPATH, "//span[text()='=']").click() 

result = WebDriverWait(driver, 47).until(EC.text_to_be_present_in_element(By.CLASS_NAME))

driver.quit()