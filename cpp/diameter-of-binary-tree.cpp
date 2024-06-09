// https://leetcode.com/problems/diameter-of-binary-tree/

#include "data_structures.h"

#include <algorithm>

class Solution {
  public:
    int diameterOfBinaryTree(TreeNode* root) {
        int found_diameter = 0;
        diameter(root, &found_diameter);
        return found_diameter;
    }

    int diameter(TreeNode* root, int* max_diameter) {
        if (root == nullptr) {
            return 0;
        }
        int l_height = diameter(root->left, max_diameter);
        int r_height = diameter(root->right, max_diameter);
        int current_diameter = l_height + r_height;
        *max_diameter = std::max(*max_diameter, current_diameter);
        return std::max(l_height, r_height) + 1;
    }
};
