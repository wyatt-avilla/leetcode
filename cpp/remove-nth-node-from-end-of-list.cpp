// https://leetcode.com/problems/remove-nth-node-from-end-of-list/

#include "data_structures.h"

int delete_nth_last(ListNode* cur, int n) {
    if (cur == nullptr) {
        return 0;
    }
    int current_depth = delete_nth_last(cur->next, n) + 1;
    if (current_depth == (n + 1)) {
        cur->next = cur->next->next;
    }
    return current_depth;
}

class Solution {
  public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head->next == nullptr) {
            return nullptr;
        }
        if (delete_nth_last(head, n) == n) {
            return head->next;
        }
        return head;
    }
};

int main(void) {
    Solution solution;

    ListNode* l1_in = new ListNode({1, 2, 3, 4, 5});
    ListNode* l1_exp = new ListNode({1, 2, 3, 5});

    std::cout << l1_exp << std::endl;
    std::cout << solution.removeNthFromEnd(l1_in, 2) << std::endl;

    std::cout << "----" << std::endl;


    ListNode* l2_in = new ListNode({1});

    solution.removeNthFromEnd(l2_in, 1);

    std::cout << l2_in << std::endl;
    std::cout << "nullptr" << std::endl;

    std::cout << "----" << std::endl;


    ListNode* l3_in = new ListNode({1, 2});
    ListNode* l3_exp = new ListNode({1});

    std::cout << l3_exp << std::endl;
    std::cout << solution.removeNthFromEnd(l3_in, 1) << std::endl;


    std::cout << "----" << std::endl;

    ListNode* l4_in = new ListNode({1, 2});
    ListNode* l4_exp = new ListNode({2});

    std::cout << l4_exp << std::endl;
    std::cout << solution.removeNthFromEnd(l4_in, 2) << std::endl;


    return 0;
}
