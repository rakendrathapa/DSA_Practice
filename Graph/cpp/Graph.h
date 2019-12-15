#include <vector>
#include <iostream>
#include <queue>

class Graph
{
    // objects: A nonempty set of vertices and a set of undirected edges
    // each edge is a pair of vertices
    public:
    int e;      // Number of edges
    int n;      // Number of vertices

    public:
    virtual ~Graph(){}  // virtual destructor
    bool IsEmpty() const{return n==0;}  // return true if no vertices
    int NumOfVertices() const {return n;}   // return the number of vertices in the graph
    int NumOfEdges() const {return e;}  // return the number of edges in the graph
    virtual int Degree(int u) const = 0;    // return number of edges incident on u
    virtual bool ExistsEdge(int u, int v) const=0;  // return true if graph has the edge(u,v)
    virtual void InsertVertex(int v) = 0;   // insert vertex v into the graph; v has no incident edges
    virtual void InsertEdge(int u, int v) = 0;  // insert edge (u,v) in the graph
    virtual void DeleteVertex(int v) = 0;   // Deletes vertex v and all the edges incident on it.
    virtual void DeleteEdge(int u, int v) = 0;  // Delete edge (u,v) from the graph
};

class LinkedGraph : public Graph
{
    private:
    std::vector<int> *adjLists;

    void DFSUtil(int u, bool* &visited)
    {
        std::cout << u << " ";
        visited[u] = true;
        std::vector<int>::iterator it = adjLists[u].begin();
        while( it != adjLists[u].end())
        {
            if(visited[*it] == false){
                DFSUtil(*it, visited);
            }
            it++;
        }
    }

    public:
    LinkedGraph(const int vertices=0)
    {
        n = vertices;
        e = 0;
        adjLists = new std::vector<int>[vertices];
    }

    int Degree(int u) const
    {
        if (u > n){
            std::cerr << "Error: Invalid vertex" << std::endl;
            return -1;
        }
        else{
            return adjLists[u].size();
        }
    }

    bool ExistsEdge(int u, int v) const{
        if (( u > n ) || (v > n)){
            std::cerr << "Invalid Vertex" << std::endl;
            return false;
        }
        std::vector<int>::iterator it= adjLists[u].begin();
        while(it != adjLists[u].end()){
            if (*(it++) == v){
                return true;
            }
        }
        return false;
    }

    void InsertEdge(int u, int v){
        if ((u > n) || (v > n)){
            std::cerr << "Invalid vertices "<< std::endl;
            return;
        }
        adjLists[u].push_back(v);
    }

    void InsertVertex(int v)
    {
        return;
    }

    void DeleteVertex(int v)
    {
        return;
    }

    void DeleteEdge(int u, int v)
    {
        return;
    }

    // Prints BFS traversal from a given node
    void BFS(int s)
    {
        if (IsEmpty() || (s > n)){
            std::cerr << "Graph Empty or Invalid Node" << std::endl;
            return;
        }
        bool *visited = new bool[n];
        for(int i=0; i<n; i++){
            visited[n] = false;
        }

        // Create a queue;
        std::queue<int> q;
        q.push(s);
        while(q.empty() == false){
            int e = q.front();
            std::cout << e << " ";
            visited[e] = true;
            q.pop();
            std::vector<int>::iterator it = adjLists[e].begin();
            while(it != adjLists[e].end()){
                if(visited[*it] == false){
                    q.push(*(it));
                }
                it++;
            }
        }
        delete[] visited;
    }

    // Prints DFS traversal from a given node
    void DFS(int s)
    {
        if (IsEmpty() || (s > n)){
            std::cerr << "Graph Empty or Invalid Node" << std::endl;
            return;
        }
        bool *visited = new bool[n];
        for (int i=0; i<n; i++){
            visited[i] = false;
        }
        DFSUtil(s, visited);
        delete[] visited;
    }
};
