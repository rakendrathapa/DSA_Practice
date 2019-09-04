from collections import defaultdict, deque
from .DisjointSets import DisjointSets

class Graph:
    def __init__(self, num_vertices):
        self.edges = defaultdict(list)
        self.num_of_vertices = num_vertices

    def addEdge(self, u, v):
        raise NotImplementedError('To be implemented in the subclass')

class UDGraph(Graph):
    def __init__(self, n):
        super().__init__(n)

    def addEdge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def __DFSUtil(self, visited, u):
        if u is None:
            return
        visited[u] = True
        print('{', u, '} --> ', end='')
        for v in self.edges[u]:
            if visited[v] is False:
                self.__DFSUtil(visited, v)

    def DFS(self, vertex):
        visited = [False] * self.num_of_vertices
        self.__DFSUtil(visited, vertex)

    def BFS(self, vertex):
        if vertex is None:
            return
        visited = [False] * self.num_of_vertices
        queue = deque()
        queue.appendleft(vertex)
        visited[vertex] = True
        while len(queue):
            u = queue.pop()
            # print('{', u, '} --> ', end='')
            for v in self.edges[u]:
                if visited[v] is False:
                    queue.appendleft(v)
                    visited[v] = True
            yield u


class WeightedUDGraph(UDGraph):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.weights = list()

    def add_weighted_edges(self, u, v, w):
        self.addEdge(u, v)
        self.weights.append((u, v, w))

    def KruskalMST(self):
        result = list()
        sorted_edges = sorted(self.weights, key=lambda item: item[2])
        uf = DisjointSets(self.num_of_vertices)
        for edge in sorted_edges:
            u, v, w = edge
            if uf.union(u, v):
                result.append((u, v))
        yield result


