from selenium.webdriver.common.by import By


class ResultPage:
    def __init__(self, driver):
        self._driver = driver

    def add_books(self):
        by_buttons = self._driver.find_elements(By.CSS_SELECTOR, "a.btn-tocart.buy-link")
        counter = 0
        for btn in by_buttons:
            btn.click()
            counter += 1
        return counter

    def get_empty_result_message(self):
        div = self._driver.find_element(By.CSS_SELECTOR, "div.search-error")
        h1 = div.find_element(By.CSS_SELECTOR, 'h1')
        return h1.text
