// https://leetcode.com/problems/add-two-numbers-ii/

#include "data_structures.h"

int list_len(ListNode* cur) {
    int size = 0;
    while (cur) {
        cur = cur->next;
        size++;
    }
    return size;
}

ListNode* left_pad_by(ListNode* head, int extension_size) {
    ListNode* cur = head;
    for (int i = 0; i < extension_size; ++i) {
        ListNode* next = new ListNode();
        next->next = cur;
        cur = next;
    }

    return cur;
}

int build_sum(ListNode* sum, ListNode* l1, ListNode* l2) {
    if (l1 == nullptr || l2 == nullptr) {
        return 0;
    }

    ListNode* next_digit = (l1->next || l2->next) ? new ListNode : nullptr;
    sum->next = next_digit;

    int carry = build_sum(sum->next, l1->next, l2->next);

    sum->val = l1->val + l2->val + carry;
    if (sum->val < 10) {
        return 0;
    }

    sum->val -= 10;
    return 1;
}

class Solution {
  public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int l1_len = list_len(l1);
        int l2_len = list_len(l2);
        if (l1_len > l2_len) {
            l2 = left_pad_by(l2, (l1_len - l2_len));
        }
        if (l2_len > l1_len) {
            l1 = left_pad_by(l1, (l2_len - l1_len));
        }

        ListNode* sum = new ListNode();
        if (build_sum(sum, l1, l2) == 0) {
            return sum;
        }

        ListNode* head = new ListNode(1);
        head->next = sum;

        return head;
    }
};

int main(void) {
    Solution solution;


    ListNode* l1_case1 = new ListNode({7, 2, 4, 3});
    ListNode* l2_case1 = new ListNode({5, 6, 4});

    std::cout << l1_case1 << std::endl;
    std::cout << l2_case1 << std::endl;

    std::cout << solution.addTwoNumbers(l1_case1, l2_case1) << std::endl;

    std::cout << "-----" << std::endl;

    ListNode* l1_case2 = new ListNode({9, 9, 9});
    ListNode* l2_case2 = new ListNode({9, 9, 9});

    std::cout << l1_case2 << std::endl;
    std::cout << l2_case2 << std::endl;

    std::cout << solution.addTwoNumbers(l1_case2, l2_case2) << std::endl;


    return 0;
}
