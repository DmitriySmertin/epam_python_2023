import pytest

from src.hw12.data.Data import USER_NAME, PASSWORD, TEST_CATEGORY, TEST_ITEM
from src.hw12.page.HomePage import HomePage, LOGIN_NAME_FIELD_LOCATOR, LOGIN_PASS_FIELD_LOCATOR
from src.hw12.page.ItemCardPage import ItemCardPage


@pytest.mark.usefixtures("init_driver")
@pytest.mark.login
class TestLogin:

    @pytest.fixture
    def loginSetUp(self):
        home_page = HomePage(self.driver)
        home_page.openLoginWindow()
        home_page.login(USER_NAME, PASSWORD)
        return home_page

    def testLogin(self):
        home_page = HomePage(self.driver)
        # Step-1
        home_page.openLoginWindow()
        home_page.checkPresenceLoginField(self.driver, LOGIN_NAME_FIELD_LOCATOR)
        home_page.checkPresenceLoginField(self.driver, LOGIN_PASS_FIELD_LOCATOR)
        # Step-2
        account_page = home_page.login(USER_NAME, PASSWORD)
        account_page.checkPresenceLogOutBtn(self.driver)
        account_page.checkWelcomeMessage()

    def testAddedInCart(self, loginSetUp):
        home_page = loginSetUp
        # Step-1
        home_page.openCategory(TEST_CATEGORY)
        # Step-2
        high_price = home_page.getHighPriceItemInShop()
        home_page.checkNameAndPrice(TEST_ITEM, high_price)
        # Step-3
        card_page = ItemCardPage(self.driver)
        card_page.add_to_cart()
        # Step-4
        cart_page = home_page.openCart()
        cart_page.checkNameAndPrice(TEST_ITEM, high_price)
