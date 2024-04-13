// https://leetcode.com/problems/reverse-nodes-in-even-length-groups/

#include "data_structures.h"

#include <cassert>

class Solution {
  public:
    ListNode* reverseEvenLengthGroups(ListNode* head) {
        int natural = 1;
        int group_len;

        ListNode* prev = head;
        ListNode* cur = head->next;

        ListNode* lower_conn_l;
        ListNode* upper_conn_l;

        while (cur) {
            lower_conn_l = prev;
            natural += 1;
            group_len = 0;

            for (int i = 0; i < natural; ++i) {
                if (cur == nullptr) {
                    break;
                }
                group_len += 1;
                prev = cur;
                cur = cur->next;
            }

            if (group_len % 2 != 0) {
                continue;
            }

            prev = lower_conn_l;
            cur = prev->next;

            upper_conn_l = cur;

            for (int i = 0; i < group_len; ++i) {
                ListNode* next = cur->next;
                cur->next = prev;
                prev = cur;
                cur = next;
            }

            lower_conn_l->next = prev;
            upper_conn_l->next = cur;

            prev = upper_conn_l;
        }

        return head;
    }
};


int main(void) {
    Solution solution;

    ListNode* l1 = new ListNode({5, 2, 6, 3, 9, 1, 7, 3, 8, 4});
    std::cout << l1 << std::endl;

    ListNode* l1_res = solution.reverseEvenLengthGroups(l1);
    std::cout << l1_res << std::endl;

    std::cout << "-----" << std::endl;

    ListNode* l2 = new ListNode({1, 1, 0, 6});
    std::cout << l2 << std::endl;

    ListNode* l2_res = solution.reverseEvenLengthGroups(l2);
    std::cout << l2_res << std::endl;

    std::cout << "-----" << std::endl;

    ListNode* l3 = new ListNode({1, 2, 0, 6, 5});
    std::cout << l3 << std::endl;

    ListNode* l3_res = solution.reverseEvenLengthGroups(l3);
    std::cout << l3_res << std::endl;

    std::cout << "-----" << std::endl;

    ListNode* l4 = new ListNode({9,  9,  3,  8, 14, 15, 13, 14, 15, 19,
                                 0,  12, 13, 5, 17, 20, 19, 1,  14, 12,
                                 13, 2,  2,  0, 15, 19, 8,  6,  3,  15});

    ListNode* l4_exp = new ListNode({9,  3,  9,  8, 14, 15, 19, 15, 14, 13,
                                     0,  12, 13, 5, 17, 13, 12, 14, 1,  19,
                                     20, 2,  2,  0, 15, 19, 8,  6,  15, 3});

    std::cout << l4 << std::endl;
    ListNode* l4_res = solution.reverseEvenLengthGroups(l4);
    std::cout << l4_res << std::endl;

    assert(l4_res == l4_exp);

    std::cout << "-----" << std::endl;


    return 0;
}
