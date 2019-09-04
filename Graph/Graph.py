from collections import defaultdict, deque

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
