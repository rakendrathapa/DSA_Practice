#include <iostream>
#include <vector>
#include <queue>

class Node{
public:  
    int data;
    Node *left, *right;
    Node(int data, Node* left, Node* right):data(data), left(left), right(right){}
};

class Tree
{
private:
    Node *TreeRoot;
    unsigned int len;
    virtual unsigned int BFSUtil(Node* node);
    virtual unsigned int DFSUtil(Node* node);
    virtual void InsertUtil(int data, Node *node);
    virtual bool isEmpty();
    virtual unsigned int size();

public:
    Tree(Node* root=nullptr) : TreeRoot(root){
        if(root == nullptr){
            len = 0;
        }
        else{
            len = DFSUtil(root);
        }
    }    
    virtual unsigned int BFS();
    virtual unsigned int DFS();
    virtual void Insert(int data);
};

unsigned int Tree::size()
{
    return this->len;
}

bool Tree::isEmpty()
{
    if (TreeRoot == nullptr){
        this->size = 0;
    }
    return (this->size() == 0);
}

void Tree::Insert(int data)
{
    if (isEmpty()){
        Node* newNode = new Node(data, nullptr, nullptr);
        TreeRoot = newNode;
        len = 1;
        return;
    }
    InsertUtil(data, TreeRoot); 
}

unsigned int Tree::BFS()
{
    if (isEmpty()){
        std::cout << "BFS: Empty Tree" << std::endl;
        return 0;
    }
    return BFSUtil(TreeRoot);
}

unsigned int Tree::DFS()
{
    if (isEmpty()){
        std::cout << "DFS: Empty Tree" << std::endl;
        return 0;
    }
    return DFSUtil(TreeRoot);
}

void Tree::InsertUtil(int data, Node* node)
{
    if (node == nullptr)
    {   
        Node *newNode = new Node(data, nullptr, nullptr);
        node = newNode;
        len += 1;
        return;
    }

    if(node->data <= data){
        node = node->right;
    }else{
        node = node->left;
    }
    InsertUtil(data, node);
}

unsigned int Tree::BFSUtil(Node* node)
{
    unsigned int count = 0;
    if(node == nullptr){
        return 0;
    }
    std::queue<Node*> q;
    q.push(node);
    while(q.empty() == false){
        Node *newNode = q.front();
        q.pop();
        count += 1;
        std::cout << newNode->data << std::endl;
        if(nullptr != newNode->left){
            q.push(newNode->left);
        }
        if(nullptr != newNode->right){
            q.push(newNode->right);
        }
    }
    return count;
}
unsigned int Tree::DFSUtil(Node* node)
{
    unsigned int count = 0;
    if(node == nullptr){
        return 0;
    }
    return count;
}

int main()
{
    Tree *
    Node* leftNode = new Node();
    Node* rightNode = new Node();
    Node *root = new Node(1, leftNode, rightNode);
}