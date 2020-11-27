#include<stdio.h>

int main(void) {
    int x = 2;
    int *p;

    p = &x;
    *p = 5;
    printf(x);

    int array[10];
    p = array;

    for(int i = 0; i < 10; i++) {
        *p = 1;
        p++;
    }
}

void func(int *a) {
    (*a)++;
    return;
}