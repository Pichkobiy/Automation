import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from basePage import BasePage
from loginPage import LoginPage
from cartPage import CartPage
import configure

def shopping_test(browser):
    login_page = LoginPage(browser)
    login_page.go_to_site(URL="https://www.saucedemo.com/")
    login_page.login_as("standart_user")
    cart_page = CartPage(browser)
    cart_page.add_to_cart("Sauce Labs Backpack")
    cart_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    cart_page.add_to_cart("Sauce Labs Onesie")
    cart_page.go_to_cart()
    cart_page.proceed_to_checkout()

    cart_page.fill_checkout_form("Irine", "Pichkobiy", "186870")
    total_cost = cart_page.get_total_cost()
    assert total_cost == "$58.29"