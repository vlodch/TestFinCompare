from UtilityPackage.SeleniumDriver import SeleniumDriver


class CreditPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _kreditLink = "funnel__products__title"  # Classname
    _amountElement = "amount"  # By id
    _findPurposeDropdown = "/html[1]/body[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]"  # xpath
    _choosePurposeDropdown = "//li[contains(text(),'Software / IT / EDV')]"  # xpath
    _chooseTerms = "select-term"  # id
    _chooseFromTermsMenu = "//li[@class='jss171 jss505 jss508 jss513 jss514 jss516 jss502 jss504 jss503']"  # Xpath
    _findCountMonaiteDropdown = "//span[@class='jss174']/..)[11]"  # Xpath
    _chooseMonaiteCount = "//*[contains(text(),'18 Monate')]"  # Xpath
    _submitButton = "//*[contains(text(),'Weiter')]"  # Xpath

    def ClickKreditLink(self):
        self.elementClick(self._kreditLink, locatorType="class")

    def FillOutAmounField(self, s1=2):
        self.sendKeys(s1, self._amountElement, locatorType="id")

    def ClickPurposeDropdown(self):
        self.elementClick(self._findPurposeDropdown, locatorType="xpath")

    def ChooseFromPurposeDropdownMenu(self):
        self.elementClick(self._choosePurposeDropdown, locatorType="xpath")

    def ChooseTerms(self):
        self.elementClick(self._chooseTerms, locatorType="id")

    def ChoseFromTermsMenu(self):
        self.elementClick(self._chooseFromTermsMenu, locatorType="xpath")

    def ChoseMonaiteDropdown(self):
        self.elementClick(self._findCountMonaiteDropdown, locatorType="xpath")

    def ChoseFromCountMonaiteDropdown(self):
        self.elementClick(self._chooseMonaiteCount, locatorType="xpath")

    def ClickSubmitButton(self):
        self.elementClick(self._submitButton, locatorType="xpath")