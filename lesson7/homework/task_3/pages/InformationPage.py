from selenium.webdriver.common.by import By


class InformationPage:
    def __init__(self, driver):
        self._driver = driver

    def add_first_name(self, value):
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(value)

    def add_last_name(self, value):
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(value)

    def add_zip_code(self, value):
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(value)

    def click_button(self):
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()



