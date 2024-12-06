import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Tạo đối tượng Service sử dụng ChromeDriverManager
service_obj = Service(ChromeDriverManager().install())

# Truyền đối tượng service vào Chrome WebDriver
driver = webdriver.Chrome(service=service_obj)

# Mở trang web
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")


# ChromeDriverManager Chr ChromeDriverManageromeDriverManager ChromeDriverManager ChromeDriverManager