// https://leetcode.com/problems/palindrome-linked-list/

#include "data_structures.h"

#include <cassert>

bool isPalindromeRec(ListNode** left, ListNode* right) {
    if (right == nullptr) {
        return true;
    }
    bool sub_res = isPalindromeRec(left, right->next);
    if ((*left)->val != right->val) {
        return false;
    }
    (*left) = (*left)->next;
    return true && sub_res;
}

class Solution {
  public:
    bool isPalindrome(ListNode* head) {
        return isPalindromeRec(&head, head->next);
    }
};

int main(void) {
    Solution solution;

    ListNode* l = new ListNode(
        1, new ListNode(2, new ListNode(2, new ListNode(1, nullptr))));
    assert(solution.isPalindrome(l));

    std::cout << "----" << std::endl;

    ListNode* l2 = new ListNode(1, new ListNode(2, nullptr));
    assert(solution.isPalindrome(l2) == false);

    return 0;
}
