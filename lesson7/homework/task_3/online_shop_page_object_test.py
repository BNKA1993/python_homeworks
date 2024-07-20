from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.MainPage import MainPage
from pages.ResultPage import ResultPage
from pages.AuthorizationPage import AuthorizationPage
from pages.InformationPage import InformationPage
from pages.CartPage import CartPage


def test_result():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    authorization_page = AuthorizationPage(browser)

    authorization_page.username("standard_user")
    authorization_page.password("secret_sauce")
    authorization_page.click_login()

    main_page = MainPage(browser)
    main_page.add_to_cart()

    cart_page = CartPage(browser)
    cart_page.get_to_cart()
    cart_page.get_to_checkout()

    information_page = InformationPage(browser)
    information_page.add_first_name("Виктория")
    information_page.add_last_name("Ситникова")
    information_page.add_zip_code("0000")
    information_page.click_button()

    result_page = ResultPage(browser)
    result_amount = result_page.text_result()

    browser.quit()

    assert result_amount == "Total: $58.29"


