from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import time
import time

from selenium.webdriver.support.select import Select

service_obj = Service("E://Aditya//chromedriver-win64//chromedriver-win64//chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, "name").send_keys("keerthan")
driver.find_element(By.NAME, "email").send_keys("keerthanrampalli98@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12324567")
driver.find_element(By.ID, "exampleCheck1").click()

# CSS can be constructed by (tagname[attribute='value']), #id, .classname
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

# Static dropdowns
dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Male")
# dropdown.select_by_visible_text()

driver.find_element(By.XPATH, "//input[@type='submit']").click()


message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

assert "Success" in message

# driver.find_element(By.XPATH, "//input[@class='ng-pristine ng-valid ng-touched']").send_keys("AgainHello")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("AgainHello")
time.sleep(3)

# I am modifin gth efile to check the how git ranching works