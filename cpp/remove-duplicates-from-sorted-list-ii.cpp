// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

#include "data_structures.h"

class Solution {
  public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        ListNode* prev = nullptr;
        ListNode* cur = head;
        while (cur != nullptr && cur->next != nullptr) {
            if (cur->val != cur->next->val) {
                prev = cur;
                cur = cur->next;
                continue;
            }

            int checking_for = cur->val;
            while (cur != nullptr) {
                if (checking_for != cur->val) {
                    break;
                }
                cur = cur->next;
            }

            (prev == nullptr) ? head = cur : prev->next = cur;
        }

        return head;
    }
};

int main(void) {
    Solution solution;

    ListNode* l1 = new ListNode({1, 2, 3, 3, 4, 4, 5});
    ListNode* l1_exp = new ListNode({1, 2, 5});
    std::cout << l1 << std::endl;
    std::cout << solution.deleteDuplicates(l1) << std::endl;

    std::cout << "-----" << std::endl;

    ListNode* l2 = new ListNode({1, 1, 1, 2, 3});
    ListNode* l2_exp = new ListNode({2, 3});
    std::cout << l2 << std::endl;
    std::cout << solution.deleteDuplicates(l2) << std::endl;

    std::cout << "-----" << std::endl;

    return 0;
}
