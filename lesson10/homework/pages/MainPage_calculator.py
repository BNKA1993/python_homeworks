from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:
    """
    Класс для взаимодействия с главной страницей медленного калькулятора.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализирует главную страницу.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(3)
        self._driver.maximize_window()

    def delay(self, value: str) -> None:
        """
        Устанавливает значение задержки.

        :param value: Значение задержки в миллисекундах.
        """
        delay_element = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_element.clear()
        delay_element.send_keys(value)

    def click_button(self, text: str) -> None:
        """
        Нажимает на кнопку с заданным текстом.

        :param text: Текст кнопки.
        """
        self._driver.find_element(By.XPATH, f"//span[text() = '{text}']").click()
