# Test Automation framework FinCompare Instructions to Run

********Instructions.********
***********Install following software "pytest", "pytest-ordering","pytest-html"***********

Requirements for TestSuite run

1) Use below commands to install required plugins

Python 3 Version should be installed and also following packages:
pytest, html report and pytest-ordering

- pip3 install pytest
- pip3 install pytest-ordering
- pip3 install pytest-html

********Instructions to Run.********

Use below command to run the tests and generate the report for Credit and Login Pages

* py.test -s -v TestPackage/TestCreditPage.py --html=Htmlreport.html
* py.test -s -v TestPackage/TestRegisterPage.py --html=Htmlreport.html 


*****Observing Results.*****
Open HTML report with results in your browser, report is located in UtilityPackage directory 
and it contains filename with report inside, name of report is:
* htmlreport.html

