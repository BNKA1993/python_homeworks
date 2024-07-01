from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from selenium.webdriver.support import expected_conditions as EC

cookie = {"name": "cookie_policy", "value": "1"}


def test_card_counter():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # Перейти на сайт «Лабиринта»

    browser.get("https://www.labirint.ru")
    browser.add_cookie(cookie)
    browser.implicitly_wait(4)
    browser.maximize_window()

    # Найти все книги по слову Python
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys('python')
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Переключиться на таблицу
    by_buttons = browser.find_elements(By.CSS_SELECTOR, "a.btn-tocart.buy-link")

    # Добавить все книги в корзину и посчитать
    counter = 0
    for btn in by_buttons:
        btn.click()
        counter += 1
    print(counter)
    # Перейти в корзину
    browser.get("https://www.labirint.ru/cart")
    # Проверить счетчик товаров
    browser.find_element(By.CSS_SELECTOR, 'a[data-event-label="myCart"]')
    txt = browser.find_element(By.CSS_SELECTOR, 'a[data-event-label="myCart"]').find_element(By.CSS_SELECTOR, "b").text
    assert counter == int(txt)
    sleep(5)
    browser.quit()
