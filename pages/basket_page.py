from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_be_message_cart_empty(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_CART_TITlE), 'title is not present'
        empty_cart_text = self.find_element_presented(BasePageLocators.EMPTY_CART_TITlE).text
        assert  'Your basket is empty.' in empty_cart_text, 'Cart is not empty'

    def should_be_no_items_in_cart(self):
        assert self.is_not_element_present(*BasePageLocators.ITEM_ROW_CART), "item is present, but shouldn't"