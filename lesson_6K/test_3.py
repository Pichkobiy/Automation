from selenium.webdriver.common.by import By
from base import *
from selenium import webdriver

driver = webdriver.Chrome()

def test_shop_form(driver):
    driver.get(URL_2)
    driver.find_element(By.ID, "user-name").send_keys("problem_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.ID, "shopping_cart_container").click()
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Irine") 
    driver.find_element(By.ID, "last-name").send_keys("Pichkobiy")
    driver.find_element(By.ID, "postal-code").send_keys("")
    driver.find_element(By.ID, "continue").click()
    total_price = driver.find_element(By.CLASS_NAME, 'summary_total_label')
    total = total_price

expected_total = "58.29"
assert total == expected_total
print("Итого: ", total)
driver.quit()