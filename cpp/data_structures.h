#include <iostream>

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
    ListNode(std::initializer_list<int> values) : val(0), next(nullptr) {
        ListNode* current = this;
        for (int value : values) {
            current->val = value;
            if (value != *(values.end() - 1)) {
                current->next = new ListNode();
                current = current->next;
            }
        }
    }

    bool operator==(const ListNode& other) const {
        const ListNode* currentThis = this;
        const ListNode* currentOther = &other;

        while (currentThis != nullptr && currentOther != nullptr) {
            if (currentThis->val != currentOther->val) {
                return false;
            }
            currentThis = currentThis->next;
            currentOther = currentOther->next;
        }

        return currentThis == nullptr && currentOther == nullptr;
    }

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
