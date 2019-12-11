/**
 * PROBLEM NAME: Easy Subsequence Selection
 * You are given a string S with length N. Choose an integer K and two non-empty subsequences A and B
 * of characters of this string, each with length K, such that:
 * A=B, i.e. for each valid i, the i-th character in A is the same as the i-th character in B.
 * Let's denote the indices of characters used to construct A by a1,a2,…,aK, i.e. A=(Sa1,Sa2,…,SaK).
 * Similarly, let's denote the indices of characters used to construct B by b1,b2,…,bK.
 * If we denote the number of common indices in the sequences a and b by M, then M+1≤K.
 *
 * Input
 * The first line of the input contains a single integer T denoting the number of test cases.
 * The description of T test cases follows.
 * The first line of each test case contains a single integer N.
 * The second line contains a single string S with length N.
 *
 * Output
 * For each test case, print a single line containing one integer ― the maximum K,
 * or 0 if there is no solution.
 *
 * Constraints
 * 1≤T≤100
 * 1≤N≤105
 * S contains only lowercase English letters
 *
 * Example Input
 * 1
 * 4
 * anxa
 * Example Output
 * 1
 **/
#include <iostream>
#include <vector>
#include <string>

using namespace std;

extern int GetMaxSubStringLen(const string&);
int main()
{
    int t=0, l=0;
    string input;

    cin >> t;
    for (int i=0; i<t; i++){
        cin >> l;
        cin >> input;
        int n = GetMaxSubStringLen(input);
        cout << n << endl;
    }
    return 0;
}

class Tree;
class Node{
private:
    char data;
    vector<char>* childChars;
    friend class Tree;
public:
    Node(char data, vector<char> *childs=nullptr)
    {
        this->data = data;
        this->childChars = childs;
    }
};

class Tree
{
private:
    Node* rootNode;
    vector<char>* rootChild;
public:
    Tree(int data)
    {
        rootChild = new vector<char>();
        rootNode = new Node(data, rootChild);
    }
    ~Tree(){
        if(rootNode){
            delete rootNode;
        }
        if(rootChild){
            delete rootChild;
        }
    }

    int Insert(int data)
    {
        Node *node = rootNode;
        int count = 0;
        if(data == node->data){
            return ++count;
        }


    }
};

int GetMaxSubStringLen(const string& input)
{
    int maxVal = 0, insertCost = 0;
    string::const_iterator it = input.begin();
    Tree tree(*it);
    while(it != input.end())
    {
        insertCost = tree.Insert(*it++);
        if(maxVal < insertCost){maxVal = insertCost;}
    }
    return maxVal;
}
