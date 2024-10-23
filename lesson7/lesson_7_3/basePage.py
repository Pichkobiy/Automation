from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
URL = ("https://www.saucedemo.com/")

class BasePage():
    def __init__(self, driver):
        self.driver = driver

class LoginPage(BasePage):
    def go_to_site(self, URL):
        self.driver.get(URL)

    def login_as(self, username):
        username_field = self.driver.find_element(By.ID, "user-name")
        username_field.send_keys("username")
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sause")
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()


