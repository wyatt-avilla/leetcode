// https://leetcode.com/problems/remove-nodes-from-linked-list/

#include "SLL.h"

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

struct ListNode* deleteUntil(struct ListNode* head, int target) {
    struct ListNode* headcpy = head;
    struct ListNode* temp = NULL;
    while (headcpy) {
        if (headcpy->val == target) {
            head = headcpy;
            break;
        }
        temp = headcpy->next;
        free(headcpy);
        headcpy = temp;
    }
    return head;
}

bool greaterAhead(struct ListNode* currentNode, int comparingAgainst,
                  bool* isSorted, int* foundMax) {
    struct ListNode* currcpy = currentNode;
    *isSorted = true;
    while (currcpy->next) {
        if (currcpy->val < currcpy->next->val) {
            *isSorted = false;
        }
        if (currcpy->next->val > comparingAgainst) {
            *foundMax = currcpy->next->val;
            printf("found! %d\n", *foundMax);
            return true;
        }
        currcpy = currcpy->next;
    }
    return false;
}

struct ListNode* removeNodes(struct ListNode* head) {
    struct ListNode* retNode = head;
    struct ListNode* currentNode = head;
    struct ListNode* prevNode = NULL;
    bool isSorted = false;
    int currentMax = 0;
    while (currentNode) {
        if (isSorted) {
            break;
        }
        if (greaterAhead(currentNode, currentNode->val, &isSorted,
                         &currentMax)) {
            currentNode = deleteUntil(currentNode, currentMax);
            if (!prevNode) {
                retNode = currentNode;
            } else {
                prevNode->next = currentNode;
            }
            continue;
        }
        prevNode = currentNode;
        currentNode = currentNode->next;
    }
    return retNode;
}

int main() {
    struct ListNode* head = malloc(sizeof(struct ListNode));
    head->val = 5;
    head->next = malloc(sizeof(struct ListNode));
    head->next->val = 2;
    head->next->next = malloc(sizeof(struct ListNode));
    head->next->next->val = 13;
    head->next->next->next = malloc(sizeof(struct ListNode));
    head->next->next->next->val = 3;
    head->next->next->next->next = malloc(sizeof(struct ListNode));
    head->next->next->next->next->val = 8;
    head->next->next->next->next->next = NULL;


    struct ListNode* newHead = removeNodes(head);

    while (newHead) {
        printf("[%d] \n", newHead->val);
        struct ListNode* t = newHead->next;
        free(newHead);
        newHead = t;
    }
}
