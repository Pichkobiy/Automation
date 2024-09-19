from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
for i in range(5):
    add_btn = driver.find_element(By.CSS_SELECTOR("button[onclick^='addElement()']"))
    add_btn.click()
    sleep(5)

delete_buttons = driver.find_element(By.CSS_SELECTOR("button[onclick^='deleteElement()']"))
print("Размер списка кнопок Delete:", len(delete_buttons))


driver.quit()