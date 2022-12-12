from time import sleep
import sys
import os

import Reader
import Writer


class Controller:

    def __init__(self, duration) -> None:
        self.topo_file = 'topology.txt'
        self.duration = duration
        self.channels = list()
        self.nodes = set()
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
            print(self.nodes)
        except Exception as e:
            print(e, "\nTopology file empty or file not available.")


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        cntrl = Controller(int(args[1]))
    else:
        print("Invalid Format")
        sys.exit()
