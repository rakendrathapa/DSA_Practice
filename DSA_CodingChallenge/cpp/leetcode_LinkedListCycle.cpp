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

    ListNode *detectCycle(ListNode *head) {
        if(head == nullptr){
            return nullptr;
        }
        if(head->next == nullptr){
            return nullptr;
        }
        if(head->next == head){
            return head;
        }

        ListNode* slow = head;
        ListNode* fast = head->next;
        ListNode* cycleNode = nullptr;

        while(true){

            if((fast == nullptr) || (fast->next == nullptr)){
                return nullptr;
            }

            if((fast->next == slow) || (fast->next->next == slow)){
                cycleNode = slow;
                break;
            }
            slow = slow->next;
            fast = fast->next->next;
        }

        return cycleNode;
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
            if(count == 0){
                head = new ListNode(*it);
                node = head;
            }else{
                node->next = new ListNode(*it);
                node = node->next;
            }

            if(count == pos){
                cycleNode = node;
            }

            it++;
            count++;
        }

        if(cycleNode != nullptr){
            node->next = cycleNode;
            fprintf(stdout, "cycleNode:%p\t", cycleNode);
        }else{
            fprintf(stdout, "cycleNode:nullptr\t");
        }

        return true;
    }
};

int main()
{
    pair<vector<int>, int> t1, t2, t3, t4, t5, t6;
    Solution s;
    t1 = make_pair(vector<int>{3,2,0,-4}, 1);
    t2 = make_pair(vector<int>{1,2}, 0);
    t3 = make_pair(vector<int>{1}, -1);
    t4 = make_pair(vector<int>{1}, 0);
    t5 = make_pair(vector<int>{-1,-7,7,-4,19,6,-9,-5,-2,-5}, 9);
    t6 = make_pair(vector<int>{-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5}, 24);

    vector<pair<vector<int>, int> >test_vector {t1, t2, t3, t4, t5, t6};
    vector<pair<vector<int>, int> >::const_iterator cit = test_vector.begin();

    while(cit != test_vector.end())
    {
        ListNode* head = nullptr;
        if(false == s.CreateLinkedList(*cit, head)){
            cerr << "Error: Unable to create Linked List" << endl;
            break;
        }

        // s.PrintLinkedList(head);
        /*
        if(s.hasCycle(head)){
            cout << "true" << endl;
        }else{
            cout << "false" << endl;
        }
        */

        ListNode *node = s.detectCycle(head);
        if(node == nullptr){
            fprintf(stdout, "Found:nullptr\n");
        }else{
            fprintf(stdout, "Found:%p\n", node);
        }
        cit++;
    }
}

