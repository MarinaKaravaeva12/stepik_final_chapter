from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

# class MainPageLocators():


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR,'#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR,'#register_form')

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.XPATH,'//form[@id="add_to_basket_form"]/button')
    SUCCESS_TEXT_NAME = (By.XPATH,'//div[@id="messages"]/div/div')
    PRODUCT_NAME = (By.XPATH,'//div[contains(@class,"product_main")]/h1')
    PRODUCT_PRICE = (By.XPATH,'//div[contains(@class,"product_main")]/p[contains(@class,"price_color")]')
    SUCCESS_TEXT_PRICE = (By.XPATH,'//div[@id="messages"]/div[3]//strong')

