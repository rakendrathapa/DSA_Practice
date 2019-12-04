#include "BinaryTree.h"

unsigned int BinaryTree::size()
{
    return this->len;
}

bool BinaryTree::isEmpty()
{
    if (TreeRoot == nullptr){
        this->len = 0;
    }
    return (this->size() == 0);
}

void BinarySearchTree::Insert(int data)
{
    if (isEmpty()){
        Node* newNode = new Node(data, nullptr, nullptr);
        TreeRoot = newNode;
        len = 1;
        return;
    }
    InsertUtil(data, TreeRoot);
}

unsigned int BinaryTree::BFS()
{
    if (isEmpty()){
        std::cout << "BFS: Empty Tree" << std::endl;
        return 0;
    }
    return BFSUtil(TreeRoot);
}

unsigned int BinaryTree::DFS(DFSType order)
{
    if (isEmpty()){
        std::cout << "DFS: Empty Tree" << std::endl;
        return 0;
    }
    if(order == inorder){
        return DFSUtil_Inorder(TreeRoot);
    }
    else if (order == preorder){
        return DFSUtil_Preorder(TreeRoot);
    }
    else if (order == postorder){
        return DFSUtil_Postorder(TreeRoot);
    }
    return 0;
}

void BinarySearchTree::InsertUtil(int data, Node* node)
{
    if (node == nullptr)
    {
        Node *newNode = new Node(data, nullptr, nullptr);
        node = newNode;
        len += 1;
        return;
    }

    if(node->data <= data){
        if (node->right){
            InsertUtil(data, node->right);
        }else{
            Node *newNode = new Node(data, nullptr, nullptr);
            node->right = newNode;
            len += 1;
            return;
        }
    }else{
        if(node->left){
            InsertUtil(data, node->left);
        }else{
            Node *newNode = new Node(data, nullptr, nullptr);
            node->left = newNode;
            len += 1;
            return;
        }
    }
}

unsigned int BinaryTree::BFSUtil(Node* node)
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
        std::cout << newNode->data << " " << std::endl;
        if(nullptr != newNode->left){
            q.push(newNode->left);
        }
        if(nullptr != newNode->right){
            q.push(newNode->right);
        }
    }
    return count;
}

unsigned int BinaryTree::DFSUtil_Inorder(Node* node)
{
    unsigned int count = 0;
    if(node == nullptr){
        return 0;
    }
    if (node->left){
        count += DFSUtil_Inorder(node->left);
    }
    std::cout << node->data << " " <<std::endl;
    count += 1;

    if (node->right){
        count += DFSUtil_Inorder(node->right);
    }

    return count;
}

unsigned int BinaryTree::DFSUtil_Preorder(Node* node)
{
    unsigned int count = 0;
    if(node == nullptr){
        return 0;
    }
    std::cout << node->data << " " <<std::endl;
    count += 1;
    if (node->left){
        count += DFSUtil_Preorder(node->left);
    }
    if (node->right){
        count += DFSUtil_Preorder(node->right);
    }

    return count;
}

unsigned int BinaryTree::DFSUtil_Postorder(Node* node)
{
    unsigned int count = 0;
    if(node == nullptr){
        return 0;
    }
    if (node->left){
        count += DFSUtil_Postorder(node->left);
    }
    if (node->right){
        count += DFSUtil_Postorder(node->right);
    }
    std::cout << node->data << " " <<std::endl;
    count += 1;

    return count;
}

bool BinarySearchTree::Search(int key)
{
    if (isEmpty()){
        return false;
    }
    Node* searchNode = TreeRoot;
    while(searchNode)
    {
        if(key == searchNode->data){
            return true;
        }
        if (key > searchNode->data){
            searchNode = searchNode->right;
        }else if(key < searchNode->data){
            searchNode = searchNode->left;
        }
    }
    return false;
}
