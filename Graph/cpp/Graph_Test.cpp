#include "Graph.h"

int main()
{
    LinkedGraph *g = new LinkedGraph(4);
    g->InsertEdge(0,1);
    g->InsertEdge(0,2);
    g->InsertEdge(1,2);
    g->InsertEdge(2,0);
    g->InsertEdge(2,3);
    g->InsertEdge(3,3);

    std::cout << std::endl <<"BFS from vertex 2:";
    g->BFS(2);

    std::cout << std::endl <<"DFS from vertex 2:";
    g->DFS(2);

    delete g;
    return 0;
}
