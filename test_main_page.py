from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
#импортируем класс описывающий главную страницу

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser,link)#передаем в конструктор экземплятр браузера и url
    page.open() #открываем страницу
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_should_see_login_and_register_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser,link)
    page.open()
    page.go_to_login_page()
    regist_page = LoginPage(browser,browser.current_url)
    regist_page.should_be_login_page()
   
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = BasePage(browser,link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser,link)
    page.should_be_empty_basket()
