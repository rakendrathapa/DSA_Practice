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
            if self.rank[parent_u] > self.rank[parent_v]:
                self.parent[parent_v] = parent_u
            elif self.rank[parent_v] > self.rank[parent_u]:
                self.parent[parent_u] = parent_v
            else:
                self.parent[v] = parent_u
                self.rank[parent_v] += 1
            self.sets -= 1
            return True
        return False
