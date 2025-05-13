from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

# maximizing the window
driver.maximize_window()

# driver.get("https://rahulshettyacademy.com")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
print(driver.title)

print(driver.current_url)

# driver.get("https://rahulshettyacademy.com/seleniumpractise/#/")
# driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
# for closing the browser
driver.close()

