##init driver. Before start tests need to choose file .env "BROWSER"
import pytest
import os
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options as FfOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture(scope="class")
def init_driver(request):
    load_dotenv()
    supported_browser = ["chrome", "firefox", "safari", "headlesschrome", "headlessfirefox"]
    browser = os.environ.setdefault("BROWSER", os.getenv("BROWSER"))
    if not browser:
        raise Exception("Not selected 'BROWSER'.")
    if browser not in supported_browser:
        raise Exception("Browser not supported")

    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "headlesschrome":
        ch_options = ChOptions()
        ch_options.add_argument('--disable-gpu')
        ch_options.add_argument('--no-sandbox')
        ch_options.add_argument('--headless')
        driver = webdriver.Chrome(options=ch_options)
    elif browser == "headlessfirefox":
        ff_options = FfOptions()
        ff_options.add_argument('--disable-gpu')
        ff_options.add_argument('--no-sandbox')
        ff_options.add_argument('--headless')
        driver = webdriver.Firefox(options=ff_options)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()
