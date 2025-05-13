from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)


def test_handling_windows():

    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/windows")

    driver.find_element(By.XPATH, "//a[text()='Click Here']").click()

    windows_opened = driver.window_handles
    print(windows_opened)

    driver.switch_to.window(windows_opened[1])
    print(driver.find_element(By.XPATH, "//div/h3").text)

    driver.switch_to.window(windows_opened[0])
    print(driver.find_element(By.CSS_SELECTOR, "div h3").text)
