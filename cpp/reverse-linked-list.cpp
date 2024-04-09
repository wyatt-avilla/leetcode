// https://leetcode.com/problems/reverse-linked-list/

#include "data_structures.h"

#include <iostream>

void print_list(ListNode* head) {
    ListNode* cur = head;
    while (cur != nullptr) {
        std::cout << cur->val << " ";
        cur = cur->next;
    }
    std::cout << std::endl;
}

class Solution {
  public:
    ListNode* reverseList(ListNode* head) {
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
};


int main(int argc, char* argv[]) {
    Solution solution;

    ListNode* l = new ListNode;
    l->val = 1;

    l->next = new ListNode;
    l->next->val = 2;

    l->next->next = new ListNode;
    l->next->next->val = 3;

    print_list(l);
    solution.reverseList(l);
    print_list(l);

    return 0;
}
