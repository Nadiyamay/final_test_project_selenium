from .base_page import BasePage
from .login_page import LoginPage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):

    def should_be_empty_basket(self):
        self.should_not_be_any_products_in_basket()
        self.should_be_message_about_empty_one()
 
    def should_not_be_any_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TOTAL),\
            "Total amount is presented, basket in not empty!"

    def should_be_message_about_empty_one(self):
        basket_massage = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE)
        assert str(basket_massage.text.split(".")[0]) == "Your basket is empty", "There in not massage about empty basket"

