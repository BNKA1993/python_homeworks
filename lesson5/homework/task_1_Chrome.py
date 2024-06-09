from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.maximize_window()

# зайти на сайт
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# пять раз кликаем на кнопку Add Element
button_locator = '//button[text()="Add Element"]'
button_input = driver.find_element(By.XPATH, button_locator)

for i in range(1, 6):
    button_input.send_keys(Keys.RETURN)
    
# собираем со страницы список кнопок Delete
buttons_delete_locators = '//button[text()="Delete"]'
buttons = driver.find_elements(By.XPATH, buttons_delete_locators)

# выводим на экран размер списка
print(len(buttons))
