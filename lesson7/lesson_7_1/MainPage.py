from selenium.webdriver.common.by import By



class MainPageLocators:
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    ADDRESS = (By.ID, 'address')
    EMAIL = (By.ID, 'email')
    PHONE = (By.ID, 'phone')
    ZIP_CODE = (By.ID, 'zip-code')
    CITY = (By.ID, 'city')
    COUNTRY = (By.ID, 'country')
    JOB_POSITION = (By.ID, 'job-position')
    COMPANY = (By.ID, 'company')
    SUBMIT_BUTTON = (By.ID, 'submit')

fields = ()