from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class InformationPage:
    """
    Класс для взаимодействия со страницей ввода информации о пользователе.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализирует страницу информации.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self._driver = driver

    def add_first_name(self, value: str) -> None:
        """
        Вводит имя пользователя.

        :param value: Имя пользователя.
        """
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(value)

    def add_last_name(self, value: str) -> None:
        """
        Вводит фамилию пользователя.

        :param value: Фамилия пользователя.
        """
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(value)

    def add_zip_code(self, value: str) -> None:
        """
        Вводит почтовый индекс.

        :param value: Почтовый индекс.
        """
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(value)

    def click_button(self) -> None:
        """
        Нажимает на кнопку продолжения.
        """
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()
