class temp:
	global varone
	varone = [1,2]
	def __init__(self, test):
		self.test = test

	def prin(self):
		print(self.varone)

	def setVarOne(self, var):
		temp = varone
		varone.append(var)
	
	def testGlobal(self):
		print(varone)

ta = temp(5)
ta.setVarOne(6)
ta.testGlobal()