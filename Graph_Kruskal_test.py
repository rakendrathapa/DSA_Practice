from Graph import WeightedUDGraph as graph


def testmain():
    testcases = []
    n = 9
    edges = [[0, 1, 4], [0, 7, 8], [1, 2, 8], [2, 5, 4], [2, 3, 7],
             [3, 4, 9], [3, 5, 14], [5, 4, 10], [6, 5, 2], [7, 6, 1],
             [7, 8, 7], [7, 1, 11], [8, 2, 2], [8, 6, 6]]

    case = (n, edges)
    testcases.append(case)

    count = 1
    for cases in testcases:
        n, edges = cases
        g = graph.WeightedUDGraph(n)
        for edge in edges:
            u, v, w = edge
            g.add_weighted_edge(u, v, w)

        print('\nGraph:{count}'.format(count=count))
        print('Kruskal MST:')
        mst = g.KruskalMST()
        print(mst)
        print('\n-----------------------------------')
        count += 1


if __name__ == '__main__':
    testmain()
