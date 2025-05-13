from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")

service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

driver.implicitly_wait(5)

# Taking a screenshot
driver.get_screenshot_as_file("screenshot.png")
driver.get_screenshot_as_png()
