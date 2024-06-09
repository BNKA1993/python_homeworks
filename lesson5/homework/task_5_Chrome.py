from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.maximize_window()

# зайти на сайт
driver.get("http://the-internet.herokuapp.com/inputs")

input_locator = 'input[type="number"]'

input_text = driver.find_element(By.CSS_SELECTOR, input_locator)
sleep(2)
input_text.send_keys("1000")
sleep(2)
input_text.clear()
sleep(2)
input_text.send_keys("999")
sleep(5)
