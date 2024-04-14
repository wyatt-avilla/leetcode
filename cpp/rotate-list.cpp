// https://leetcode.com/problems/rotate-list/

#include "data_structures.h"

class Solution {
  public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        int list_len = 0;
        for (ListNode* temp = head; temp != nullptr; temp = temp->next) {
            list_len++;
        }

        k %= list_len;

        if (k == 0) {
            return head;
        }

        ListNode* cur = head;
        for (int i = 0; i < (list_len - k - 1); ++i) {
            cur = cur->next;
        }

        ListNode* old_head = head;
        head = cur->next;
        cur->next = nullptr;

        cur = head;
        while (cur->next) {
            cur = cur->next;
        }

        cur->next = old_head;


        return head;
    }
};


int main(void) {
    Solution solution;

    ListNode* l1 = new ListNode({1, 2, 3, 4, 5});
    std::cout << l1 << std::endl;
    std::cout << solution.rotateRight(l1, 2) << std::endl;

    std::cout << "-----" << std::endl;

    ListNode* l2 = new ListNode({0, 1, 2});
    std::cout << l2 << std::endl;
    std::cout << solution.rotateRight(l2, 4) << std::endl;

    std::cout << "-----" << std::endl;

    ListNode* l3 = new ListNode({0, 1, 2});
    std::cout << l3 << std::endl;
    std::cout << solution.rotateRight(l3, 0) << std::endl;

    std::cout << "-----" << std::endl;

    ListNode* l4 = new ListNode({1});
    std::cout << l4 << std::endl;
    std::cout << solution.rotateRight(l4, 1) << std::endl;

    std::cout << "-----" << std::endl;

    ListNode* l5 = new ListNode({1, 2});
    std::cout << l5 << std::endl;
    std::cout << solution.rotateRight(l5, 2) << std::endl;


    return 0;
}
