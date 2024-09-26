from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.ID, "text")
input_field.send_keys("SkyPro")
button = driver.find_element(By.ID, "myButton")
button.click()
waiter = WebDriverWait(driver, 30)

button_text = driver.find_element(By.ID, "button1").text
print(button_text)
driver.quit()