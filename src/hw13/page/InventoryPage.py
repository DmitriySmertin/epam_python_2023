from src.hw13.config.Url import *


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url
