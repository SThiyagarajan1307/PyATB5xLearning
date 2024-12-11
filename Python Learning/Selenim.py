import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Replace "path/to/chromedriver" with the actual path to your ChromeDriver executable
driver_path = ("E:/Thiyagarajan/chromedriver-win64/chromedriver.exe")
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Open Google in the new Chrome window
driver.maximize_window()
driver.get("https://www.google.com")
driver.find_element(By.XPATH, "//div/textarea").send_keys("Hello")

time.sleep(5)