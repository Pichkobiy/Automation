from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait = WebDriverWait(driver, 20)
images = wait.until(EC.visibility_of_all_elements_located(By.TAG_NAME, 'img'))
third_image_src = images[2].get_attribute('src')
print(third_image_src)
driver.quit()