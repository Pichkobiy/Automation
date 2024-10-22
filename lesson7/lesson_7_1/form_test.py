import pytest
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from MainPage import MainPageLocators
from fillFormPage import FillFormPage
from checkFormPage import CheckFormPage


class TestFormSubmission(unittest.TestCase):
    def setUp(self):
        fill_form = FillFormPage(self.driver)
        check_form = CheckFormPage(self.driver)

        fill_form.fill_form("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "Москва", "Россия", "QA", "SkyPro")
        
        check_form.check_zip_code_highlighted()
        check_form.check_other_fields_highlighted()
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()            
      