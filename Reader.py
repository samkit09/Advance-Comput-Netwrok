# Reader class
class Reader:

    # setting up class variables 
    count = 0
    channel = 0
    readFilePath, writeFilePath = ''

    def _init_(self,readFilePath,writeFilePath) -> None:
        '''
        Constructor for Reader class
        '''
        try:
            self.readFilePath = readFilePath
            self.readWriteFile = writeFilePath
        except Exception as e:
            print(e+" in Reader Contructor")
        finally:
            pass

    def readWriteFile(self):
        '''
        Used by Controller to read output files and write into input files.
        '''
        try:
            temp = 0
            with open(self.readFilePath,'r') as readFile:
                line = readFile.readline()
                while line:
                    temp += 1
                    if temp>self.count:
                        with open(self.writeFilePath,'a') as writeFile:
                            writeFile.write(line+'\n')
                    line = readFile.readline()
                self.count = temp
        except Exception as e:
            print(e+" in readWriteFile()")