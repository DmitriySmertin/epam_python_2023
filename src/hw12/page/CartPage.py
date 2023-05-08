from selenium.webdriver.common.by import By

LIST_DESCRIPTION_ITEM_LOCATOR = "//tr[@class='success']//td"


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def getDescriptionsOfItem(self):
        return self.driver.find_elements(By.XPATH, LIST_DESCRIPTION_ITEM_LOCATOR)

    def checkNameAndPrice(self, name, price):
        listDescr = self.getDescriptionsOfItem()
        actualName = listDescr[1]
        actualPrice = "$" + listDescr[2]
        assert actualName == name
        assert actualPrice == price
