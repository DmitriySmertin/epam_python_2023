from selenium.webdriver.common.by import By

LIST_DESCRIPTION_ITEM_LOCATOR = "//tr[@class='success']//td"


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def getDescriptionsOfItem(self):
        return self.driver.find_elements(By.XPATH, LIST_DESCRIPTION_ITEM_LOCATOR)

    @staticmethod
    def getPrice(list: list):
        return list[2].text

    @staticmethod
    def getName(list: list):
        return list[1].text

    def checkNameAndPrice(self, name, price):
        listDescr = self.getDescriptionsOfItem()
        actualPrice = "$" + self.getPrice(listDescr)
        actualName = self.getName(listDescr)
        assert actualName == name
        assert actualPrice == price
