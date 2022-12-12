import os

# Reader class
class Reader:

	# setting up class variables 

	def __init__(self, readFilePath, writeFilePath) -> None:
		'''
		Constructor for Reader class
		'''
		try:
			self.readFilePath = readFilePath
			self.writeFilePath = writeFilePath
			self.count = 0
			self.channel = 0
		except Exception as e:
			print(e, "in Reader Contructor")
		finally:
			pass

	def readWriteFile(self):
		'''
		Used by Controller to read output files and write into input files.
		'''
		try:
			temp = 0
			with open(self.readFilePath, mode='a+') as readFile:
				line = readFile.readline()
				while line:
					temp += 1
					if temp>self.count:
						mode = 'a' if os.path.exists(self.writeFilePath) else 'w'
						with open(self.writeFilePath, mode) as writeFile:
							writeFile.write(line+'\n')
					line = readFile.readline()
				self.count = temp
		except Exception as e:
			print(e, "in readWriteFile()")