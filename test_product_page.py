
from pages.product_page import ProductPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.locators import MainPageLocators
from pages.locators import LoginPageLocators
from pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6", 
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser,link):
    basket = ProductPage(browser,link)
    basket.open()
    basket.should_add_product_to_basket_succesfully()
 
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook__207/?promo=offer0"
    page = ProductPage(browser,link)
    page.open()
    page.can_add_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED), \
       "Success message is presented, but should not be"

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook__207/?promo=offer0"
    page= ProductPage(browser,link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED), \
       "Success message is presented, but should not be"

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook__207/?promo=offer0"
    page = ProductPage(browser,link)
    page.open()
    page.can_add_to_basket()
    assert page.is_disappeared(*ProductPageLocators.PRODUCT_ADDED),\
        "Success message is presented, but should not be"