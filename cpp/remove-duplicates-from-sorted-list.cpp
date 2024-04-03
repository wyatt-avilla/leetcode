// https://leetcode.com/problems/remove-duplicates-from-sorted-list/

#include "data_structures.h"

class Solution {
  public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* cur = head;
        while (cur != nullptr && cur->next != nullptr) {
            if (cur->val == cur->next->val) {
                cur->next = cur->next->next;
                continue;
            }
            cur = cur->next;
        }
        return head;
    }
};
