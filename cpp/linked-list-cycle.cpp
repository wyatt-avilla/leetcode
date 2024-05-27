// https://leetcode.com/problems/linked-list-cycle/

#include "data_structures.h"

class Solution {
  public:
    bool hasCycle(ListNode* head) {
        if (!head || !head->next) {
            return false;
        }
        ListNode* slow = head;
        ListNode* fast = head->next;

        while (slow && fast) {
            if (slow == fast) {
                return true;
            }
            slow = slow->next;
            fast = (fast->next) ? fast->next->next : nullptr;
        }
        return false;
    }
};
