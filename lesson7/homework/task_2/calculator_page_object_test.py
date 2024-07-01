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


def test_result():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPage(browser)

    main_page.delay("45")
    main_page.click_button("7")
    main_page.click_button("+")
    main_page.click_button("8")
    main_page.click_button("=")

    result_page = ResultPage(browser)
    result = result_page.display_time_result()

    assert 15 == result, f"Expected 15, but got {result}"

    browser.quit()
