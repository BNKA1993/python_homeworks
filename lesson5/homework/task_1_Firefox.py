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

# зайти на сайт
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# зайти на сайт
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# пять раз кликаем на кнопку Add Element
button_locator = 'button[onclick="addElement()"]'
button_input = driver.find_element(By.CSS_SELECTOR, button_locator)

for i in range(1, 6):
    button_input.send_keys(Keys.RETURN)
    
# собираем со страницы список кнопок Delete
buttons_delete_locators = 'button[onclick="deleteElement()"]'
buttons = driver.find_elements(By.CSS_SELECTOR, buttons_delete_locators)

# выводим на экран размер списка
print(len(buttons))
driver.close()