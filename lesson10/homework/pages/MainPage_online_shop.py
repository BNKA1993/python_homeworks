from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:
    """
    Класс для взаимодействия с главной страницей магазина.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализирует главную страницу магазина.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self._driver = driver

    def add_to_cart(self) -> None:
        """
        Добавляет товары в корзину.
        """
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
