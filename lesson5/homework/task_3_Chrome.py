from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
 
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
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
