#include <iostream>
#include <vector>

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
    ListNode(std::initializer_list<int> values) : val(0), next(nullptr) {
        std::vector<int> vec(values);
        ListNode* current = this;
        for (auto it = vec.begin(); it != vec.end(); ++it) {
            current->val = *it;
            if (it == vec.end() - 1) {
                break;
            }
            current->next = new ListNode();
            current = current->next;
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

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right)
        : val(x), left(left), right(right) {}
};
