from .Graph import WeightedUDGraph

# Driver code
def testmain():
    testcases = []
    n = 9
    weighted_edges = [[0, 1, 4], [0, 7, 8], [1, 2, 8], [1, 7, 11], [2, 5, 4], [2, 3, 7],
             [3, 4, 9], [3, 5, 14], [5, 4, 10], [6, 5, 2], [7, 6, 1], [7, 8, 7],
             [8, 2, 2], [8, 6, 6]]
    testcases.append((n, weighted_edges))

    for cases in testcases:
        n, edges = cases
        g = WeightedUDGraph(n)
        for edge in edges:
            u, v, w = edge
            g.add_weighted_edges(u, v, w)

        print('KruskalMST:')
        for result in g.KruskalMST():
            print(result)


if __name__ == '__main__':
    testmain()

