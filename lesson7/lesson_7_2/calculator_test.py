from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from slowCalculatorPage import SlowCalculatorPage
from formCalculator import FormCalculator
import config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_slow_calculator(browser):
    calculator_page = SlowCalculatorPage(browser)
    calculator_page.open()
    calculator_page.set_delay("45")
    calculator_page.click("7")
    calculator_page.click("+")
    calculator_page.click("8")
    calculator_page.click("=")


    WebDriverWait(browser, 45).until(EC.text_to_be_present_in_element(By.CLASS_NAME))

    result = calculator_page.get_result()
    assert result == "15"
