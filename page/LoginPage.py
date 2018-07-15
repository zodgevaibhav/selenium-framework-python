import WebDriverFactory
from AbstractSelenium import AbstractSelenium
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class LoginPage(AbstractSelenium):
		
	def navigateToLoginPage(self):
		self.driver = WebDriverFactory.WebDriverFactory.getDriver()
		self.driver.maximize_window()
		self.driver.get("https://yourtestsite.com")
		return self
		
	def login(self,userName):
		self.driver.switch_to_frame("mainFrame")
		self.driver.find_element_by_id("validateUserId_loginName").send_keys(userName)
		self.driver.find_element_by_name("bt_login").click()
		self.wait.until(expected_conditions.presence_of_element_located((By.ID,"bt_ok")))
		return self

	def printErrorMessage(self):
		print(self.driver.find_element_by_xpath("//p[@class='sorry-message']").text)