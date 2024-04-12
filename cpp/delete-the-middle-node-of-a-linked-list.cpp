// https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

#include "data_structures.h"

class Solution {
  public:
    ListNode* deleteMiddle(ListNode* head) {
        ListNode* slow;
        ListNode* fast;
        slow = fast = head;

        while (fast != nullptr && fast->next != nullptr) {
            fast = fast->next->next;
            slow = slow->next;
        }

        if (slow->next != nullptr) {
            slow->val = slow->next->val;
            slow->next = slow->next->next;
        } else {
            head->next == nullptr ? head = nullptr : head->next = nullptr;
        }

        return head;
    }
};

int main(void) {
    Solution solution;

    ListNode* l = new ListNode(
        1, new ListNode(2, new ListNode(3, new ListNode(4, nullptr))));
    std::cout << l << std::endl;
    solution.deleteMiddle(l);
    std::cout << l << std::endl;

    std::cout << "----" << std::endl;

    ListNode* l2 = new ListNode(
        1, new ListNode(
               2, new ListNode(3, new ListNode(4, new ListNode(5, nullptr)))));
    std::cout << l2 << std::endl;
    solution.deleteMiddle(l2);
    std::cout << l2 << std::endl;

    std::cout << "----" << std::endl;

    ListNode* l3 = new ListNode(2, new ListNode(1, nullptr));
    std::cout << l3 << std::endl;
    solution.deleteMiddle(l3);
    std::cout << l3 << std::endl;

    std::cout << "----" << std::endl;

    ListNode* l4 = new ListNode(5, nullptr);
    std::cout << l4 << std::endl;
    if (solution.deleteMiddle(l4) == nullptr) {
        std::cout << "null" << std::endl;
    }


    return 0;
}
