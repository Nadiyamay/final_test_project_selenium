from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
import time



class ProductPage(BasePage):
#указали класс-предок в скобках, а текущий класс-наследник
    def should_add_product_to_basket_succesfully_guest(self):
        self.can_add_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_visible_in_mini_basket()
        self.should_be_book_name_in_confirmation()

    def should_add_product_to_basket_succesfully_user(self):
        self.can_add_to_basket()
        self.should_be_visible_in_mini_basket()
        self.should_be_book_name_in_confirmation()    

    def can_add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def message_should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDED),\
            "Success message is presented, but should not be"
       
    def success_message_shouldnt_be_presented(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED), \
           "Success message is presented, but should not be"

        
    def should_be_visible_in_mini_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        time.sleep(6)
        basket_amount = self.browser.find_element(*ProductPageLocators.BASKET_AMOUNT)
        assert str(product_price.text) in str(basket_amount.text), "Basket amount is incorrect"

    def should_be_book_name_in_confirmation(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_added = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED)
        assert str(product_name.text) == str(product_added.text), "The book has not been added"
    
    def shouldnt_be_success_message_without_added_product(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED), \
            "Success message is presented, but should not be"

