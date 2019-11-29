from myTime import *
from myMemory import *


class TestCases:
	def __init__(self):
		self.n = [10, 25, 50, 100, 500, 1000, 5000, 10000]
		self.testsConstantCapacity = dict()
		self.testsVaryingCapacity = dict()

	def __generateTests(self):
		for numberItems in self.n:
			"""
			self.testsVaryingCapacity[numberItems] = [[(i, random.randint(1, 2 + int(numberItems/10)), random.randint(1, 2+int(numberItems/5))) 
						for i in range(numberItems)], random.randint(max(int(numberItems/10), 20), max(int(numberItems/5), 100))]
			self.testsConstantCapacity[numberItems] = [[(i, random.randint(1, 2 + int(numberItems/10)), random.randint(1, 2+int(numberItems/5))) 
						for i in range(numberItems)], 1]
			"""

class Analyze:
	def __init__(self):
