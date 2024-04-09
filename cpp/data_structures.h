#include <iostream>

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}

    friend std::ostream& operator<<(std::ostream& os, const ListNode* node) {
        while (node != nullptr) {
            os << node->val;
            if (node->next != nullptr) {
                os << " -> ";
            }
            node = node->next;
        }
        return os;
    }
};
