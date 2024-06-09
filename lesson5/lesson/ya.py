from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru")
driver.get("https://vk.com")
driver.set_window_size(640, 460)
driver.save_screenshot("./ya.png")
# driver.maximize_window #открыть окно по размеру экрана
# driver.minimize_window #свернуть окно браузера
# driver.fullscreen_window #развернуть окно на весь экран, аналог F11

# for x in range(1, 10):
#     driver.back()
#     driver.forward()

# driver.refresh()

sleep(50)