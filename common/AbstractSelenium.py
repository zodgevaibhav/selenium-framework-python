from selenium.webdriver.support.wait import WebDriverWait
import WebDriverFactory

class AbstractSelenium:
	
	def __init__(self):
		print("****************** in AbstractSelenium constructor")
		self.wait=WebDriverWait(WebDriverFactory.WebDriverFactory.getDriver(),20)