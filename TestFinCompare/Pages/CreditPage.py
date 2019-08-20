from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

options = Options()
options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
driver = webdriver.Chrome(chrome_options=options,
                          executable_path="C:/Users/Volodymyr.Chukhna/PycharmProjects/FinCompare/TestFinCompare/Drivers/chromedriver_76.exe", )
driver.implicitly_wait(2)

# Navigating to base page and validate if page is displayed
# page = driver.get('https://app.fincompare.de/wizard/products/')
page = driver.get('https://app.fincompare.de/wizard/products/')
driver.maximize_window()
# validate_success_navigationtoBasePage()

# Maximize window
driver.maximize_window()
# validate_success_navigationtoBasePage()
# Find Locators of elements and fill out them by some data
driver.find_element_by_class_name("funnel__products__title").click()
# Send Amount 2 to amount field
driver.find_element_by_id("amount").send_keys("2")
driver.find_element_by_xpath("(//div[@class='jss135 jss138 jss136 jss122 jss107'])[1]").click()
time.sleep(2)
driver.find_element_by_xpath("(//span[@class='jss174']/..)[11]").click()
time.sleep(4)
driver.find_element_by_xpath("(//div[@class='jss135 jss138 jss136 jss122 jss107'])[2]").click()
time.sleep(4)
driver.find_element_by_xpath("//*[contains(text(),'18 Monate')]").click()
time.sleep(4)
driver.find_element_by_xpath("//*[contains(text(),'Weiter')]").click()
driver.close()
