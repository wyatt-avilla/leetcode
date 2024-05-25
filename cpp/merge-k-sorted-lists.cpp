// https://leetcode.com/problems/merge-k-sorted-lists/

#include "data_structures.h"

#include <vector>

class Solution {
  public:
    ListNode* mergeKLists(std::vector<ListNode*>& lists) {
        ListNode* head = new ListNode();
        ListNode* curr = head;

        int min_idx;
        while (1) {
            min_idx = -1;
            for (int i = 0; i < lists.size(); ++i) {
                if (lists[i] == nullptr) {
                    continue;
                } else if (min_idx == -1) {
                    min_idx = i;
                } else if (lists[i]->val < lists[min_idx]->val) {
                    min_idx = i;
                }
            }
            if (min_idx == -1) {
                break;
            }

            curr->next = lists[min_idx];
            curr = curr->next;
            lists[min_idx] = lists[min_idx]->next;
        }
        return head->next;
    }
};

int main(void) {
    Solution solution;
    std::vector<ListNode*> lists_1;
    lists_1.push_back(new ListNode{1, 4, 5});
    lists_1.push_back(new ListNode{1, 3, 4});
    lists_1.push_back(new ListNode{2, 6});

    std::cout << solution.mergeKLists(lists_1) << std::endl;

    return 0;
}
