from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

my_cookie = {
	'name': 'cookie_policy',
	'value': '1'}

driver.get("https://labirint.ru/")
driver.add_cookie(my_cookie)

cookie = driver.get_cookie('PHPSESSID') #переменная, в которую соберутся cookies
print(cookie) #запрос на вывод данных в терминал

driver.refresh()

sleep(10)
driver.quit()