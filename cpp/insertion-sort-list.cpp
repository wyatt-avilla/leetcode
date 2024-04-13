// https://leetcode.com/problems/insertion-sort-list/

#include "data_structures.h"

bool rec_insert(ListNode* cur, int val, int sub_len) {
    if (sub_len == 0) {
        return false;
    }

    if (rec_insert(cur->next, val, --sub_len)) {
        return true;
    }

    if (cur->val <= val) {
        cur->next->val = val;
        return true;
    }

    cur->next->val = cur->val; // shift right
    return false;
}

class Solution {
  public:
    ListNode* insertionSortList(ListNode* head) {

        int sub_len = 0;
        for (ListNode* cur = head; cur != nullptr; cur = cur->next) {

            int key = cur->val;

            if (!rec_insert(head, key, sub_len++)) {
                head->val = key;
            }
        }

        return head;
    }
};

int main(void) {

    Solution solution;

    ListNode* l1 = new ListNode({4, 2, 1, 3});
    std::cout << l1 << std::endl;
    std::cout << solution.insertionSortList(l1) << std::endl;

    std::cout << "-----" << std::endl;

    ListNode* l2 = new ListNode({-1, 5, 3, 4, 0});
    std::cout << l2 << std::endl;
    std::cout << solution.insertionSortList(l2) << std::endl;

    return 0;
}
