import os


class Reader:

    # Contstructor for Reader class
    def __init__(self):
        '''
        Constructor for Reader class
        '''
        try:
            self.count_o = 0
            self.count_i = 0
            self.channel = 0
        except Exception as e:
            print(e, "in Reader Contructor")

    def readFile(self, input_file):
        '''
        Used by Node to read its input file.
        '''
        self.input_file = os.getcwd()+'/files/'+input_file
        temp = 0
        s = []
        with open(self.input_file, mode='a+') as readFile:
            line = readFile.readline().strip()
            while line:
                temp += 1
                if temp > self.count_i:
                    s.append(line)
                line = readFile.readline()
            self.count_i = temp
            return s

    def readWriteFile(self, input_file, output_file):
        '''
        Used by Controller to read output files and write into input files.
        '''
        self.output_file = os.getcwd()+'/files/'+output_file
        self.input_file = os.getcwd()+'/files/'+input_file
        try:
            temp = 0
            mode = 'a+' if os.path.exists(self.input_file) else 'r'
            with open(self.output_file, mode) as readFile:
                line = readFile.readline().strip()
                while line:
                    temp += 1
                    if temp > self.count_o:
                        mode = 'a+'
                        with open(self.input_file, mode) as writeFile:
                            writeFile.write(line+'\n')
                    line = readFile.readline()
                self.count_o = temp
        except Exception as e:
            print(e, "in readWriteFile()")
