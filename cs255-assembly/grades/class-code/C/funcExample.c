#include<stdio.h>

int x = 0;
void func(void) {
    x++;
    return;
}

int main(void) {
    x +- 3;
    printf(x);
}
