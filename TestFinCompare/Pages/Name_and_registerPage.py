from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
driver = webdriver.Chrome(chrome_options=options, executable_path="C:/Users/Volodymyr.Chukhna/PycharmProjects"
                                                                  "/FinCompare/TestFinCompare/Drivers/chromedriver_76"
                                                                  ".exe", )

driver = webdriver.Chrome("C:/Users/Volodymyr.Chukhna/PycharmProjects/FinCompare/TestFinCompare/Drivers"
                          "/chromedriver_76.exe", )
driver.get('https://app.fincompare.de/wizard/company/search')
driver.maximize_window()
driver.find_element_by_id("companyName").send_keys("FinCompare GmbH")
time.sleep(2)
driver.find_element_by_xpath("//*[contains(text(),'Unternehmen suchen')]").click()
time.sleep(2)
driver.find_element_by_xpath("//*[contains(text(),'FinCompare GmbH')]").click()
time.sleep(3)
driver.find_element_by_id("firstName").send_keys("TestName")
time.sleep(2)
driver.find_element_by_id("lastName").send_keys("TestLastName")
time.sleep(2)
driver.find_element_by_id("phone").send_keys("888-888-888")
time.sleep(2)
driver.find_element_by_id("select-businessRelation").click()
time.sleep(2)
driver.find_element_by_xpath("//*[contains(text(),'Ihren Kunden')]").click()
time.sleep(2)
driver.find_element_by_xpath("//*[contains(text(),'Kostenlos registrieren')]").click()
driver.close()