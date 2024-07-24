from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:
    """
    Класс для взаимодействия со страницей ввода данных.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализирует главную страницу.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(3)
        self._driver.maximize_window()

    def first_name(self, value: str) -> None:
        """
        Вводит имя пользователя.

        :param value: Имя пользователя.
        """
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='first-name']").send_keys(value)

    def last_name(self, value: str) -> None:
        """
        Вводит фамилию пользователя.

        :param value: Фамилия пользователя.
        """
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='last-name']").send_keys(value)

    def address(self, value: str) -> None:
        """
        Вводит адрес пользователя.

        :param value: Адрес пользователя.
        """
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='address']").send_keys(value)

    def email(self, value: str) -> None:
        """
        Вводит электронную почту пользователя.

        :param value: Электронная почта пользователя.
        """
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='e-mail']").send_keys(value)

    def phone(self, value: str) -> None:
        """
        Вводит номер телефона пользователя.

        :param value: Номер телефона пользователя.
        """
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='phone']").send_keys(value)

    def zip_code(self, value: str) -> None:
        """
        Вводит почтовый индекс.

        :param value: Почтовый индекс.
        """
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='zip-code']").send_keys(value)

    def city(self, value: str) -> None:
        """
        Вводит город пользователя.

        :param value: Город пользователя.
        """
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='city']").send_keys(value)

    def country(self, value: str) -> None:
        """
        Вводит страну пользователя.

        :param value: Страна пользователя.
        """
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='country']").send_keys(value)

    def job_position(self, value: str) -> None:
        """
        Вводит должность пользователя.

        :param value: Должность пользователя.
        """
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='job-position']").send_keys(value)

    def company(self, value: str) -> None:
        """
        Вводит компанию пользователя.

        :param value: Компания пользователя.
        """
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='company']").send_keys(value)

    def send_form(self) -> None:
        """
        Отправляет форму.
        """
        self._driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
