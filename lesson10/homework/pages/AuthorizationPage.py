from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AuthorizationPage:
    """
    Класс для взаимодействия со страницей авторизации.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализирует страницу авторизации.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(3)
        self._driver.maximize_window()

    def username(self, value: str) -> None:
        """
        Вводит имя пользователя.

        :param value: Имя пользователя.
        """
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(value)

    def password(self, value: str) -> None:
        """
        Вводит пароль.

        :param value: Пароль.
        """
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys(value)

    def click_login(self) -> None:
        """
        Нажимает на кнопку входа.
        """
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()
