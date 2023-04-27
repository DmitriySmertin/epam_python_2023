import pytest
from src.hw13.page.LoginPage import LoginPage
from src.hw13.config.Url import *
from test.hw13.data.Data import USER_NAME, USER_PASS


@pytest.mark.usefixtures("init_driver")
@pytest.mark.login
class TestLoginPositive:

    def test_login_positive(self):
        login_page = LoginPage(self.driver)
        inventory_page = login_page.login(USER_NAME, USER_PASS)
        cur_url = inventory_page.get_current_url(self.driver)
        assert cur_url is INVENTORY_URL
