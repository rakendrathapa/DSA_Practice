from .Graph import UDGraph


class WeightedUDGraph(UDGraph):
    class UnionFind:
        def __init__(self, n):
            self.parent = [i for i in range(n)]
            self.rank = [0] * n

        def find(self, node):
            if self.parent[node] != node:
                self.parent[node] = self.find(self.parent[node])
            return self.parent[node]

        def union(self, u, v):
            p_u, p_v = self.find(u), self.find(v)
            if p_u != p_v:
                if self.rank[p_u] > self.rank[p_v]:
                    self.parent[p_v] = p_u
                elif self.rank[p_v] > self.rank[p_u]:
                    self.parent[p_u] = p_v
                else:
                    self.parent[p_v] = p_u
                    self.rank[p_v] += 1
                return True
            return False  # Same set

    def __init__(self, n):
        super().__init__(n)
        self.weights = list()

    def add_weighted_edge(self, u, v, w):
        self.addEdge(u, v)
        self.weights.append((u, v, w))

    def KruskalMST(self):
        result = list()
        uf = self.UnionFind(self.num_of_vertices)
        sorted_edges = sorted(self.weights, key=lambda item: item[2])

        for edge in sorted_edges:
            u, v, w = edge
            print(u, v, w)
            if uf.union(u, v):
                result.append((u, v))
            print(len(result))
        return result
