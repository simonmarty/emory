#include<stdio.h>
#include<stdlib.h>
#include"bankaccount.h"

int main(void) {
    BankAccount_t *a;
    a = malloc(sizeof(BankAccount_t));
    a -> balance = 100;
    a -> accountNumber = 13;

    printf("Account Balance: %d\n", a -> balance);
    free(a);
    a = malloc(sizeof(BankAccount_t));
    a->balance = 200;
    a->accountNumber = 2;
}