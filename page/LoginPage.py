import WebDriverFactory
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage:
		
	def __init__(self):
		self.wait=WebDriverWait(WebDriverFactory.WebDriverFactory.getDriver(),20)
		
	def navigateToLoginPage(self):
		self.driver = WebDriverFactory.WebDriverFactory.getDriver()
		self.driver.maximize_window()
		self.driver.get("https://stagemc.transnox.com/jsp/vt/jsp/index.jsp")
		return self
		
	def __login(self,userName):
		self.driver.switch_to_frame("mainFrame")
		self.driver.find_element_by_id("validateUserId_loginName").send_keys(userName)
		self.driver.find_element_by_name("bt_login").click()
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