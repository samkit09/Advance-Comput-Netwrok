from collections import defaultdict

class InTree:
	def __init__(self, channels):
		self.root = id
		self.graph = defaultdict(list)
		self.T = defaultdict(list)
		self.createInTree(channels)

	def addEdge(self, from_node, to_node):
		# append the neighbor node to its corresponding key node
		self.graph[from_node].append(to_node)
		self.T[to_node].append(from_node)

	def createInTree(self, channels):
		for channel in channels:
			self.addEdge(channel[0], channel[1])
		# print('Graph = ',self.graph)
		# print('InTree = ',self.T)

	def calculateInTree(self):
		pass

	def return_topo(self):
		return self.graph