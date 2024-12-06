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
driver.get("https://rahulshettyacademy.com")



time.sleep(10)
driver.get("http://localhost/qltau2/admin/login.php")
driver.maximize_window()
print(driver.title)
print(driver.current_url)