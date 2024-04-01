// https://leetcode.com/problems/palindrome-linked-list/

#include "SLL.h"

#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

bool isPalindrome(struct ListNode* head) {
    int list_size = 0;
    struct ListNode* headcpy = head;
    struct ListNode* headcpy2 = head;

    while (headcpy != NULL) {
        headcpy = headcpy->next;
        list_size++;
    }

    int* digit_arr = calloc(list_size, sizeof(int));
    for (int i = 0; i < list_size; i++) {
        digit_arr[i] = headcpy2->val;
        headcpy2 = headcpy2->next;
    }

    for (int j = (list_size - 1); j >= 0; j--) {
        if (digit_arr[j] != head->val) {
            free(digit_arr);
            return false;
        }
        head = head->next;
    }
    free(digit_arr);
    return true;
}

int main() {
    struct ListNode* head = NULL;
    head = (struct ListNode*) malloc(sizeof(struct ListNode));
    head->val = 1;
    head->next = (struct ListNode*) malloc(sizeof(struct ListNode));
    head->next->val = 2;
    head->next->next = (struct ListNode*) malloc(sizeof(struct ListNode));
    head->next->next->val = 2;
    head->next->next->next = (struct ListNode*) malloc(sizeof(struct ListNode));
    head->next->next->next->val = 1;
    head->next->next->next->next = NULL;

    struct ListNode* anotherhead = head;
    struct ListNode* anotherhead2 = head;

    while (anotherhead != NULL) {
        printf("%d ", anotherhead->val);
        anotherhead = anotherhead->next;
    }

    assert(isPalindrome(head));
    while (anotherhead2 != NULL) {
        printf("%d ", anotherhead2->val);
        anotherhead2 = anotherhead2->next;
    }
}
