#include "BinaryTree.h"

int main()
{
    BinarySearchTree *tree = new BinarySearchTree();
    tree->Insert(8);
    tree->Insert(3);
    tree->Insert(10);
    tree->Insert(1);
    tree->Insert(6);
    tree->Insert(14);
    tree->Insert(4);
    tree->Insert(7);
    tree->Insert(13);

    int countNodes = 0;
    std::cout << "BFS: ";
    countNodes = tree->BFS();
    std::cout << "\tNo of nodes:" << countNodes << std::endl;

    std::cout << "DFS: Inorder" << tree->DFS() << std::endl;
    std::cout << "DFS: Preorder" << tree->DFS(DFSType::preorder) << std::endl;
    std::cout << "DFS: Postorder" << tree->DFS(DFSType::postorder) << std::endl;

    int searchkey = 0;
    std::cin >> searchkey;
    std::cout << std::endl << std::boolalpha << tree->Search(searchkey);
    return 0;
}
