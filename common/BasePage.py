import sys
sys.path.append('../common/')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import WebDriverFactory
class BasePage:
	def findElementBy(self,elementDescription):
		wait=WebDriverWait(WebDriverFactory.WebDriverFactory.getDriver(),20)
		wait.until(expected_conditions.presence_of_element_located((elementDescription[0],elementDescription[1])))
		return WebDriverFactory.WebDriverFactory.getDriver().find_element(elementDescription[0],elementDescription[1])