from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service


def test_Guru99():
    s = Service(executable_path="C:\\Users\\PC\\Desktop\\Selenium Driver files\\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.get('https://demo.guru99.com/test/newtours/register.php')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys('Merlin')
    driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys('Lyola')
    driver.find_element(By.XPATH, "//input[@name='phone']").send_keys('123456789')
    driver.find_element(By.XPATH, "//input[@id='userName']").send_keys('merlin123@gmail.com')
    driver.find_element(By.XPATH, "//input[@name='address1']").send_keys('French Road')
    driver.find_element(By.XPATH, "//input[@name='city']").send_keys('Rochester')
    driver.find_element(By.XPATH, "//input[@name='state']").send_keys('Newyork')
    driver.find_element(By.XPATH, "//input[@name='postalCode']").send_keys('14618')
    driver.find_element(By.XPATH, "//input[@id='email']").send_keys('merlin123@gmail.com')
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys('admin123')
    driver.find_element(By.XPATH, "//input[@name='confirmPassword']").send_keys('admin123')
    driver.find_element(By.XPATH, "//input[@name='submit']").click()
    driver.close()
