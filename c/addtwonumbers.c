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
    bool iDone = false;
    bool jDone = false;
    bool carry = false;

    int placeval;

    i = l1;
    j = l2;
    struct ListNode *currNode = (struct ListNode *) malloc(sizeof(struct ListNode));
    sumList = currNode;
    while ((i->next != NULL) || (j->next != NULL)) {

        placeval = i->val + j->val + carry;
        if (placeval >= 10) {
            placeval -= 10;
            carry = true;
        } else {
            carry = false;
        }
        currNode->val = placeval;

        if ( (i->next == NULL) && (j->next == NULL) && !carry ) {
            currNode->next = NULL;
        } else if ( (i->next == NULL) && (j->next == NULL) && carry ) {
            currNode->next = (struct ListNode *) malloc(sizeof(struct ListNode));
            currNode->next->val = 1;
            currNode->next->next = NULL;
            currNode = currNode->next; // prob unneeded
        } else {
            currNode->next = (struct ListNode *) malloc(sizeof(struct ListNode));
            currNode->next->val = -1;
            currNode->next->next = NULL;
            currNode = currNode->next;
        }
        

        if ( i->next != NULL ) {
            i = i->next;
        } else if (i->next == NULL){
            i->val = 0;
        }

        if ( j->next != NULL ) {
            j = j->next;
        } else if (j->next == NULL) {
            j->val = 0;
        }
        
    }
    
    currNode = NULL;
    return sumList;
}


int main() {

    struct ListNode* head = NULL;
    head = (struct ListNode *) malloc(sizeof(struct ListNode));
    head->val = 6;
    head->next = (struct ListNode *) malloc(sizeof(struct ListNode)); 
    head->next->val = 6;
    head->next->next = (struct ListNode *) malloc(sizeof(struct ListNode));
    head->next->next->val = 3;
    head->next->next->next = (struct ListNode *) malloc(sizeof(struct ListNode));
    head->next->next->next->val = 2;
    head->next->next->next->next = NULL;

    struct ListNode* head2 = NULL;
    head2 = (struct ListNode *) malloc(sizeof(struct ListNode));
    head2->val = 4;
    head2->next = (struct ListNode *) malloc(sizeof(struct ListNode));
    head2->next->val = 5;
    head2->next->next = (struct ListNode *) malloc(sizeof(struct ListNode));
    head2->next->next->val = 2;
    head2->next->next->next = (struct ListNode *) malloc(sizeof(struct ListNode));
    head2->next->next->next->val = 6;
    head2->next->next->next->next = NULL;

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