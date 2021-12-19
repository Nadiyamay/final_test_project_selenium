from .base_page import BasePage
from .login_page import LoginPage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
#указали класс-предок в скобках, а текущий класс-наследник
   def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)