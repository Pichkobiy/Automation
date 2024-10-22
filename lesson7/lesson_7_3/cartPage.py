from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from basePage import BasePage
from loginPage import LoginPage


class CartPage(BasePage):
    def add_to_cart(self, product_name):
        add_to_cart_button = self.driver.find_element(By.XPATH, f"//div[text()='{product_name}]/following-sibling: :button")
        add_to_cart_button.click()

    def go_to_cart(self):
        shopping_cart_link = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        shopping_cart_link.click()

    def proceed_to_checkout(self):
        checkout_button = self.driver.find_element(By.CLASS_NAME, "checkout_button")
        checkout_button.click()

    def fill_checkout_form(self, first_name, last_name, postal_code):
        first_name_field = self.driver.find_element(By.ID, "first-name")
        first_name_field.send_keys(first_name)
        last_name_field = self.driver.find_element(By.ID, "last-name") 
        last_name_field.send_keys(last_name) 
        postal_code_field = self.driver.find_element(By.ID, "postal-code")
        postal_code_field.send_keys(postal_code)
        continue_button = self.driver.find_element(By.CLASS_NAME, "cart-button")
        continue_button.click()

    def get_total_cost(self):
        total_cost = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        return total_cost          

