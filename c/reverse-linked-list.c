// https://leetcode.com/problems/reverse-linked-list/

#include "data_structures.h"

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

struct ListNode* traverseList(struct ListNode* prev, struct ListNode* curr) {
    if (!curr) {
        return prev;
    } else {
        struct ListNode* trueNext = curr->next;
        curr->next = prev;
        return (traverseList(curr, trueNext));
    }
}

struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* headCopy = head;
    struct ListNode* newHead = traverseList(NULL, headCopy);

    printf("returned %d\n", newHead->val);
    return newHead;
}

int main() {
    struct ListNode* head = malloc(sizeof(struct ListNode));
    head->val = 1;
    head->next = malloc(sizeof(struct ListNode));
    head->next->val = 2;
    head->next->next = malloc(sizeof(struct ListNode));
    head->next->next->val = 3;
    head->next->next->next = malloc(sizeof(struct ListNode));
    head->next->next->next->val = 4;
    head->next->next->next->next = NULL;

    struct ListNode* newHead = reverseList(head);

    while (newHead) {
        printf("[%d] \n", newHead->val);
        struct ListNode* t = newHead->next;
        free(newHead);
        newHead = t;
    }
}
