from selenium.common import TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ADD_TO_CART_BTN_LOCATOR = "//a[text()='Add to cart']"


class ItemCardPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_btn = driver.find_element(By.XPATH, ADD_TO_CART_BTN_LOCATOR)

    def add_to_cart(self):
        self.add_to_cart_btn.click()
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            print("no alert")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//li[@class='nav-item']")))

