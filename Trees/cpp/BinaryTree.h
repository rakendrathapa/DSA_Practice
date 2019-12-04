#include <iostream>
#include <cstdlib>
#include <vector>
#include <queue>

using namespace std;

class Node{
public:
    int data;
    Node *left, *right;
    Node(int data, Node* left, Node* right):data(data), left(left), right(right){}
};

enum DFSType
{
    inorder,
    preorder,
    postorder
};

class BinaryTree
{
private:
    virtual unsigned int BFSUtil(Node* node);
    virtual unsigned int DFSUtil_Inorder(Node* node);
    virtual unsigned int DFSUtil_Preorder(Node* node);
    virtual unsigned int DFSUtil_Postorder(Node* node);

protected:
    Node *TreeRoot;
    unsigned int len;
    virtual unsigned int size();

public:
    BinaryTree(Node *root = nullptr) : TreeRoot(root){
        if(root == nullptr){
            len = 0;
        }
        else{
            len = BFS();
        }
    }
    virtual bool isEmpty();
    virtual unsigned int BFS();
    virtual unsigned int DFS(DFSType order = DFSType::inorder);
    virtual void Insert(int data) = 0;
};

class BinarySearchTree : public BinaryTree
{
private:
    virtual void InsertUtil(int data, Node *node);

public:
    BinarySearchTree(Node* root = nullptr) : BinaryTree(root){
    }
    virtual void Insert(int data);
    virtual bool Search(int key);
};
