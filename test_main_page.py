from pages.main_page import MainPage
from pages.login_page import LoginPage
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
    regist_page = LoginPage(browser,link)
    regist_page.should_be_login_page()
    