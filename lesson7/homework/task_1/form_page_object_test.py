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


def test_red_element():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPage(browser)

    main_page.first_name("Иван")
    main_page.last_name("Петров")
    main_page.address("Ленина, 55-3")
    main_page.email("test@skypro.com")
    main_page.phone("+7985899998787")
    main_page.zip_code("")
    main_page.city("Москва")
    main_page.country("Россия")
    main_page.job_position("QA")
    main_page.company("SkyPro")
    main_page.send_form()

    result_page = ResultPage(browser)
    to_be = result_page.empty_zip_result_is_red()

    as_is = 1

    assert as_is == to_be

    browser.quit()


def test_green_elements():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPage(browser)

    main_page.first_name("Иван")
    main_page.last_name("Петров")
    main_page.address("Ленина, 55-3")
    main_page.email("test@skypro.com")
    main_page.phone("+7985899998787")
    main_page.zip_code("")
    main_page.city("Москва")
    main_page.country("Россия")
    main_page.job_position("QA")
    main_page.company("SkyPro")
    main_page.send_form()

    result_page = ResultPage(browser)
    classes = result_page.other_elements_result_is_green()

    assert 'alert-success' in classes
