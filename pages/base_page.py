import math

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def open(self):
        return self.browser.get(self.url)

    def is_element_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, method, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((method, locator))
            )
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, method, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((method, locator))
            )
        except TimeoutException:
            return False
        return True

    def find_element_clickable(self, locator):
        element = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locator)
        )
        return element

    def find_element_presented(self, locator):
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(locator)
        )
        return element

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_cart(self):
        assert self.is_element_present(*BasePageLocators.CART_BUTTON)
        cart_button = self.browser.find_element(*BasePageLocators.CART_BUTTON)
        cart_button.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
