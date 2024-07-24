from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """
    Класс для взаимодействия с корзиной.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализирует страницу корзины.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self._driver = driver

    def get_to_cart(self) -> None:
        """
        Переходит к корзине.
        """
        self._driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container>a').click()

    def get_to_checkout(self) -> None:
        """
        Переходит к странице оформления заказа.
        """
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()

