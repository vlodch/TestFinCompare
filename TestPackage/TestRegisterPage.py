from selenium import webdriver
from PageObjectsPackage.CompanySearchAndRegisterPages import CompanySearchAndRegisterPages
import unittest
import pytest
import time

"""
 Test case 2 : Verification for Company Search and Register pages, checking if all fields are accessible/selectable/able to be filled out
"""


class TestRegisterPage(unittest.TestCase):
    baseURLCompanySearchPage = "https://app.fincompare.de/wizard/company/search"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(baseURLCompanySearchPage)
    csp = CompanySearchAndRegisterPages(driver)

    @pytest.mark.run(order=1)
    def test_CompanySearchAndRegisterPages(self):
        self.driver.get(self.baseURLCompanySearchPage)
        time.sleep(3)
        self.csp.FillOutCompanyName()
        time.sleep(2)
        self.csp.ClickSubmitButton()
        time.sleep(2)
        self.csp.ClickFinCompareLink()
        time.sleep(3)
        self.csp.SendFirstName()
        time.sleep(2)
        self.csp.SendLastName()
        time.sleep(3)
        self.csp.ClickBuisnessRelationMenu()
        time.sleep(3)
        self.csp.SelectIhrenKunden()
        time.sleep(3)
        self.csp.SendPhone()
        time.sleep(2)
        self.csp.ClickSubmitRegisterButton()
        time.sleep(5)
        self.csp.CheckEmailErrorField()
        time.sleep(3)
