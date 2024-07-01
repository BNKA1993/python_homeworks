from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(3)
        self._driver.maximize_window()

    def first_name(self, value):
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='first-name']").send_keys(value)

    def last_name(self, value):
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='last-name']").send_keys(value)

    def address(self, value):
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='address']").send_keys(value)

    def email(self, value):
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='e-mail']").send_keys(value)

    def phone(self, value):
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='phone']").send_keys(value)

    def zip_code(self, value):
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='zip-code']").send_keys(value)

    def city(self, value):
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='city']").send_keys(value)

    def country(self, value):
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='country']").send_keys(value)

    def job_position(self, value):
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='job-position']").send_keys(value)

    def company(self, value):
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='company']").send_keys(value)

    def send_form(self):
        self._driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

