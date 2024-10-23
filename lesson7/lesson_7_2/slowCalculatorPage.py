from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



class SlowCalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    delay_input = (By.CSS_SELECTOR, '#delay')
    buttons = {
        "7": (By.CSS_SELECTOR, '#seven'),
        "+": (By.CSS_SELECTOR, '#add'),
        "8": (By.CSS_SELECTOR, '#eight'),
        "=": (By.CSS_SELECTOR, '#equal') 
    }
    result = (By.CSS_SELECTOR, '#display')

