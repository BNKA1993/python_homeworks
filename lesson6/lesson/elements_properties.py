from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/checkboxes")

divs = driver.find_elements(By.CSS_SELECTOR, "div")

div = divs[6]
#запрашиваем атрибуты и помещаем в переменную css_class:
css_class = div.get_attribute("class")
#выводим в терминал:
print(css_class)
driver.quit()

# div = driver.find_element(By.CSS_SELECTOR, "#page-footer")
# a = div.find_element(By.CSS_SELECTOR, "a")
# divs = driver.find_elements(By.CSS_SELECTOR, "div")
# print(a.get_attribute("href"))
# print(len(divs))

# cb = driver.find_element(By.CSS_SELECTOR, "input[type=checkbox]")

# is_selected = cb.is_selected()
# print(is_selected)

# sleep(3)

# cb.click()

# is_selected = cb.is_selected()
# print(is_selected)

# sleep(3)

# driver.quit()


# is_enabled = driver.find_element(By.CSS_SELECTOR, '#yesRadio').is_enabled()
# print(is_enabled)

# is_enabled = driver.find_element(By.CSS_SELECTOR, '#noRadio').is_enabled()
# print(is_enabled)



# is_displayed = driver.find_element(
# By.CSS_SELECTOR, "#transparentButton").is_displayed()
# print(is_displayed)

# driver.find_element(By.CSS_SELECTOR, '#hideButton').click()
# sleep(2)

# is_displayed = driver.find_element(
# By.CSS_SELECTOR, "#transparentButton").is_displayed()
# print(is_displayed)
# sleep(2)


# txt = driver.find_element(By.CSS_SELECTOR, 'a[href="https://news.mail.ru/currency/charcode/USD/"]').text
# tag = driver.find_element(By.CSS_SELECTOR, 'a[href="https://news.mail.ru/currency/charcode/USD/"]').tag_name
# id = driver.find_element(By.CSS_SELECTOR, 'a[href="https://news.mail.ru/currency/charcode/USD/"]').id
# href = driver.find_element(By.CSS_SELECTOR, 'a[href="https://news.mail.ru/currency/charcode/USD/"]').get_attribute("href")
# ff = driver.find_element(By.CSS_SELECTOR, 'a[href="https://news.mail.ru/currency/charcode/USD/"]').value_of_css_property("font-family")

# print(txt)
# print(tag)
# print(id)
# print(href)
# print(ff)



