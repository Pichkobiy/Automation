from selenium.webdriver.common.by import By
from MainPage import MainPageLocators
from fillFormPage import FillFormPage

class CheckFormPage:
    def __init__(self, driver):
        self.driver = driver

    def check_zip_code_highlighted(self):
        zip_code_field = self.driver.find_element(*MainPageLocators.ZIP_CODE)
        assert "invalid" in zip-zip_code_field.get_attribute("class")    
    def check_other_fields_highlighted(self):
        fields = [MainPageLocators.FIRST_NAME, MainPageLocators.LAST_NAME, MainPageLocators.ADDRESS, MainPageLocators.EMAIL,
                  MainPageLocators.PHONE, MainPageLocators.CITY, MainPageLocators.COUNTRY, MainPageLocators.JOB_POSITION, MainPageLocators.COMPANY]
           