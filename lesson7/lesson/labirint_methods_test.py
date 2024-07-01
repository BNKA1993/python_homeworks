from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from selenium.webdriver.support import expected_conditions as EC

cookie = {"name": "cookie_policy", "value": "1"}

browser = webdriver.Chrome()


def open_labirint():
    # Перейти на сайт «Лабиринта»
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)


def search(term):
    # Найти все книги по слову Python
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


def add_books():
    # Добавить все книги в корзину и посчитать
    by_buttons = browser.find_elements(By.CSS_SELECTOR, "a.btn-tocart.buy-link")

    counter = 0
    for btn in by_buttons:
        btn.click()
        counter += 1
    return counter


def go_to_cart():
    # Перейти в корзину
    browser.get("https://www.labirint.ru/cart")


def get_cart_counter():
    # Проверить счетчик товаров. Должен быть равен числу нажатий
    txt = browser.find_element(By.CSS_SELECTOR, 'a[data-event-label="myCart"]').find_element(By.CSS_SELECTOR, "b").text
    return int(txt)


def close_browser():
    browser.quit()


def test_card_counter():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    open_labirint()
    search('python')

    added = add_books()
    go_to_cart()
    cart_counter = get_cart_counter()
    assert added == cart_counter
    close_browser()
