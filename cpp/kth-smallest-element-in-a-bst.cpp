#include "data_structures.h"

#include <stack>

class Solution {
  public:
    int kthSmallest(TreeNode* root, int k) {
        std::stack<TreeNode*> stack;
        stack.push(root);

        int num_popped = 0;
        TreeNode* curr_node = stack.top();
        while (!stack.empty()) {
            if (curr_node == nullptr) {
                curr_node = stack.top();
                stack.pop();

                if (++num_popped == k) {
                    return curr_node->val;
                } else {
                    curr_node = curr_node->right;
                }

            } else {

                stack.push(curr_node);
                curr_node = curr_node->left;
            }
        }

        return -1;
    }
};

int main(void) {
    Solution solution;

    TreeNode* case1 = new TreeNode(5);
    case1->left = new TreeNode(3);
    case1->right = new TreeNode(6);
    case1->left->left = new TreeNode(2);
    case1->left->right = new TreeNode(4);
    case1->left->left->left = new TreeNode(1);

    solution.kthSmallest(case1, 3);

    return 0;
}
