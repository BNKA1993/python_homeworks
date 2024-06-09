from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager  # Изменено здесь
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()))
driver.maximize_window()


# зайти на сайт
driver.get("http://the-internet.herokuapp.com/inputs")

input_locator = 'input[type="number"]'

input_text = driver.find_element(By.CSS_SELECTOR, input_locator)
sleep(1)
input_text.send_keys("1000")
sleep(1)
input_text.clear()
sleep(1)
input_text.send_keys("999")
sleep(1)

driver.quit()