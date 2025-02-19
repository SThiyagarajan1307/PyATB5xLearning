import time

from selenium import webdriver

#driver = webdriver.Chrome()
driver = webdriver.Edge()
driver.maximize_window()
time.sleep(2)
driver.get("https://www.udemy.com/")
time.sleep(2)
print(driver.title)
print(driver.current_url)
driver.close()





# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# driver.get("https://rahulshettyacademy.com")
# driver.maximize_window()
# print(driver.title)
# print(driver.current_url)
