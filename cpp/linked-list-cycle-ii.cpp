// https://leetcode.com/problems/linked-list-cycle-ii/

#include "data_structures.h"

class Solution {
  public:
    ListNode* detectCycle(ListNode* head) {
        ListNode* intersect = intersection(head);
        if (intersect == nullptr) {
            return nullptr;
        }

        while (head != intersect) {
            head = head->next;
            intersect = intersect->next;
        }

        return head;
    }

  private:
    ListNode* intersection(ListNode* head) {
        if (head == nullptr) {
            return nullptr;
        }
        ListNode* slow = head;
        ListNode* fast = head;

        while (slow && fast) {
            slow = slow->next;
            fast = (fast->next) ? fast->next->next : nullptr;

            if (slow == fast) {
                return slow;
            }
        }
        return nullptr;
    }
};
