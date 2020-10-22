#include<stdio.h>

int d;

int g(int x, int y) {
    int a = x+1;
    int b = y+1;
    return a*a+b*b;
}

int main(void) {
    d = g(1, 2);
}