from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def check_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
        "Row with product is presented in basket, but should not be"

    def check_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT),"Basket is empty text is not presented"