from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.hw12.data.Data import USER_NAME

LOGOUT_BTN_LOCATOR = "//a[text()='Log out']"
WELCOME_MSG_LOCATOR = "nameofuser"


class AccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.logout_btn = driver.find_element(By.XPATH, LOGOUT_BTN_LOCATOR)

    @staticmethod
    def checkPresenceLogOutBtn(driver):
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, LOGOUT_BTN_LOCATOR)))

    def checkWelcomeMessage(self):
        assert self.driver.find_element(By.ID, WELCOME_MSG_LOCATOR).text == "Welcome " + USER_NAME
