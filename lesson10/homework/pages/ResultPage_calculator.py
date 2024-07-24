from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class ResultPage:
    """
    Класс для взаимодействия со страницей результатов калькулятора.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализирует страницу результатов.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self._driver = driver

    def display_time_result(self) -> int:
        """
        Ожидает отображения результата на странице и возвращает его.

        :return: Значение результата на странице.
        """
        waiter = WebDriverWait(self._driver, 46)
        waiter.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="calculator"]/div[1]/div'), "15"))

        result_element = self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[1]/div')
        return int(result_element.text)
