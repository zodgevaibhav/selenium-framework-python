import WebDriverFactory
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import BasePage

class LoginPage(BasePage.BasePage):
		
	elmLoginButton=(By.NAME,"bt_login")
	elmUserName=(By.ID,"validateUserId_loginName")
	
	
	def __init__(self):
		self.wait=WebDriverWait(WebDriverFactory.WebDriverFactory.getDriver(),20)
		self.driver=WebDriverFactory.WebDriverFactory.getDriver()
		
	def navigateToLoginPage(self):
		self.driver.get("https:")
		return self
		
	def __login(self,userName):
		self.driver.switch_to_frame("mainFrame")
		self.findElementBy(self.elmUserName).send_keys(userName)
		self.findElementBy(self.elmLoginButton).click()
		return self

	def loginForExpiredPassword(self,userName):
		self.__login(userName)
		self.wait.until(expected_conditions.presence_of_element_located((By.ID,"bt_ok")))
		return self

	def loginForSuccess(self,userName):
		self.__login(userName)
		#code to return home page
		return self

	def loginForInvalidUser(self,userName):
		self.__login(userName)
		return self		

	def printErrorMessage(self):
		print(self.driver.find_element_by_xpath("//p[@class='sorry-message']").text)