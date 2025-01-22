from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BUTTON = (By.XPATH, '//span/a[@class="btn btn-default"]')
    EMPTY_CART_TITlE = (By.XPATH, '//div[@id="content_inner"]/p')
    ITEM_ROW_CART = (By.ID, '#basket_formset')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL = (By.ID, 'id_registration-email')
    REGISTRATION_PASSWORD = (By.ID, 'id_registration-password1')
    REGISTRATION_CONFIRM_PASSWORD = (By.ID, 'id_registration-password2')
    REGISTRATION_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.XPATH, '//form[@id="add_to_basket_form"]/button')
    SUCCESS_TEXT_NAME = (By.XPATH, '//div[@id="messages"]/div/div')
    PRODUCT_NAME = (By.XPATH, '//div[contains(@class,"product_main")]/h1')
    PRODUCT_PRICE = (By.XPATH, '//div[contains(@class,"product_main")]/p[contains(@class,"price_color")]')
    SUCCESS_TEXT_PRICE = (By.XPATH, '//div[@id="messages"]/div[3]//strong')
