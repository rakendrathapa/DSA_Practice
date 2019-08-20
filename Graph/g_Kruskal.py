# python program for Kruskal algorithm to find
# Minimum spanning tree of a given connected, weighted
# undirected graph
from collections import defaultdict


# Graph representing class
class Graph:
    class __Node:
        # private class Node, containing the weight of the edge and the vertices
        __slots__ = '_to_node', '_weight'

        def __init__(self, v, w):
            self._to_node = v
            self._weight = w

    class _Disjoint_set:
        def __init__(self, number_of_elements):
            self.parent = [i for i in range(number_of_elements)]
            self.rank = [0] * number_of_elements

        # Utility function to find the set of the an element i
        # uses path compression
        def find(self, i):
            if self.parent[i] == i:
                return i
            self.parent[i] = self.find(self.parent[i])

        # Utility function that uses ranking to do union of 2 sets
        def union(self, x, y):
            xroot = self.find(x)
            yroot = self.find(y)

            # Attach the smaller rank tree under the root of
            # higher rank tree (Union by Rank)
            if self.rank[xroot] < self.rank[yroot]:
                self.parent[xroot] = yroot
            elif self.rank[yroot] < self.rank[xroot]:
                self.parent[yroot] = xroot

            # Ranks are same. Make any one as root and increment the rank.
            else:
                self.parent[xroot] = yroot
                self.rank[yroot] += 1

    # Main class Graph
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self._Disjoint_set(vertices)

    def add_edges(self, u, v, w):
        self.graph[u].append(self.__Node(v, w))
        self.graph[v].append(self.__Node(u, w))  # Adding both the directions for the undirected graph

    # utility function that checks if the graph is cyclic
    def is_cyclic(self):
        # Iterate through all the edges of the graph.
        # find the set of both vertices of every edge.
        # if the set is same, then there is a cycle in the graph.
        for i in self.graph:
            for node in self.graph[i]:
                v = node._to_node
                x = self._Disjoint_set.find(i)
                y = self._Disjoint_set.find(v)
                if x == y:
                    return True
                self._Disjoint_set.union(x, y)

    # def takeWeight(self, i):

    # Kruskal algorithm to find the Minimum Spanning Tree
    def KruskalMST(self):
        result = []  # stores the resultant MST
        i = 0  # An index variable, used for sorted edges
        e = 0  # An index variable, used for result

        # Step 1: Sort all edges in non-decreasing order of their weight.
        # Create the copy of the graph
        # self.graph = sorted(self.graph, key=self.takeWeight)

        for i in self.graph:
            print(self.graph[i].__)
            # for node in self.graph[i]:
            #    print("u:{} -> v:{} w:{}".format(i, node._to_node, node._weight))
        return
