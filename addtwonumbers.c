#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *i, *j, *sumList;
    size_t exp, sum = 0;
    for (i = l1, exp = 1; i != NULL; i = i->next, exp *= 10) {
        sum += i->val * exp;
    }
    for (j = l2, exp = 1; j != NULL; j = j->next, exp *= 10) {
        sum += j->val * exp;
    }

    long sumcopy;
    int digitcount;
    for (digitcount = 0, sumcopy = sum; sumcopy > 0; sumcopy /= 10, digitcount++) {
        ;
    }

    if (digitcount == 0) {
        sumList = malloc(sizeof(struct ListNode));
        sumList->val = 0;
        sumList->next = NULL;
        return sumList;
    }

    char *intstr = calloc(sizeof(char), digitcount+1);
    snprintf(intstr, (digitcount+1), "%ld", (sum)); 

    int asciiDigit;
    struct ListNode *currentNode = malloc(sizeof(struct ListNode));
    sumList = currentNode;

    for (int k = --digitcount; k > 0; k--) {

        asciiDigit = intstr[k] - '0';
        currentNode->next = malloc(sizeof(struct ListNode));

        currentNode->val = asciiDigit;
        currentNode = currentNode->next;

    }
    currentNode->val = intstr[0] - '0';
    currentNode->next =  NULL;

    free(intstr);
    return sumList;
}


int main() {

    struct ListNode* head = NULL;
    head = (struct ListNode *) malloc(sizeof(struct ListNode));
    head->val = 9;
    head->next = NULL; 

    struct ListNode* head2 = NULL;
    head2 = (struct ListNode *) malloc(sizeof(struct ListNode));
    head2->val = 1;
    head2->next = (struct ListNode *) malloc(sizeof(struct ListNode));
    head2->next->val = 1;
    head2->next->next = (struct ListNode *) malloc(sizeof(struct ListNode));
    head2->next->next->val = 4;
    head2->next->next->next = NULL;

    struct ListNode *headcopy = head;
    struct ListNode *head2copy = head2;

    while (headcopy != NULL) {
        printf("[%d] ", headcopy->val);
        headcopy = headcopy->next;
    }
    printf("\n");
    while (head2copy != NULL) {
        printf("[%d] ", head2copy->val);
        head2copy = head2copy->next;
    }
    printf("\n");


    struct ListNode *x = addTwoNumbers(head, head2);

    while (x != NULL) {
        printf("[%d] ", x->val);
        struct ListNode *nn = x->next;
        free(x);
        x = nn;
    }
    printf("\n");

    while (head != NULL) {
        struct ListNode *nn = head->next;
        free(head);
        head = nn;
    }
    while (head2 != NULL) {
        struct ListNode *nn = head2->next;
        free(head2);
        head2 = nn;
    }

}