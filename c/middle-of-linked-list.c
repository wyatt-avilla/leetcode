// https://leetcode.com/problems/middle-of-the-linked-list/

#include "SLL.h"

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct ListNode* node;


node middleNode(struct ListNode* head) {
    node current = head;
    int head_len = 0;
    while (current != NULL) {
        head_len++;
        current = current->next;
    }

    current = head;
    for (int i = 0; i <= head_len / 2; i++) {
        if (i == head_len / 2) {
            return current;
        }
        current = current->next;
    }
    return NULL;
}


int main() {


    // ------------------------------------------ case 1
    node case_1_head = malloc(sizeof(struct ListNode));
    case_1_head->val = 1;

    node prev_node_1 = case_1_head;
    for (int i = 2; i <= 5; i++) {
        node new_node = malloc(sizeof(struct ListNode));
        new_node->val = i;
        new_node->next = NULL;
        prev_node_1->next = new_node;
        prev_node_1 = new_node;
    }

    node middle_node = middleNode(case_1_head);
    printf("case 1: ");
    if (middle_node->val == 3) {
        printf("\033[1;32mPASS\033[0m\n");
    } else {
        printf("\033[1;31mFAIL\033[0m\n");
    }
    // free(middle_node);

    node current1 = case_1_head;
    while (current1 != NULL) {
        node prev = current1;
        // printf("%d ", current->val);
        current1 = current1->next;
        free(prev);
    }

    // ------------------------------------------ case 2
    node case_2_head = malloc(sizeof(struct ListNode));
    case_2_head->val = 1;

    node prev_node_2 = case_2_head;
    for (int i = 2; i <= 6; i++) {
        node new_node = malloc(sizeof(struct ListNode));
        new_node->val = i;
        new_node->next = NULL;
        prev_node_2->next = new_node;
        prev_node_2 = new_node;
    }

    node middle_node_2 = middleNode(case_2_head);
    printf("case 2: ");
    if (middle_node_2->val == 4) {
        printf("\033[1;32mPASS\033[0m\n");
    } else {
        printf("\033[1;31mFAIL\033[0m\n");
    }
    // free(middle_node_2);

    node current2 = case_2_head;
    while (current2 != NULL) {
        node prev = current2;
        // printf("%d ", current->val);
        current2 = current2->next;
        free(prev);
    }
}
