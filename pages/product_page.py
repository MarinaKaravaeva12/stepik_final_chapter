from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "Add to card button is missing"
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def take_product_name(self):
        product_name = self.find_element_clickable(ProductPageLocators.PRODUCT_NAME).text
        print(product_name)
        return product_name

    def take_product_price(self):
        product_price = self.find_element_clickable(ProductPageLocators.PRODUCT_PRICE).text
        print(product_price)
        return product_price

    def should_be_success_message_correct_title(self, product_name):
        success_message = self.find_element_presented(ProductPageLocators.SUCCESS_TEXT_NAME)
        print(success_message.text)
        assert f"{product_name} has been added to your basket." in success_message.text, 'Incorrect message'

    def should_be_success_message_correct_price(self, product_price):
        success_message = self.find_element_presented(ProductPageLocators.SUCCESS_TEXT_PRICE)
        print(success_message.text)
        assert product_price == success_message.text, 'Incorrect price'

    def should_not_be_successful_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_TEXT_NAME), 'Success message is presented, but should not be'

    def message_should_disappear(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_TEXT_NAME), 'Success message is not disappearing, but should be'
