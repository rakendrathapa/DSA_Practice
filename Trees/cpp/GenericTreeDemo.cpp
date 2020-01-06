#include <stdio.h>
#include <string>
#include "GenericTree.h"

using namespace std;

typedef Tree<string> StringTree;
typedef StringTree::Node StringNode;

// Printing Nodes
void PrintNode(StringNode node, int nLevel)
{
    // Print new line
    fputs("\n", stdout);
    string s;
    s.resize(nLevel*2, ' ');
    fputs(s.c_str(), stdout);

    // print the value
    std::cout << node.GetData().GetData();
    // fputs(node.GetData()->c_str(), stdout);

    // iterate through children
    nLevel++;
    for(int n=0; n<node.GetCount(); n++){
        PrintNode(node.GetNodes(n), nLevel);
    }
}

int main(int argc, char* argv[])
{
    // Define the tree
    StringTree tree;
    (string&)tree = "Root";

    // Add few nodes
    StringNode node = tree;

    node.AddNode("1").AddNode("11");
    StringNode node2=node.AddNode("2");

    node2.AddNode("21").AddNode("211");
    node2.AddNode("22");
    node2.AddNode("23");

    node.AddNode("3");

    // Print the tree
    PrintNode(tree, 0);

    // Wait for enter
    char buf[3];
    fputs("\nPress ENTER :", stdout);
    fgets(buf, 3, stdin);
    return EXIT_SUCCESS;
}
