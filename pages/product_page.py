from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
import time



class ProductPage(BasePage):
#указали класс-предок в скобках, а текущий класс-наследник
    def should_add_product_to_basket_succesfully(self):
        self.can_add_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_visible_in_mini_basket()
        self.should_be_book_name_in_confirmation()

    def can_add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()
        
    def should_be_visible_in_mini_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        time.sleep(6)
        basket_amount = self.browser.find_element(*ProductPageLocators.BASKET_AMOUNT)
        assert str(product_price.text) in str(basket_amount.text), "Basket amount is incorrect"

    def should_be_book_name_in_confirmation(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_added = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED)
        assert str(product_name.text) == str(product_added.text), "The book has not been added"

