from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from MainPage import MainPageLocators

class FillFormPage:
    def __init__(self, driver):
        self.driver = driver

def fill_form(self, first_name, last_name, adress, email, phone, zip_code, city, job_position, company):
    self.driver.find_element(*MainPageLocators.FIRST_NAME).send_keys(first_name)
    self.driver.find_element(*MainPageLocators.LAST_NAME).send_keys(last_name)
    self.driver.find_element(*MainPageLocators.ADDRESS).send_keys(address)
    self.driver.find_element(*MainPageLocators.EMAIL).send_keys(email)
    self.driver.find_element(*MainPageLocators.PHONE).send_keys(phone)
    self.driver.find_element(*MainPageLocators.CITY).send_keys(city)
    self.driver.find_element(*MainPageLocators.COUNTRY).send_keys(country)
    self.driver.find_element(*MainPageLocators.ZIP_CODE).send_keys(zip_code)
    self.driver.find_element(*MainPageLocators.JOB_POSITION).send_keys(job_position)
    self.driver.find_element(*MainPageLocators.COMPANY).send_keys(company)

