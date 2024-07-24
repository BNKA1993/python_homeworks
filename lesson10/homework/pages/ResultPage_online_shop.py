from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ResultPage:
    """
    Класс для взаимодействия со страницей результатов оформления заказа.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализирует страницу результатов оформления заказа.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self._driver = driver

    def text_result(self) -> str:
        """
        Получает текст результата на странице оформления заказа.

        :return: Текст результата.
        """
        txt = self._driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[8]").text
        return txt
