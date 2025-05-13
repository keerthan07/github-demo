from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("E://Aditya//chromedriver-win64//chromedriver-win64//chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
vegetables = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(3)

# Vegetables list displayed on the page
vegetableNames = driver.find_elements(By.XPATH, "//div/div/h4")
print(vegetableNames)

for vegetableName in vegetableNames:
    if vegetableName.text in vegetables:
        print("Yes")

veggies = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(veggies))

for veggie in veggies:
    veggie.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Sum Validation

prices = driver.find_elements(By.CSS_SELECTOR, "tr td:last-child p")
sum = 0
for price in prices:
    sum += int(price.text)

print(sum)

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[text()='Apply']").click()

wait = WebDriverWait(driver, 10)
promoText = wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo"))).text

print(promoText)

totalAmount = int(driver.find_element(By.XPATH, "//span[@class='totAmt']").text)
print(totalAmount)
assert sum == totalAmount

discountAmount = int(driver.find_element(By.XPATH, "//span[@class='discountAmt']").text)
print(discountAmount)

assert totalAmount == discountAmount

driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

time.sleep(4)


