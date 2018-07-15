from selenium import webdriver

class WebDriverFactory:
	name="Vaibhav Zodge"
	driver = webdriver.Chrome("E:\selenium\chromedriver.exe")
	#def __init__(self):
	
	def getDriver():
		return WebDriverFactory.driver
	