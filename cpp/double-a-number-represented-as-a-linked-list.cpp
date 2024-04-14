// https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

#include "data_structures.h"

int double_list(ListNode* cur) {
    if (cur == nullptr) {
        return 0;
    }

    int carry = double_list(cur->next);
    cur->val *= 2;
    cur->val += carry;

    if (cur->val < 10) {
        return 0;
    }

    cur->val -= 10;
    return 1;
}

class Solution {
  public:
    ListNode* doubleIt(ListNode* head) {
        int carry = double_list(head);

        if (carry == 0) {
            return head;
        }

        ListNode* new_head = new ListNode(1);
        new_head->next = head;
        return new_head;
    }
};

int main(void) {
    Solution solution;

    ListNode* l1 = new ListNode({1, 8, 9});
    std::cout << l1 << std::endl;
    std::cout << solution.doubleIt(l1) << std::endl;

    std::cout << "-----" << std::endl;

    ListNode* l2 = new ListNode({9, 9, 9});
    std::cout << l2 << std::endl;
    std::cout << solution.doubleIt(l2) << std::endl;

    return 0;
}
