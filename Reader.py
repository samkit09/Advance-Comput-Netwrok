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
            print(e, "in Reader Contructor()")

    def readFile(self, input_file):
        '''
        Used by Node to read its input file.
        '''
        s = list()
        try:
            input = os.getcwd()+'/files/'+input_file
            temp = 0
            with open(input, mode='r') as readFile:
                line = readFile.readline()
                while line:
                    temp += 1
                    if temp > self.count_i:
                        s.append(line.strip())
                    line = readFile.readline()
                self.count_i = temp
                return s
        except:
            return s

    def readWriteFile(self, input_file, output_file):
        '''
        Used by Controller to read output files and write into input files.
        '''
        outf = os.getcwd()+'/files/'+output_file
        inpf = os.getcwd()+'/files/'+input_file
        try:
            temp = 0
            moder = 'a+' if os.path.exists(inpf) else 'r'
            modew = 'a+'
            with open(outf, moder) as readFile:
                line = readFile.readline().strip()
                while line:
                    temp += 1
                    if temp > self.count_o: # revert indent below 2 lines
                        with open(inpf, modew) as writeFile:
                            writeFile.write(line+'\n')
                    line = readFile.readline().strip()
                self.count_o = temp
        except Exception as e:
            print(e, "in readWriteFile()")
