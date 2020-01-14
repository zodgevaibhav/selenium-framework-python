# selenium-framework-python

Setup :
  1. Download python from https://www.python.org/downloads/windows/ and Install it.
  2. Install pip ()
      Download https://bootstrap.pypa.io/get-pip.py file and keep it at c:\
      run this python file by command "py c:\get-pip.py"
      Make sure pip path is added in environmental variable
  3. Install Selenium Webdriver "pip install -U selenium"
  4. Install openpyxl, it will be used to read excel files. Install using command "pip install -U openpyxl"
  5. Install pytest testing framework by using command "pip install -U pytest"
  6. Install pytesthtml to generate html report from tests "pip install pytest-html"
  7. Install pytest-xdist to run tests parallel by command "pip install pytest-xdist"
  8. Install pytest-rerunfailures to re-run the failed tests. "pip install pytest-rerunfailures"
  
Test execution :
  pytest TestLogin.py
  
  pytest pytest --junitxml=junitResult.xml TestLogin.py
  
  pytest --html=report.html TestLogin.py. //This will work only if pytest-html installed
  
  pytest -n 3 --html=report.html TestLogin.py
  
  pytest -n 3 --rerun 2 --html=report.html TestLogin.py
