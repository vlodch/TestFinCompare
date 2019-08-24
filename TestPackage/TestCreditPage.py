from selenium import webdriver
from PageObjectsPackage.CreditPage import CreditPage
from PageObjectsPackage.CompanySearchAndRegisterPages import CompanySearchAndRegisterPages
import unittest
import pytest
import time


class TestCreditPage(unittest.TestCase):
    baseURLCreditPage = "https://app.fincompare.de/wizard/products/"
    baseURLCompanySearchPage = "https://app.fincompare.de/wizard/company/search"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(baseURLCreditPage)
    cp = CreditPage(driver)
    csp = CompanySearchAndRegisterPages(driver)

    """
    Test case 1 : Verification for Credit Page, checking if all fields are accessible/selectable/able to be filled out
    """

    @pytest.mark.run(order=1)
    def test_CreditPage(self):
        self.driver.get(self.baseURLCreditPage)
        time.sleep(3)
        self.cp.ClickKreditLink()
        time.sleep(3)
        self.cp.FillOutAmounField()
        time.sleep(3)
        self.cp.ClickPurposeDropdown()
        time.sleep(3)
        self.cp.ChooseFromPurposeDropdownMenu()
        time.sleep(3)
        self.cp.ChooseTerms()
        time.sleep(3)
        self.cp.ChoseFromTermsMenu()
        time.sleep(2)
        self.cp.ChoseFromCountMonaiteDropdown()
        time.sleep(2)
        self.cp.ClickSubmitButton()
        time.sleep(5)






