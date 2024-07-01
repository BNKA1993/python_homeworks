from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(3)
        self._driver.maximize_window()

    def delay(self, value):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(value)

    def click_button(self, text):
        self._driver.find_element(By.XPATH, f"//span[text() = '{text}']").click()

