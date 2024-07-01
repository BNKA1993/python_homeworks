from selenium.webdriver.common.by import By


class AuthorizationPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(3)
        self._driver.maximize_window()

    def username(self, value):
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(value)

    def password(self, value):
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys(value)

    def click_login(self):
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()
