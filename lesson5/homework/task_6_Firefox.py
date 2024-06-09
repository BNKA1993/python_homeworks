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
driver.get("http://the-internet.herokuapp.com/login")
sleep(1)

username_locator = "#username"
input_username = driver.find_element(By.CSS_SELECTOR, username_locator)
input_username.send_keys("tomsmith")
sleep(1)

password_locator = "#password"
input_password = driver.find_element(By.CSS_SELECTOR, password_locator)
input_password.send_keys("SuperSecretPassword!")
sleep(1)

login_locator = "i.fa.fa-2x.fa-sign-in"
input_login = driver.find_element(By.CSS_SELECTOR, login_locator)
input_login.click()
sleep(1)

driver.quit()