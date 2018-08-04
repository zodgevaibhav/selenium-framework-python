import pytest
import sys
sys.path.append('../page/')
sys.path.append('../common/')

import WebDriverFactory,LoginPage,AbstractSelenium

class TestLogin(AbstractSelenium.AbstractSelenium):

    @pytest.mark.parametrize("userName", [("vzodge")])
    def test_verifyLoginForExpiredUser(self,userName):
        print("*********** in test1",userName)
        LoginPage.LoginPage().navigateToLoginPage().loginForExpiredPassword(userName).printErrorMessage()

    @pytest.mark.parametrize("userName", [("vaibhavz"),("zodge")])
    def test_verifyLoginForInvalidUser(self,userName):
        print("*********** in test1",userName)
        LoginPage.LoginPage().navigateToLoginPage().loginForInvalidUser(userName)