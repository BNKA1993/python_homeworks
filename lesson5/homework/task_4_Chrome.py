from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.maximize_window()

# зайти на сайт
driver.get("http://the-internet.herokuapp.com/entry_ad")

# дожидаемся появления модального окна
modal = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal")))
    
button = modal.find_element(By.CSS_SELECTOR, "div.modal-footer > p")
button.click()

driver.quit()

