// https://leetcode.com/problems/reverse-linked-list-ii/

#include "data_structures.h"

class Solution {
  public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (left == right == 1) {
            return head;
        }
        ListNode* lower_connection_l = nullptr;
        ListNode* upper_connection_l = nullptr;

        size_t count = 1;
        ListNode* cur = head;
        ListNode* prev = nullptr;
        ListNode* next = nullptr;
        while (cur != nullptr) {
            next = cur->next;

            if (count == left) {
                lower_connection_l = prev;
                upper_connection_l = cur;
            }
            if (count == right) {
                if (lower_connection_l == nullptr) {
                    head = cur;
                } else {
                    lower_connection_l->next = cur;
                }
                upper_connection_l->next = next;
            }
            if (count >= left && count <= right) {
                cur->next = prev;
            }

            prev = cur;
            cur = next;
            count += 1;
        }

        return head;
    }
};

int main(int argc, char* argv[]) {
    Solution solution;

    ListNode* l = new ListNode(
        1, new ListNode(
               2, new ListNode(3, new ListNode(4, new ListNode(5, nullptr)))));
    std::cout << l << std::endl;
    std::cout << solution.reverseBetween(l, 3, 5) << std::endl;

    ListNode* l2 = new ListNode(3, new ListNode(5, nullptr));
    std::cout << l2 << std::endl;
    std::cout << solution.reverseBetween(l2, 1, 2) << std::endl;

    ListNode* l3 = new ListNode(3, new ListNode(5, nullptr));
    std::cout << l3 << std::endl;
    std::cout << solution.reverseBetween(l3, 1, 1) << std::endl;


    return 0;
}
