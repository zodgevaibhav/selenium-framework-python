import inspect
class DataProvider:
	def getData(methodName):
		print(" **************"+inspect.stack()[1][3]+"."+methodName)
		return [("SahilShinde")]