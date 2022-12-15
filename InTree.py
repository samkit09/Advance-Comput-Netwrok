from collections import defaultdict
import re


class InTree:
    def __init__(self):
        self.graph = defaultdict(list)
        self.T = defaultdict(list)
        self.nodes = list()

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

    def updateInTree(self, id, intree):
        # tempintree = defaultdict(list)
        edges = re.findall(r'\d+', intree)
        edges = edges[1:]
        edges = [(int(edges[i]), int(edges[i+1]))
                 for i in range(0, len(edges), 2)]

        # print("Updating - ", edges)

        for i in edges:
            if i[1] not in self.T[i[0]]:
                self.T[i[0]].append(i[1])

            # for j in self.T.keys():
            #     print(i, 'edges[i] - ', edges[i], 'SElf.T 1-', self.T[j])
            #     print(True if edges[i] in self.T[j] else False)
            #     if edges[i] in self.T[j] and edges[i+1] not in self.T:
            #         print('SElf.T 2-', self.T[j])
            #         self.T[j].append(edges[i+1])
        # print(self.T)

    def return_in_tree(self):
        return self.T

    def return_topo(self):
        return self.graph
