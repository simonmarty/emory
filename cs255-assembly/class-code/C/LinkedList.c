#include<stdio.h>
#include<stdlib.h>

typedef struct Node {
    int value;
    struct Node *next;
} Node_t;

int main(void) {
    Node_t *root, *p;
    root = malloc(sizeof(Node_t));
    root-> value = 1;
    root -> next = NULL;
    p = root;
    p = malloc(sizeof(Node_t));
    p -> next = root;
    p -> value = 2;
    root = p;
    p = malloc(sizeof(Node_t));
    p -> next = root;
    p -> value = 3;
    root = p;

    for(p = root; p != NULL; p = p -> next) {
        printf("%d\n", p-> value);
    }
}

