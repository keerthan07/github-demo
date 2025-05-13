from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Shop").click()

ListOfMobiles = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in ListOfMobiles:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//div/ul/li/a").click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Ind")
wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='suggestions']/ul/li/a")))
# driver.find_element(By.XPATH, "//div[@class='suggestions']/ul/li/a").click()

wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()

driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

driver.find_element(By.XPATH, "//input[@type='submit']").click()

