class DisjointSets:
    def __init__(self, n_sets):
        self.sets = n_sets
        self.parent = [i for i in range(n_sets)]
        self.rank = [0] * n_sets

    def __find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.__find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        parent_u, parent_v = self.__find(u), self.__find(v)
        if parent_u != parent_v:
            if self.rank[u] > self.rank[v]:
                self.parent[v] = u
            elif self.rank[v] > self.rank[u]:
                self.parent[u] = v
            else:
                self.parent[v] = u
                self.rank[u] += 1
            self.sets -= 1
