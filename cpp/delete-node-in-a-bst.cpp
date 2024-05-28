// https://leetcode.com/problems/delete-node-in-a-bst/

#include "data_structures.h"

class Solution {
  public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (root == nullptr) {
            return root;
        }

        if (root->val > key) {
            root->left = deleteNode(root->left, key);
        } else if (root->val < key) {
            root->right = deleteNode(root->right, key);
        } else {
            if (root->left == nullptr) {
                return root->right;
            } else if (root->right == nullptr) {
                return root->left;
            } else {
                root->val = find_min(root->right);
                root->right = deleteNode(root->right, root->val);
            }
        }

        return root;
    }

  private:
    int find_min(TreeNode* root) {
        return (!root->left) ? root->val : find_min(root->left);
    }
};

int main(void) {
    TreeNode* case1 = new TreeNode(5);
    case1->left = new TreeNode(3);
    case1->right = new TreeNode(6);
    case1->left->left = new TreeNode(2);
    case1->left->right = new TreeNode(4);
    case1->right->right = new TreeNode(7);
    Solution solution;

    solution.deleteNode(case1, 7);


    return 0;
}
