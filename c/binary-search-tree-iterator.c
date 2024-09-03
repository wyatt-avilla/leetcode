// https://leetcode.com/problems/binary-search-tree-iterator/

#include "data_structures.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

enum TraversalType {
    preorder = 2 << 0,
    inorder = 2 << 1,
    postorder = 2 << 2,
};

enum RecursionState {
    pre = 2 << 0,
    in = 2 << 1,
    post = 2 << 2,
};

typedef struct TreeSLLNode {
    struct TreeNode* data;
    enum RecursionState state;
    struct TreeSLLNode* next;
} TreeSLLNode;

typedef struct BSTIterator {
    TreeSLLNode* head;
} BSTIterator;

TreeSLLNode* new_node(struct TreeNode* data) {
    TreeSLLNode* node = malloc(sizeof(TreeSLLNode));
    node->data = data;
    node->state = pre;
    node->next = NULL;

    return node;
}

void advance_iterator(BSTIterator* obj) {
    switch (obj->head->state) {
    case post: {
        TreeSLLNode* new_head = obj->head->next;
        free(obj->head);
        obj->head = new_head;

        if (obj->head && obj->head->state == post) {
            advance_iterator(obj);
        }
    } break;
    case pre: {
        obj->head->state = in;
        if (obj->head->data->left) {
            TreeSLLNode* new_head = new_node(obj->head->data->left);
            new_head->next = obj->head;
            obj->head = new_head;
            advance_iterator(obj);
        }
    } break;
    case in: {
        obj->head->state = post;
        if (obj->head->data->right) {
            TreeSLLNode* new_head = new_node(obj->head->data->right);
            new_head->next = obj->head;
            obj->head = new_head;
        }
        advance_iterator(obj);
    } break;
    }
}

int bSTIteratorNext(BSTIterator* obj) {
    int to_return = obj->head->data->val;
    advance_iterator(obj);
    return to_return;
}


BSTIterator* bSTIteratorCreate(struct TreeNode* root) {
    BSTIterator* obj = malloc(sizeof(BSTIterator));
    obj->head = new_node(root);

    bSTIteratorNext(obj);

    return obj;
}

bool bSTIteratorHasNext(BSTIterator* obj) { return obj->head != NULL; }


void bSTIteratorFree(BSTIterator* obj) {
    TreeSLLNode* curr = obj->head;
    TreeSLLNode* next = NULL;
    while (curr) {
        next = curr->next;
        free(curr);
        curr = next;
    }
    free(obj);
}

void dfs_map(struct TreeNode* node, enum TraversalType traversal,
             void (*func)(struct TreeNode* node)) {
    if (node == NULL) {
        return;
    }

    if (traversal == preorder) {
        func(node);
    }

    dfs_map(node->left, traversal, func);
    if (traversal == inorder) {
        func(node);
    }

    dfs_map(node->right, traversal, func);
    if (traversal == postorder) {
        func(node);
    }
}

void print_node(struct TreeNode* node) { printf("%d\n", node->val); }

void free_node(struct TreeNode* node) { free(node); }

struct TreeNode* new_tree_node(int val) {
    struct TreeNode* node = malloc(sizeof(struct TreeNode));
    node->val = val;
    node->left = NULL;
    node->right = NULL;

    return node;
}

int main(int argc, char* argv[]) {

    struct TreeNode* root = new_tree_node(10);
    root->left = new_tree_node(5);
    root->right = new_tree_node(12);
    root->left->left = new_tree_node(2);
    root->left->right = new_tree_node(7);
    root->right->right = new_tree_node(18);

    BSTIterator* iter = bSTIteratorCreate(root);
    for (int i = 0; i < 6; i++) {
        printf("[%d]\n", bSTIteratorNext(iter));
    }

    dfs_map(root, inorder, print_node);
    dfs_map(root, postorder, free_node);

    printf("status %d\n", bSTIteratorHasNext(iter));

    bSTIteratorFree(iter);

    return EXIT_SUCCESS;
}
