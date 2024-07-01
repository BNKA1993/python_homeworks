from selenium.webdriver.common.by import By


class ResultPage:
    def __init__(self, driver):
        self._driver = driver

    def empty_zip_result_is_red(self):
        zip_id = self._driver.find_elements(By.CSS_SELECTOR, "#zip-code.alert-danger")
        return len(zip_id)

    def other_elements_result_is_green(self):
        elements = self._driver.find_elements(By.CSS_SELECTOR, "div.alert")
        for el in elements:
            id_element = el.get_attribute('id')
            # пропуск элемента zip-code
            if id_element == 'zip-code':
                continue
            class_list = el.get_attribute("class").split(' ')
            return class_list

