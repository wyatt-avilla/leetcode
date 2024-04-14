// https://leetcode.com/problems/merge-nodes-in-between-zeros/

#include "data_structures.h"

int sum_and_merge(ListNode* cur) {
    if (cur->val == 0) {
        return 0;
    }

    int sum = sum_and_merge(cur->next);

    sum += cur->val;
    cur->next = cur->next->next;

    return sum;
}

class Solution {
  public:
    ListNode* mergeNodes(ListNode* head) {
        ListNode* cur = head->next;

        while (cur) {
            int sum = sum_and_merge(cur);
            cur->val = sum;
            cur = cur->next;
        }

        return head->next;
    }
};

int main(void) {
    Solution solution;

    ListNode* l1 = new ListNode({0, 3, 1, 0, 4, 5, 2, 0});
    std::cout << l1 << std::endl;
    std::cout << solution.mergeNodes(l1) << std::endl;

    ListNode* l2 = new ListNode({0, 1, 0, 3, 0, 2, 2, 0});
    std::cout << l2 << std::endl;
    std::cout << solution.mergeNodes(l2) << std::endl;

    ListNode* l3 = new ListNode({0, 1, 0});
    std::cout << l3 << std::endl;
    std::cout << solution.mergeNodes(l3) << std::endl;

    return 0;
}
