from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager  # Изменено здесь
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.alert import Alert

driver = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()))
driver.maximize_window()

for _ in range(3):
    print("Вывод А")
    driver.get("http://uitestingplayground.com/classattr")
    button_blue_locator = "button.btn-primary.btn-test"
    button_input = driver.find_element(By.CSS_SELECTOR, button_blue_locator)
    button_input.click()
    alert = Alert(driver) 
    print(alert.text) 
    alert.accept() 
    # driver.close()
    print("Вывод Б")


driver.quit()