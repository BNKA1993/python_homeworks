from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager  # Изменено здесь
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

driver = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()))
driver.maximize_window()


for _ in range(3):
    driver.get("http://uitestingplayground.com/dynamicid")
    button_locator = "button.btn.btn-primary"
    button_input = driver.find_element(By.CSS_SELECTOR, button_locator)
    button_input.send_keys(Keys.RETURN)
    button_input.click()

driver.quit()
