#include"bankaccount.h"
#include<stdio.h>

int getBalance(struct BankAccount *a) {
    return (*a).balance;
}

void setBalance(struct BankAccount *a, double amount) {
    (*a).balance = amount;
    printf("%lf\n", (*a).balance);
}