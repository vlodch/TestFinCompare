from UtilityPackage.SeleniumDriver import SeleniumDriver


class CompanySearchAndRegisterPages(SeleniumDriver):

    _companyName = "companyName"  # Id
    _submitButtonCompanySearch = "//*[contains(text(),'Unternehmen suchen')]"  # Xpath
    _clickFinCompareLink = "//h3[contains(text(),'FinCompare GmbH')]"  # Xpath
    _sendFirstName = "firstName"  # Id
    _sendLastName = "lastName"  # Id
    _findPhoneLocator = "phone"  # Id
    _sendPhone = "phone"  # Id
    _selectBuisnesRelation = "//div[@id='select-businessRelation']"  # Xpath
    _selectIhrenKunden = "//*[contains(text(),'Ihren Kunden')]"  # Xpath
    _emailError = "//p[@id='name-error-text']"  # Xpath
    _submitRegister = "//*[contains(text(),'Kostenlos registrieren')]"  # Xpath

    def FillOutCompanyName(self, cn="FinCompare GmbH"):
        self.sendKeys(cn, self._companyName, locatorType="id")

    def ClickSubmitButton(self):
        self.elementClick(self._submitButtonCompanySearch, locatorType="xpath")

    def ClickFinCompareLink(self):
        self.elementClick(self._clickFinCompareLink, locatorType="xpath")

    def SendFirstName(self, fn="Testfn"):
        self.sendKeys(fn, self._sendFirstName, locatorType="id")

    def SendLastName(self, ln="Testln"):
        self.sendKeys(ln, self._sendLastName, locatorType="id")

    def SendPhone(self, pn="33322213"):
        self.sendKeys(pn, self._findPhoneLocator, locatorType="id")

    def ClickBuisnessRelationMenu(self):
        self.elementClick(self._selectBuisnesRelation, locatorType="xpath")

    def SelectIhrenKunden(self):
        self.elementClick(self._selectIhrenKunden, locatorType="xpath")

    def ClickSubmitRegisterButton(self):
        self.elementClick(self._submitRegister, locatorType="xpath")

    def CheckEmailErrorField(self):
        self.isElementPresent(self._emailError, locatorType="xpath")