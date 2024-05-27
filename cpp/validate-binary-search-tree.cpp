// https://leetcode.com/problems/validate-binary-search-tree/

#include "data_structures.h"

#include <cassert>
#include <limits>

class Solution {
  public:
    bool isValidBST(TreeNode* root) {
        if (root == nullptr) {
            return true;
        } else {
            return dfs(root, std::numeric_limits<long>::min(),
                       std::numeric_limits<long>::max());
        }
    }

  private:
    bool dfs(TreeNode* root, long start, long end) {
        if (root == nullptr) {
            return true;
        } else {
            return root->val > start && root->val < end &&
                   dfs(root->left, start, root->val) &&
                   dfs(root->right, root->val, end) &&
                   ((root->left) ? root->left->val < root->val : true) &&
                   ((root->right) ? root->right->val > root->val : true);
        }
    }
};

int main(void) {
    Solution solution;

    TreeNode* head = new TreeNode(5);
    head->left = new TreeNode(4);
    head->right = new TreeNode(8);
    // head->left->right = new TreeNode(8);
    head->right->left = new TreeNode(6);
    head->right->right = new TreeNode(9);
    // head->right->left->left = new TreeNode(3);
    head->right->left->right = new TreeNode(7);

    assert(solution.isValidBST(head));

    return 0;
}
