from Graph import g_Kruskal

# Driver code
def testfunction():
    g = g_Kruskal.Graph(4)
    g.add_edges(0, 1, 10)
    g.add_edges(0, 2, 6)
    g.add_edges(0, 3, 5)
    g.add_edges(1, 3, 15)
    g.add_edges(2, 3, 4)

    g.KruskalMST()

if __name__ == '__main__':
    testfunction()