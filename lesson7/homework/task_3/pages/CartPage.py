from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self._driver = driver

    def get_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container>a').click()

    def get_to_checkout(self):
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()
