
import sys
sys.path.append('../page/')
sys.path.append('../common/')

import WebDriverFactory,LoginPage

dr = WebDriverFactory.WebDriverFactory()

LoginPage.LoginPage().navigateToLoginPage().login("vzodge").printErrorMessage()
WebDriverFactory.WebDriverFactory.getDriver().quit()