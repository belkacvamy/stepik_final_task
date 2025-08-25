from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_IN_BASKET), \
        "Success message is presented, but should not be"

    def add_to_basket(self):
        self.add_to_basket_btn_exists()
        add_to_basket_btn=self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def success_message_is_displayed(self):
        product_name=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_basket=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert product_name==product_name_in_basket, f"different products names in product: {product_name} and basket:{product_name_in_basket}"

    def basket_sum_same_as_product(self):
        product_price=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_basket=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
        assert product_price==product_price_in_basket, f"different products prices in product:{product_price} and basket:{product_price_in_basket}"

    def message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_IN_BASKET), \
        "Message is presented, but should disappear"

    def product_name_exists(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
        "Product name is not presented"

    def add_to_basket_btn_exists(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), \
        "Button for adding an item to basket is not presented!"