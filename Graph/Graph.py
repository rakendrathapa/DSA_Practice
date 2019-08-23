from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self, s):
        if s is None:
            return

        visited = [False] * (len(self.graph))
        queue=[]

        queue.append(s)
        visited[s]=True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of dequeued vertex s.
            # If adjacent has not been visited, then mark it as
            # visited and enqueue it.
            for node in self.graph[s]:
                if visited[node] == False:
                    visited[node] = True
                    queue.append(node)
