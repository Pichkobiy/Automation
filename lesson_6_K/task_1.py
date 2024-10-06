from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from base import *
from time import sleep

def test_data_tipes_form(chrome_browser):
    chrome_browser.get(URL)
    form_data = {
        "first_name": first_name,
        "last_name": last_name,
        "address": address,
        "e_mail": email,
        "phone": phone,
        "zip_code": zipcode,
        "city": city,
        "country": country,
        "job_position": job_position,
        "company": company

    }

for field_name, value in form_data.items():
    chrome_browser.find_element(By.NAME, field_name).send_keys(value)

WebDriverWait(chrome_browser, 40, 0.1).until(
    EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()
sleep(3)

field_classes = {
    "zip_code": "danger",
    "first_name": "success",
    "last_name": "success",
    "address": "success",
    "e_mail": "success",
    "phone": "success",
    "city": "success",
    "country": "success",
    "job_position": "success",
    "company": "success"
}

for field_id, class_name in field_classes.items():
    assert class_name in chrome_browser.find_element(
        By.ID, field_id).get_attribute("class")
    
    
