from time import sleep
import sys
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
			self.in_tree = InTree([(None, self.id)])

			for i in range(self.duration):

				if i % 5 == 0:
					self.hello()
				if i % 10 == 0:
					self.broadcast_in_tree()
				if i % 15 == 0 and (target not in (-1, id)):
					self.write.writeFile(self.message)

				msgs = self.read.readFile(self.inputFile)
				# for m in msgs:
				# 	print("New msg = ", m)
				sleep(1)

		except Exception as e:
			print(f"{e} in Node")

	def hello(self):
		self.write.writeFile(f'Hello {self.id}')

	def broadcast_in_tree(self):
		self.write.writeFile(f'intree {self.id}')

	def in_tree(self):
		pass

	def received(self):
		pass


if __name__ == '__main__':
	args = sys.argv
	if len(args) < 4 or len(args) > 5:
		print("Invalid Format")
		sys.exit()
	elif len(args) == 4:
		node = Node(int(args[1]), int(args[2]), int(args[3]))
	else:
		node = Node(int(args[1]), int(args[2]), int(args[3]), message=args[4])
