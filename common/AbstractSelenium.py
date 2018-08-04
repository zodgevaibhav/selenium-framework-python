from selenium.webdriver.support.wait import WebDriverWait
import WebDriverFactory

class AbstractSelenium: #this class must inherited by each Test Class
	def setup_method(self, method): #this method will run before every test method, like @BeforeTest
		WebDriverFactory.WebDriverFactory.setDriver()
		print ("************************ Before method "+method.__name__)
		AbstractSelenium.methodName=method.__name__

	def teardown_method(self, method): #this method will run after every test method, like @AfterTest
		WebDriverFactory.WebDriverFactory.getDriver().quit()
		print ("************************ After method "+method.__name__)
		
