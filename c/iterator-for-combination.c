// https://leetcode.com/problems/iterator-for-combination/

#include <stdbool.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int sub_start;
    int depth;
    struct Node* next;
} Node;

typedef struct CombinationIterator {
    char* bank;
    int bank_len;
    int max_comb_size;
    Node* head;
} CombinationIterator;

Node* new_node(int sub_start, int depth, Node* next) {
    Node* node = malloc(sizeof(Node));
    node->sub_start = sub_start;
    node->depth = depth;
    node->next = next;

    return node;
}

void pop(CombinationIterator* obj) {
    Node* new_head = obj->head->next;
    free(obj->head);
    obj->head = new_head;
}

void advance_iterator(CombinationIterator* obj) {
    if (!obj->head) {
        return;
    }
    if (obj->head->depth == obj->max_comb_size) {
        pop(obj);
        return;
    }

    if (obj->head->sub_start < obj->bank_len) {
        obj->head->sub_start++;
        Node* new_head =
            new_node(obj->head->sub_start, obj->head->depth + 1, obj->head);
        obj->head = new_head;
    } else {
        pop(obj);
    }
    advance_iterator(obj);
}

CombinationIterator* combinationIteratorCreate(char* characters,
                                               int combinationLength) {
    CombinationIterator* obj = malloc(sizeof(struct CombinationIterator));
    obj->bank = characters;
    obj->bank_len = strlen(characters);
    obj->max_comb_size = combinationLength;
    obj->head = new_node(0, 0, NULL);
    advance_iterator(obj);

    return obj;
}

char* build_str(CombinationIterator* obj) {
    char* str = malloc(sizeof(char) * obj->max_comb_size + 1);
    memset(str, 0, obj->max_comb_size + 1);

    Node* curr = obj->head;
    for (int i = obj->max_comb_size - 1; i >= 0; --i) {
        str[i] = obj->bank[curr->sub_start - 1];
        curr = curr->next;
    }
    return str;
}

char* combinationIteratorNext(CombinationIterator* obj) {
    char* to_return = build_str(obj);
    advance_iterator(obj);

    return to_return;
}

bool combinationIteratorHasNext(CombinationIterator* obj) {
    return obj->head != NULL;
}

void combinationIteratorFree(CombinationIterator* obj) {
    Node* curr = obj->head;
    while (curr) {
        Node* next = curr->next;
        free(curr);
        curr = next;
    }

    free(obj);
}


void print_stack(CombinationIterator* obj) {
    Node* curr = obj->head;
    while (curr) {
        printf("depth: %d   sub_start %d\n", curr->depth, curr->sub_start);
        curr = curr->next;
    }
}

int main(int argc, char* argv[]) {
    CombinationIterator* obj = combinationIteratorCreate("abcd", 2);

    for (int i = 0; i < 6; ++i) {
        print_stack(obj);
        char* str = combinationIteratorNext(obj);
        printf("%s\n", str);
        free(str);
    }
    combinationIteratorFree(obj);
    return EXIT_SUCCESS;
}
