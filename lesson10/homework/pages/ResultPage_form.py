from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing import List


class ResultPage:
    """
    Класс для взаимодействия со страницей результатов валидации.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализирует страницу результатов валидации.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self._driver = driver

    def empty_zip_result_is_red(self) -> int:
        """
        Проверяет, является ли поле почтового индекса пустым и имеет ли оно класс ошибки.

        :return: Количество элементов с классом ошибки для почтового индекса.
        """
        zip_id = self._driver.find_elements(By.CSS_SELECTOR, "#zip-code.alert-danger")
        return len(zip_id)

    def other_elements_result_is_green(self) -> List[str]:
        """
        Проверяет, что все другие элементы, кроме почтового индекса, имеют класс успеха.

        :return: Список классов элементов, кроме почтового индекса.
        """
        elements = self._driver.find_elements(By.CSS_SELECTOR, "div.alert")
        for el in elements:
            id_element = el.get_attribute('id')
            # Пропуск элемента zip-code
            if id_element == 'zip-code':
                continue
            class_list = el.get_attribute("class").split(' ')
            return class_list
