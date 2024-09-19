from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/entry_ad")

close_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.CLASS_NAME, 'modal-footer')).find_element(By.TAG_NAME, 'a')
close_button.click()
driver.quit()