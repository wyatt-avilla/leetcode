// https://leetcode.com/problems/reverse-linked-list/

#include "data_structures.h"

#include <iostream>

class Solution {
  public:
    ListNode* reverseList_iter(ListNode* head) {
        ListNode* new_head = nullptr;
        ListNode* cur = head;

        if (cur == nullptr) {
            return nullptr;
        }

        ListNode* prev = nullptr;
        ListNode* next = nullptr;
        while (cur != nullptr) {
            next = cur->next;
            cur->next = prev;

            prev = cur;
            cur = next;
        }
        return prev;
    }

    ListNode* reverseList_rec(ListNode* prev, ListNode* curr) {
        if (curr == nullptr) {
            return prev;
        }

        ListNode* tail = reverseList_rec(curr, curr->next);
        curr->next = prev;
        return tail;
    }

    ListNode* reverseList(ListNode* head) {
        return reverseList_rec(nullptr, head);
    }
};


int main(int argc, char* argv[]) {
    Solution solution;

    ListNode* l = new ListNode;
    l->val = 1;

    l->next = new ListNode;
    l->next->val = 2;

    l->next->next = new ListNode;
    l->next->next->val = 3;

    std::cout << l << std::endl;
    std::cout << solution.reverseList(l) << std::endl;

    return 0;
}
