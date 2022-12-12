import os


class Writer:
    def __init__(self, writeFilePath: str):
        self.writeFilePath = os.getcwd()+'/files/'+writeFilePath
        self.count = 0

    def writeFile(self, message: str):
        try:
            with open(self.writeFilePath, mode='a+') as writeFile:
                writeFile.write(message + '\n')
                self.count += 1
        except Exception as e:
            print(e, " in writerFile")
