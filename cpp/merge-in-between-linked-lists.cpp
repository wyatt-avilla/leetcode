// https://leetcode.com/problems/merge-in-between-linked-lists/

#include "data_structures.h"

class Solution {
  public:
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode* aprev;
        ListNode* bprev;

        int idx = 0;
        ListNode* cur = list1;
        while (cur) {
            if (idx == a - 1) {
                aprev = cur;
            }
            if (idx == b) {
                bprev = cur;
                break;
            }

            cur = cur->next;
            ++idx;
        }

        cur = list2;
        while (cur->next) {
            cur = cur->next;
        }

        aprev->next = list2;
        cur->next = bprev->next;


        return list1;
    }
};


int main() {
    Solution solution;


    return 0;
}
