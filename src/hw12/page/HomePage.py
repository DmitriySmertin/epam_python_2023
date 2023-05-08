from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.hw12.config.Url import BASE_URL
from src.hw12.page.AccountPage import AccountPage
from src.hw12.page.CartPage import CartPage

LOGIN_NAME_FIELD_LOCATOR = "loginusername"
LOGIN_PASS_FIELD_LOCATOR = "loginpassword"
LOGIN_NAVIGATION_BTN_LOCATOR = "login2"
LOGIN_BTN_LOCATOR = "//button[text()='Log in']"
CATEGORY_LOCATOR = "//a[text()='%s']"
CARD_BLOCK_LOCATOR = "//div[.//h5[text()='%s']]/preceding-sibling::a"
CARD_BLOCK_NAME_LOCATOR = "//div[.//h5[text()='%s']]/h4[@class='card-title']/a"
PRICES_ITEMS_IN_SHOP_LOCATOR = "//div[@id='tbodyid']//h5"
MONITOR_CARD_LOCATOR = "//a[text()='Apple monitor 24']"
HEADER_NAME = "//*[@class='name']"
HEADER_PRICE = "//*[@class='price-container']"
CART_NAV_LOCATOR = "cartur"


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.open(driver)
        self.login_nav_btn = driver.find_element(By.ID, LOGIN_NAVIGATION_BTN_LOCATOR)
        self.login_name_field = driver.find_element(By.ID, LOGIN_NAME_FIELD_LOCATOR)
        self.login_pass_field = driver.find_element(By.ID, LOGIN_PASS_FIELD_LOCATOR)
        self.login_btn = driver.find_element(By.XPATH, LOGIN_BTN_LOCATOR)
        self.cart_nav_btn = driver.find_element(By.ID, CART_NAV_LOCATOR)

    def open(self, driver):
        driver.get(BASE_URL)

    def openLoginWindow(self):
        self.login_nav_btn.click()

    def login(self, username, password):
        self.login_name_field.send_keys(username)
        self.login_pass_field.send_keys(password)
        self.login_btn.click()
        return AccountPage(self.driver)

    @staticmethod
    def checkPresenceLoginField(driver, element_locator):
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, element_locator)),
                                              "The login field not visible")

    def openCategory(self, category):
        self.driver.refresh()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, CATEGORY_LOCATOR % category)))
        element.click()

    def getHighPriceAndNameItemInShop(self):
        prices = list()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, MONITOR_CARD_LOCATOR)))
        prices_elements = self.driver.find_elements(By.XPATH, PRICES_ITEMS_IN_SHOP_LOCATOR)
        for i in prices_elements:
            prices.append(i.text)
        prices.sort(reverse=True)
        price_of_high_price = prices[0]
        name_of_high_price = self.driver.find_element(By.XPATH, CARD_BLOCK_NAME_LOCATOR % prices[0]).getText()
        pair_name_price = dict(name=name_of_high_price, price=price_of_high_price)
        self.driver.find_element(By.XPATH, CARD_BLOCK_LOCATOR % prices[0]).click()
        return pair_name_price

    def checkNameAndPrice(self, name, price):
        self.driver.refresh()
        assert self.driver.find_element(By.XPATH, HEADER_NAME).text == name, \
            f'The name of product: not same expected name: {name}'
        assert self.driver.find_element(By.XPATH, HEADER_PRICE).text.replace(" *includes tax", "") == price, \
            f'The price of product: not same expected price: ${price}'

    def openCart(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.ID, "cartur"))).click()
        return CartPage(self.driver)
