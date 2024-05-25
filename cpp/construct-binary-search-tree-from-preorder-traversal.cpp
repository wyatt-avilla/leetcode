// https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

#include "data_structures.h"

#include <vector>

class Solution {
  public:
    TreeNode* bstFromPreorder(std::vector<int>& preorder) {
        return construct_bst_rec(preorder, 0, preorder.size());
    }

  private:
    TreeNode* construct_bst_rec(std::vector<int>& preorder, int l, int r) {
        if (r - l <= 0) {
            return nullptr;
        }

        int division_point = r;
        for (int i = l + 1; i < r; ++i) {
            if (preorder[i] > preorder[l]) {
                division_point = i;
                break;
            }
        }

        return new TreeNode(preorder[l],
                            construct_bst_rec(preorder, l + 1, division_point),
                            construct_bst_rec(preorder, division_point, r));
    }
};

void preorder_print(TreeNode* root) {
    if (root == nullptr) {
        return;
    }
    std::cout << root->val << " ";
    preorder_print(root->left);
    preorder_print(root->right);
}

int main(void) {
    Solution solution;

    std::vector<int> case_1 = {8, 5, 1, 7, 10, 12};
    TreeNode* case_1_ans = solution.bstFromPreorder(case_1);
    preorder_print(case_1_ans);
    std::cout << std::endl;

    std::vector<int> case_2 = {8, 7, 6, 5, 4, 3};
    TreeNode* case_2_ans = solution.bstFromPreorder(case_2);
    preorder_print(case_2_ans);
    std::cout << std::endl;

    return 0;
}
