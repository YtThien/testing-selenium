import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Khởi tạo driver
service_obj = Service("D:/A_autotest/selenium/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# Mở trang web
driver.get("https://rahulshettyacademy.com/angularpractice/")

# Tương tác với các phần tử
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()

# CSS tagname[attribute = 'value'] => //input[@type = 'submit'] #id .classname
driver.find_element(By.CSS_SELECTOR,"input[name = 'name']").send_keys("loan")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()

# Xpath - //tagname[@attribute = 'value'] => //input[@type='submit')
#Static dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(1)
#dropdown.select_by_value()


#driver.find_element(By.XPATH,"//input[@type = 'submit']").click()
driver.find_element(By.XPATH,"/html/body/app-root/form-comp/div/form/input").click()

message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("helloagain")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()





# Giữ trình duyệt mở cho đến khi bạn nhấn Enter
input("Nhấn Enter để thoát...")

# Điều này sẽ đảm bảo trình duyệt vẫn mở cho đến khi bạn nhấn Enter
