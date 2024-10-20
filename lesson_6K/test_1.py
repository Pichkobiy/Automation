from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from base import *
import time

driver = webdriver.Chrome()

def test_data_tipes_form(driver):
    driver.get(URL)
    form_data = {
        "first-name": first_name,
        "last-name": last_name,
        "address": address,
        "e-mail": email,
        "phone": phone,
        "zip-code": zipcode,
        "city": city,
        "country": country,
        "job-position": job_position,
        "company": company

    }



    WebDriverWait(driver, 40, 0.1).until(EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()

    assert "danger" in driver.find_element(By.ID, "zip-code").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "first-name").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "last-name").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "address").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "e-mail").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "phone").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "city").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "country").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "job-position").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "company").get_attribute("class")

    driver.quit()