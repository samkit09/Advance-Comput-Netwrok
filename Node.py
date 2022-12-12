from time import sleep
import sys

import Reader
import Writer


class Node:
    def __init__(self, id: int, duration: int, target: int, message: str = None):
        try:
            self.id = id
            self.duration = duration
            self.destId = target
            self.message = message

            inputFile = "input_" + str(self.id) + ".txt"
            outputFile = "output_" + str(self.id) + ".txt"
            self.read = Reader(inputFile, outputFile)
            self.write = Writer(outputFile)

            for i in range(self.duration):
                if i % 5 == 0:
                    self.hello()
                if i % 10 == 0:
                    pass
                if i % 15 == 0:
                    pass
                self.read.readWriteFile()
                sleep(1)
        except Exception as e:
            print(e + " in Node")

    def hello(self):
        self.write.writeFile("Hello " + self.id)


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 4 or len(args) > 5:
        print("Invalid Format")
        sys.exit()
    elif len(args) == 4:
        node = Node(args[1], args[2], args[3])
    else:
        node = Node(args[1], args[2], args[3], message=args[4])
