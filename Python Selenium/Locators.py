import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# Edge_path="C:/Thiyagarajan/Browser_Drivers/edgedriver_win64/msedgedriver.exe"
# Servive_Obj = Service(path)
# driver = webdriver.Edge(service=Servive_Obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
Title = driver.title
assert Title == "ProtoCommerce"
print(Title)
url = driver.current_url
print(url)
driver.find_element(By.XPATH, "(//div/input)[1]").send_keys("Thiyagarajan")
driver.find_element(By.NAME, "email").send_keys("thiyaga214111@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Thiyaga@19")
driver.find_element(By.XPATH, "//div/input[@type='checkbox']").click()
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
time.sleep(2) #wait time
dropdown.select_by_index(0)
#driver.find_element(By.XPATH, "//input[@xpath='1']").send_keys("Thiyagarajan")








time.sleep(5)



