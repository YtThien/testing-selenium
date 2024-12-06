import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("D:/A_autotest/selenium/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# Mở trang web
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#Sum validation
prices = driver.find_elements(By.CSS_SELECTOR,"tr:nth-child(5) p")
sum = 0
for price in prices:
    # Lấy giá trị của price và loại bỏ bất kỳ ký tự không phải là số (ví dụ: dấu phẩy)
    price_text = price.text.strip().replace(',', '')  # Xử lý các dấu phẩy nếu có
    try:
        sum += int(price_text)  # Dùng float thay vì int để xử lý số thực
    except ValueError:
        print(f"Không thể chuyển đổi giá trị: {price_text}")

print(f"Sum calculated: {sum}")
totalAmount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text.strip().replace(',', ''))
print(f"Total Amount from page: {totalAmount}")

#assert abs(sum - totalAmount) < 1e-2  # Kiểm tra sai lệch nhỏ

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

print(driver.title)
print(driver.current_url)
