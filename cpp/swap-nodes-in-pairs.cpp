// https://leetcode.com/problems/swap-nodes-in-pairs/

#include "data_structures.h"

class Solution {
  public:
    ListNode* swapPairs(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* left = head;
        ListNode* right = (head) ? head->next : nullptr;

        while (left && right) {
            left->next = right->next;
            right->next = left;

            if (prev) {
                prev->next = right;
            } else {
                head = right;
            }

            prev = left;
            left = left->next;
            right = (left) ? left->next : nullptr;
        }

        return head;
    }
};

int main(void) {
    Solution solution;

    ListNode* l1 = new ListNode({1, 2, 3, 4});
    std::cout << l1 << std::endl;
    std::cout << solution.swapPairs(l1) << std::endl;

    std::cout << "-----" << std::endl;

    ListNode* l2 = new ListNode();
    std::cout << l2 << std::endl;
    std::cout << solution.swapPairs(l2) << std::endl;

    return 0;
}
