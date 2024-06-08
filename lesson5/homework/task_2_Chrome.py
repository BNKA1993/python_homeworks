from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.maximize_window()


for _ in range(3):
    driver.get("http://uitestingplayground.com/dynamicid")
    button_locator = "button.btn.btn-primary"
    button_input = driver.find_element(By.CSS_SELECTOR, button_locator)
    button_input.send_keys(Keys.RETURN)
    button_input.click()

driver.quit()
