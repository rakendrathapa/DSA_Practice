/**
 * Problem Name: Linked List Cycle
 * Given a linked list, determine if it has a cycle in it.
 *
 * To represent a cycle in the given linked list, we use an integer pos
 * which represents the position (0-indexed) in the linked list where tail connects to.
 * If pos is -1, then there is no cycle in the linked list
 *
 * Example 1:
 * Input: head = [3,2,0,-4], pos = 1
 * Output: true
 * Explanation: There is a cycle in the linked list, where tail connects to the second node.
 *
 * Example 2:
 * Input: head = [1,2], pos = 0
 * Output: true
 * Explanation: There is a cycle in the linked list, where tail connects to the first node.
 *
 * Example 3:
 * Input: head = [1], pos = -1
 * Output: false
 * Explanation: There is no cycle in the linked list.
 *
 * Follow up:
 * Can you solve it using O(1) (i.e. constant) memory?
 */

/** Definition for singly-linked list. */
#include <iostream>
#include <utility>
#include <vector>

using namespace std;
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head == nullptr){
            return false;
        }
        if(head->next == nullptr){
            return false;
        }
        ListNode *slow=head, *fast=head->next;
        while(fast != slow){
            if((fast == nullptr) || (fast->next == nullptr)){
                return false;
            }
            slow = slow->next;
            fast = fast->next->next;
        }
        return true;
    }
    void PrintLinkedList(ListNode* &head)
    {
        ListNode* node = head;
        while(node){
            cout << node->val << " ";
            node = node->next;
        }
        cout << endl;
    }

    bool CreateLinkedList(const pair<vector<int>, int> &input, ListNode* &head)
    {
        if(head != nullptr){
            return false;
        }

        vector<int> inputarr(input.first);
        int pos(input.second);
        ListNode* node = nullptr;
        ListNode* cycleNode = nullptr;
        int count = 0;

        vector<int>::const_iterator it = inputarr.begin();
        while(it != inputarr.end())
        {
            cout << "count:" << count << endl;
            if(count == 0){
                head = new ListNode(*it);
                node = head;
            }else{
                node->next = new ListNode(*it);
                node = node->next;
            }

            if(count == pos){
                cout << "pos:" << pos << endl;
                cycleNode = node;
            }

            it++;
            count++;
        }

        if(cycleNode != nullptr){
            node->next = cycleNode;
        }

        return true;
    }
};

int main()
{
    pair<vector<int>, int> t1, t2, t3;
    Solution s;
    t1 = make_pair(vector<int>{3,2,0,-4}, 1);
    t2 = make_pair(vector<int>{1,2}, 0);
    t3 = make_pair(vector<int>{1}, -1);

    vector<pair<vector<int>, int> >test_vector {t1, t2, t3};
    vector<pair<vector<int>, int> >::const_iterator cit = test_vector.begin();

    while(cit != test_vector.end())
    {
        ListNode* head = nullptr;
        if(false == s.CreateLinkedList(*cit, head)){
            cerr << "Error: Unable to create Linked List" << endl;
            break;
        }

        // s.PrintLinkedList(head);
        if(s.hasCycle(head)){
            cout << "true" << endl;
        }else{
            cout << "false" << endl;
        }
        cit++;
    }

    /*
    vector<int> v1 = t1.first;
    vector<int>::iterator it = v1.begin();
    while(it != v1.end()){
        cout << *it++ << endl;
    }
    */
}

