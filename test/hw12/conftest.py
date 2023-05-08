import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from src.hw12.data.Data import USER_NAME, PASSWORD
from src.hw12.page.HomePage import HomePage


@pytest.fixture(scope="class")
def init_driver(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope="function")
def loginSetUp(request):
    home_page = HomePage(request.cls.driver)
    home_page.openLoginWindow()
    home_page.login(USER_NAME, PASSWORD)
    return home_page
