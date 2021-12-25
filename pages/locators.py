from selenium.webdriver.common.by import By

class BasePageLocators():
    BASKET_LINK = (By.CSS_SELECTOR,".btn-group")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_EMPTY_MESSAGE = (By.TAG_NAME,"p")
    BASKET_TOTAL = (By.CSS_SELECTOR,"total")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REGISTER_INPUT = (By.CSS_SELECTOR,"#id_registration-email")
    PASSWORD_REGISTER_INPUT = (By.CSS_SELECTOR,"#id_registration-password1")
    PASSWORD_REPEAT_REGISTER_INPUT = (By.CSS_SELECTOR,"#id_registration-password2")
    SUBMIT_REGISTER = (By.XPATH,"//button[@name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_AMOUNT = (By.CSS_SELECTOR, ".pull-right.hidden-xs")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_ADDED = (By.CSS_SELECTOR,".alertinner>strong")