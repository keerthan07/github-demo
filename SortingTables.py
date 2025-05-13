from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

browserSortedVeggies = []

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

VeggiesList = driver.find_elements(By.XPATH, "//tr/td[1]")

for veggie in VeggiesList:
    browserSortedVeggies.append(veggie.text)
print(browserSortedVeggies)

OriginalVeggiesList = browserSortedVeggies.copy()

browserSortedVeggies.sort()

assert OriginalVeggiesList == browserSortedVeggies

