import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Khởi tạo driver
service_obj = Service("D:/A_autotest/selenium/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# Mở trang web
driver.get("https://rahulshettyacademy.com/client/")
time.sleep(2)  # Chờ 2 giây để đảm bảo trang web đã tải

# Nhấp vào liên kết "Forgot password?"
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
time.sleep(1)  # Chờ 1 giây

# Nhập email
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
time.sleep(1)  # Chờ 1 giây

# Nhập mật khẩu
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("loan@1234")
time.sleep(1)  # Chờ 1 giây

# Nhập xác nhận mật khẩu
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("loan@1234")
time.sleep(1)  # Chờ 1 giây

# Nhấp vào nút "Save New Password"
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
time.sleep(2)  # Chờ 2 giây để hoàn tất thao tác

input("Nhấn Enter để thoát...")
