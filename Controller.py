from time import sleep
import sys
import os
from Reader import Reader
from Writer import Writer
from InTree import InTree


class Controller:

    def __init__(self, duration):
        # declaring class variables
        self.topo_file = os.getcwd()+'/topology.txt'
        self.topology = None
        self.files_path = os.getcwd()+'/files/'
        self.duration = duration
        self.channels = list()
        self.n_channels = 0
        self.nodes = set()

        self.read = Reader()

        # to check and create directory to store text files
        if not os.path.exists('files'):
            path = os.mkdir('files')

        # block to read topology file and store the graph (as a dictionary)
        try:
            with open(self.topo_file, mode='r') as readFile:
                temp = []
                line = readFile.readline()
                while line:
                    self.channels.append(
                        tuple([int(i) for i in line.strip().split(' ')]))
                    temp += [int(i) for i in line.strip().split(' ')]
                    line = readFile.readline()
                self.nodes = set(temp)
                self.n_channels = len(self.channels)
            self.in_tree = InTree()
            self.in_tree.createInTree(self.channels,self.nodes)
            self.topology = self.in_tree.return_topo()
        except Exception as e:
            print(e, "\nTopology file empty or file not available.")

        # Block to check for messages and transfer it
        for i in range(self.duration):
            print(
                f"----------------------- Counter ({i})--------------------------")
            files = os.listdir(self.files_path)
            files = [i for i in files if i.startswith('output')]
            for out_file in files:
                temp = out_file.split('.')
                outgoing_n = self.topology[int(temp[0][-1])]
                for n in outgoing_n:
                    inp = 'input_'+str(n)+'.txt'
                    self.read.readWriteFile(inp, out_file)
					

            # waiting for 1 second before next iteration
            sleep(1)

        # Treminating the program
        print('End!')
        sleep(5)
        exit()


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        cntrl = Controller(int(args[1]))
    else:
        print("Invalid Format")
        sys.exit()
