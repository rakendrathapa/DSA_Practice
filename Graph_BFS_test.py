from Graph import Graph as grph

def main():
    g = grph.Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print("BFS:")
    g.BFS(2)

if __name__ == "__main__":
    main()