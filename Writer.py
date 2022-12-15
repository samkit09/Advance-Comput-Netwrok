import os


class Writer:
    def __init__(self, writeFilePath: str):
        self.writeFilePath = os.getcwd()+'/files/'+writeFilePath
        self.count = 0

    def writeFile(self, message: str, path=None):
        if path != None:
            p = os.getcwd()+'/files/'+path
        else:
            p = self.writeFilePath
        try:
            with open(p, mode='a+') as writeFile:
                writeFile.write(message + '\n')
                self.count += 1
            writeFile.close()
        except Exception as e:
            print(e, " in writerFile")
