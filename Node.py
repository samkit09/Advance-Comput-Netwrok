from time import sleep
import sys
import re
import traceback
from Reader import Reader
from Writer import Writer
from InTree import InTree


class Node:
    def __init__(self, id: int, duration: int, target: int, message: str = None):
        try:
            self.id = id
            self.duration = duration
            self.destId = target
            self.message = message

            self.inputFile = "input_" + str(self.id) + ".txt"
            self.outputFile = "output_" + str(self.id) + ".txt"
            self.receivedFile = str(self.id) + "_received" + ".txt"
            self.read = Reader()
            self.write = Writer(self.outputFile)
            self.write_log = Writer(self.receivedFile)
            self.tree = InTree()  # [(None, self.id)]
            self.in_tree = self.tree.return_in_tree()
            self.known_neigh = list()

            for i in range(self.duration):

                # Hello Protocol: Sending hello message with id every 5 seconds
                if i % 5 == 0:
                    self.hello()

                # Intree Protocol: Sending intree message every 10 seconds
                if i % 10 == 0:
                    # print("In_tree: ", self.in_tree)
                    self.broadcast_in_tree()

                # Sending data: Sending message to target every 15 seconds
                if i % 15 == 0 and self.message != None:
                    self.write.writeFile(self.message)

                # Reading: Reading message from input file
                msgs = self.read.readFile(self.inputFile)
                for m in msgs:
                    # when received hello message append to known neighbor and update intree
                    if m[:5] == "Hello":
                        t = int(m.strip()[-1])
                        if t not in self.known_neigh:
                            self.known_neigh.append(t)
                            self.tree.addEdge(t, self.id)

                    elif m[:6] == "intree":
                        self.tree.updateInTree(self.id, m)
                        # print("User", self.id, ' - ', self.in_tree)

                    else:
                        flag = 0
                        self.received(m)
                        from_to = re.findall(r'\d+', m)
                        from_to = [int(i) for i in from_to]
                        # print(from_to)
                        if from_to[1] != self.id and flag == 0:
                            for id, neighbor in self.in_tree.items():
                                # print(neighbor)
                                if self.id in neighbor:
                                    self.write.writeFile(m, self.outputFile)
                                    break
                                    flag = 1

                # Waiting for 1 second before next iteration
                sleep(1)

            # print("Known Neighbour: ", 'ID = ',self.id, 'N = ', self.known_neigh)
            print("Intree of ", self.id, ' =', dict(self.in_tree))
            # Treminating the program
            exit()

        except Exception as e:
            traceback.print_exception(*sys.exc_info())
            print(f"{e} in Node")

            # treminating the program
            exit()

    def hello(self):
        self.write.writeFile(f'Hello {self.id}')

    def broadcast_in_tree(self):
        s = f'intree {self.id} '
        for id, neighbor in self.in_tree.items():
            # print('intree - ',self.id,self.in_tree)
            if neighbor != [None]:
                for j in neighbor:
                    s += f'({id} {j})'
        # print('Printing s - ', s)
        self.write.writeFile(s)

    def received(self, m):
        self.write.writeFile(m, self.receivedFile)


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 4 or len(args) > 5:
        print("Invalid Format")
        sys.exit()
    elif len(args) == 4:
        node = Node(int(args[1]), int(args[2]), int(args[3]))
    else:
        node = Node(int(args[1]), int(args[2]), int(args[3]), message=args[4])

    # try:
    #     node = Node(int(args[1]), int(args[2]), int(args[3]), message=args[4])
    # except Exception as e:
    #     print("Invalid Format: ", e)
