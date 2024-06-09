from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
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

login_locator = "button[type=submit]"
input_login = driver.find_element(By.CSS_SELECTOR, login_locator)
input_login.click()
sleep(1)

driver.quit()
