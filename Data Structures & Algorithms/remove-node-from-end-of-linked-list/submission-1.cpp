/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int size = 0;
        ListNode* prun = head;
        ListNode* del_node;

        while(prun)
        {
            size += 1;
            prun = prun -> next;
        }

        if(size == 1)
        {
            delete head;
            return nullptr;
        }

        if (size == n) {
            del_node = head;
            head = head->next;
            delete del_node;
            return head;
        }

        prun = head;

        for(int i = 0; i < size - n - 1; ++i)
        {
            prun = prun -> next;
        }

        del_node = prun -> next;
        prun -> next = prun -> next -> next;
        delete del_node;

        return head;
    }
};
