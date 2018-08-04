import inspect
import pytest
import sys
sys.path.append('../page/')
sys.path.append('../common/')

import WebDriverFactory,LoginPage,DataProvider,AbstractSelenium

class TestLogin(AbstractSelenium.AbstractSelenium):

    @pytest.mark.parametrize("userName", [("vzodge")])
    def verifyLoginForExpiredUser(self,userName):
        print("*********** in test1",userName)
        LoginPage.LoginPage().navigateToLoginPage().loginForExpiredPassword(userName).printErrorMessage()

    @pytest.mark.parametrize("userName", [("vaibhavz"),("zodge")])
    def verifyLoginForInvalidUser(self,userName):
        print("*********** in test1",userName)
        LoginPage.LoginPage().navigateToLoginPage().loginForInvalidUser(userName)

    @pytest.mark.parametrize("TC_ID,TC_NAME,userName",DataProvider.DataProvider.getData("test_verifyLoginForInvalidUser"))
    def test_verifyLoginForInvalidUser(self,TC_ID,TC_NAME,userName):
        print("*********** in test1",userName)
        LoginPage.LoginPage().navigateToLoginPage().loginForInvalidUser(userName)