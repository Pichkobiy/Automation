from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from slowCalculatorPage import SlowCalculatorPage

class FormCalculator:
    def __init__(self, driver):
        self.driver()

    def open(self):
        self.driver.get(self.URL)  

    def set_delay(self, value):
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(value)
        
    def click_button(self, button_text):
        button = self.driver.find_element(*self.buttons[button_text])
        button.click()

    def get_result(self):
        return self.driver.find_element(*self.result).text    