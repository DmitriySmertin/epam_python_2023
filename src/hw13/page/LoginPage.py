from selenium.webdriver.common.by import By

from src.hw13.page import InventoryPage
from src.hw13.config.Url import *

LOGIN_USERNAME_LOCATOR = "user-name"
PASSWORD_FIELD_LOCATOR = 'password'
LOGIN_BTN_LOCATOR = "//input[@id='login-button']"


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(BASE_URL)
        self.username_field = driver.find_element(By.ID, LOGIN_USERNAME_LOCATOR)
        self.password_field = driver.find_element(By.ID, PASSWORD_FIELD_LOCATOR)
        self.login_btn = driver.find_element(By.XPATH, LOGIN_BTN_LOCATOR)

    def login(self, user_name, password):
        self.username_field.send_keys(user_name)
        self.password_field.send_keys(password)
        self.login_btn.click()
        return InventoryPage

