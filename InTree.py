from collections import defaultdict

class InTree:
    def __init__(self):
        self.graph = defaultdict(list)
        self.T = defaultdict(list)

    def addEdge(self, from_node, to_node):
        # append the neighbor node to its corresponding key node
        self.graph[from_node].append(to_node)
        self.T[to_node].append(from_node)

    def calculateInTree(self):
        pass
