import sys
sys.path.append('../common/')
import inspect,ExcelReader
class DataProvider:
	def getData(methodName):
		print(" **************"+inspect.stack()[1][3]+"."+methodName)
		#return [("1asd","Login with sahil shinde","SahilShinde")]
		return ExcelReader.ExcelReader.readData("../test/"+inspect.stack()[1][3]+".xlsx",methodName)