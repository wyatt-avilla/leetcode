// https://leetcode.com/problems/remove-linked-list-elements/

#include "data_structures.h"

class Solution {
  public:
    ListNode* removeElements(ListNode* head, int val) {
        while (head && head->val == val) {
            head = head->next;
        }

        ListNode* cur = head;
        while (cur && cur->next) {
            if (cur->next->val == val) {
                cur->next = cur->next->next;
                continue;
            }
            cur = cur->next;
        }

        return head;
    }
};


int main(void) {
    Solution solution;

    ListNode* l1 = new ListNode({1, 2, 6, 3, 4, 5, 6});
    std::cout << l1 << std::endl;
    ListNode* l1_res = solution.removeElements(l1, 6);
    std::cout << l1_res << std::endl;

    std::cout << "-----" << std::endl;

    ListNode* l2 = new ListNode({7, 7});
    std::cout << l2 << std::endl;
    ListNode* l2_res = solution.removeElements(l2, 7);
    std::cout << l2_res << std::endl;

    std::cout << "-----" << std::endl;

    ListNode* l3 = new ListNode({1, 2, 2, 1});
    std::cout << l3 << std::endl;
    ListNode* l3_res = solution.removeElements(l3, 2);
    std::cout << l3_res << std::endl;

    return 0;
}
