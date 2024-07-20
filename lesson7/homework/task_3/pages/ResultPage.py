from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResultPage:
    def __init__(self, driver):
        self._driver = driver

    def text_result(self):
        txt = self._driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[8]").text
        return txt



