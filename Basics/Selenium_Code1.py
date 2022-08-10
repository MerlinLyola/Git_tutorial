from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

s=Service(executable_path="C:/Users/PC/Desktop/Selenium Driver files/msedgedriver.exe")
driver=webdriver.Edge(service=s)
driver.get('https://google.com')
driver.maximize_window()
print(driver.title)
print(driver.current_url)