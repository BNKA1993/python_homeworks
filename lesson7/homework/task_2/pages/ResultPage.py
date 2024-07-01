from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResultPage:
    def __init__(self, driver):
        self._driver = driver

    def display_time_result(self):
        waiter = WebDriverWait(self._driver, 46)
        result = waiter.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="calculator"]/div[1]/div'), "15"))

        result_element = self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[1]/div')
        return int(result_element.text)

