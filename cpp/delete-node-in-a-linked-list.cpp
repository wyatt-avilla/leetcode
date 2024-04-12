// https://leetcode.com/problems/delete-node-in-a-linked-list/

#include "data_structures.h"

class Solution {
  public:
    void deleteNode(ListNode* head) {
        head->val = head->next->val;
        head->next = head->next->next;
    }
};

int main(void) {
    Solution solution;

    ListNode* l = new ListNode(
        1, new ListNode(2, new ListNode(2, new ListNode(1, nullptr))));
    solution.deleteNode(l->next);
    std::cout << l << std::endl;

    std::cout << "----" << std::endl;

    ListNode* l2 = new ListNode(1, new ListNode(2, nullptr));
    solution.deleteNode(l2);
    std::cout << l2 << std::endl;

    return 0;
}
