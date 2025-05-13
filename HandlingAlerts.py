from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)


def test_alerts():

    name = "Keerthan"
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Name']").send_keys(name)
    driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()

    alert = driver.switch_to.alert
    alertText = alert.text
    print(alertText)
    assert name in alertText

    alert.accept()
    # alert.dismiss()

    driver.find_element(By.CSS_SELECTOR, "#confirmbtn").click()
    time.sleep(3)
