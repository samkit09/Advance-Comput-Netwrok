class Writer:
	def __init__(self, writeFilePath: str):
		try:
			self.writeFilePath = writeFilePath
			self.count = 0
		except Exception as e:
			print(e, "in Writer")
	
	def writeFile(self, message: str):
		try:
			with open(self.writeFilePath, mode='a') as writeFile:
				writeFile.write(message + '\n')
				self.count += 1
		except Exception as e:
			print(e, "in Writer")