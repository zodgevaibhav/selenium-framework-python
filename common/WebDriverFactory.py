from selenium import webdriver

class WebDriverFactory:

    def setDriver():
        #WebDriverFactory.driver = webdriver.Chrome(r"C:\Users\vaibh\Downloads\chromedriver_win32\chromedriver.exe") #set driver object to static driver object
        WebDriverFactory.driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities={
            "browserName": "chrome"
            #"browserVersion": "latest",
            #"video": "True",
            #"platform": "WIN10",
            #"platformName": "windows",
        })
        
    def getDriver():
        return WebDriverFactory.driver
