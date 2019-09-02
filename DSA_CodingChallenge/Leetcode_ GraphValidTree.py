"""
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
Example 1:
Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:
Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
"""
from collections import defaultdict


class Graph:

    def __init__(self, num_of_v):
        self.n_vertices = num_of_v
        self.edges = defaultdict(list)

    # Graph is array of edges
    def add_edge(self, edge):
        u = edge[0]
        v = edge[1]
        self.edges[u].append(v)


class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank


def find(subsets, node):
    while subsets[node].parent != node:
        node = subsets[node].parent

    return subsets[node].parent


def union(subsets, u, v):
    if subsets[u].rank > subsets[v].rank:
        subsets[v].parent = u
    elif subsets[v].rank > subsets[u].rank:
        subsets[u].parent = v
    else:
        subsets[v].parent = u
        subsets[u].rank += 1


def isNotCycle(graph):
    subsets = []
    for u in range(graph.n_vertices):
        subsets.append(Subset(u, 0))

    # Iterate through all edges of the graph
    # find sets of both vertices of every edge
    # if sets are same, then there is cycle in the graph
    for u in graph.edges:
        u_rep = find(subsets, u)
        for v in graph.edges[u]:
            v_rep = find(subsets, v)
            if u_rep == v_rep:
                return False
            else:
                union(subsets, u_rep, v_rep)


    prev = subsets[0]
    for u in range(1, len(subsets)):
        u_rep = subsets[u]
        if prev != u_rep:
            return False
        prev = u_rep
    return True


class Solution:
    def validTree(self, n, edges):
        g = Graph(n)
        for edge in edges:
            g.add_edge(edge)
        return isNotCycle(g)

def main():
    testcases = []
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    case = (n, edges)
    testcases.append(case)
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    case = (n, edges)
    testcases.append(case)
    n = 100
    edges = [[6, 27], [83, 9], [10, 95], [48, 67], [5, 71], [18, 72], [7, 10],
             [92, 4], [68, 84], [6, 41], [82, 41], [18, 54], [0, 2], [1, 2],
             [8, 65], [47, 85], [39, 51], [13, 78], [77, 50], [70, 56], [5, 61],
             [26, 56], [18, 19], [35, 49], [79, 53], [40, 22], [8, 19], [60, 56],
             [48, 50], [20, 70], [35, 12], [99, 85], [12, 75], [2, 36], [36, 22],
             [21, 15], [98, 1], [34, 94], [25, 41], [65, 17], [1, 56], [43, 96],
             [74, 57], [19, 62], [62, 78], [50, 86], [46, 22], [10, 13], [47, 18],
             [20, 66], [83, 66], [51, 47], [23, 66], [87, 42], [25, 81], [60, 81],
             [25, 93], [35, 89], [65, 92], [87, 39], [12, 43], [75, 73], [28, 96],
             [47, 55], [18, 11], [29, 58], [78, 61], [62, 75], [60, 77], [13, 46],
             [97, 92], [4, 64], [91, 47], [58, 66], [72, 74], [28, 17], [29, 98],
             [53, 66], [37, 5], [38, 12], [44, 98], [24, 31], [68, 23], [86, 52],
             [79, 49], [32, 25], [90, 18], [16, 57], [60, 74], [81, 73], [26, 10],
             [54, 26], [57, 58], [46, 47], [66, 54], [52, 25], [62, 91], [6, 72],
             [81, 72], [50, 35], [59, 87], [21, 3], [4, 92], [70, 12], [48, 4], [9, 23],
             [52, 55], [43, 59], [49, 26], [25, 90], [52, 0], [55, 8], [7, 23], [97, 41],
             [0, 40], [69, 47], [73, 68], [10, 6], [47, 9], [64, 24], [95, 93], [79, 66],
             [77, 21], [80, 69], [85, 5], [24, 48], [74, 31], [80, 76], [81, 27], [71, 94],
             [47, 82], [3, 24], [66, 61], [52, 13], [18, 38], [1, 35], [32, 78], [7, 58],
             [26, 58], [64, 47], [60, 6], [62, 5], [5, 22], [60, 54], [49, 40], [11, 56],
             [19, 85], [65, 58], [88, 44], [86, 58]]
    case = (n, edges)
    testcases.append(case)
    n = 4
    edges = [[0, 1], [2, 3]]
    case = (n, edges)
    testcases.append(case)

    sol = Solution()
    for cases in testcases:
        n, edges = cases
        print(n, edges)
        ans = sol.validTree(n, edges)
        print(ans)


if __name__ == '__main__':
    main()
