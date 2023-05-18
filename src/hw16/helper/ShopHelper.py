from robot.libraries.BuiltIn import BuiltIn


class ShopHelper:
    def __init__(self):
        self.selLib = BuiltIn().get_library_instance("SeleniumLibrary")

    def get_high_price_and_name_item_in_shop(self):
        prices = list()
        self.selLib.wait_until_element_is_visible("xpath://a[text()='Apple monitor 24']")
        prices_elements = self.selLib.find_elements("xpath://div[@id='tbodyid']//h5")

        for price_element in prices_elements:
            prices.append(price_element.text)
        prices.sort(reverse=True)
        price_of_high_price = prices[0]

        name_of_high_price = self.selLib.find_element("xpath://div[.//h5[text()='%s']]/h4[@class='card-title']/a"
                                                      % prices[0]).text
        pair_name_price = dict(name=name_of_high_price, price=price_of_high_price)
        return pair_name_price

    def open_high_price_card(self, pair: dict):
        self.selLib.find_element("xpath://div[.//h5[text()='%s']]/preceding-sibling::a" % pair.get("price")).click()
