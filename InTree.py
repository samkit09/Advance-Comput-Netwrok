from collections import defaultdict


class InTree:
    def __init__(self):
        self.root = id
        self.graph = defaultdict(list)
        self.T = defaultdict(list)

    def addEdge(self, from_node, to_node):
        # append the neighbor node to its corresponding key node
        if to_node not in self.graph[from_node]:
            self.graph[from_node].append(to_node)
        if from_node not in self.graph[to_node]:
            self.T[to_node].append(from_node)

    def remove_node(self, rem):
        # remove the node from graph and tree
        del self.graph[rem]
        del self.T[rem]
        for node in self.graph.keys():
            try:
                self.graph[node].remove(rem)
            except:
                pass
        for node in self.T.keys():
            try:
                self.T[node].remove(rem)
            except:
                pass

    def createInTree(self, channels, nodes):
        self.nodes = sorted(list(nodes))
        for channel in channels:
            self.addEdge(channel[0], channel[1])
        print('\nGraph = ', self.graph)
        print('InTree = ', self.T)
        print(self.nodes)

    def updateInTree(self, intree):
        print("Updating - ", intree)
        tempintree = defaultdict(list)
        pass

    def return_in_tree(self):
        return self.T

    def return_topo(self):
        return self.graph
