#include<stdio.h>
#include"bankaccount.h"

extern int getBalance(struct BankAccount *a);

extern void setBalance(struct BankAccount *a, int balance);

int main(void){
    BankAccount_t x;
    struct BankAccount *a;
    
    x.balance = 100.5;
    x.accountNumber = 1;
    a= &x;
    
    int y = getBalance(a);
    setBalance(a, 1000);
}