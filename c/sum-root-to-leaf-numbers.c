// https://leetcode.com/problems/sum-root-to-leaf-numbers/

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

void traverse(struct TreeNode* currentNode, int buildingSum, int* treeSum) {
    if (!currentNode->left && !currentNode->right) {
        *treeSum += (buildingSum * 10 + currentNode->val);
    } else {
        if (currentNode->left) {
            traverse(currentNode->left, (buildingSum * 10) + currentNode->val,
                     treeSum);
        }
        if (currentNode->right) {
            traverse(currentNode->right, (buildingSum * 10) + currentNode->val,
                     treeSum);
        }
    }
}

int sumNumbers(struct TreeNode* root) {
    int sum;
    int* treeSum = calloc(1, sizeof(int));

    traverse(root, 0, treeSum);

    sum = *treeSum;
    free(treeSum);
    return sum;
}

struct TreeNode* genNode(int val) {
    struct TreeNode* node = malloc(sizeof(struct TreeNode));
    node->val = val;
    node->left = NULL;
    node->right = NULL;
    return node;
}

int main() {

    struct TreeNode* root = genNode(4);
    root->left = genNode(9);
    root->right = genNode(1);
    root->left->left = genNode(2);
    printf("returned: %d\n", sumNumbers(root));

    free(root->left->left);
    free(root->right);
    free(root->left);
    free(root);
}
