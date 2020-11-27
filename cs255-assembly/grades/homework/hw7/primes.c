/*
THIS  CODE  WAS MY OWN WORK , IT WAS  WRITTEN  WITHOUT  CONSULTING  ANY
SOURCES  OUTSIDE  OF  THOSE  APPROVED  BY THE  INSTRUCTOR. Simon Marty
*/

#define EXTERN

#include <stdio.h>
#include <stdlib.h>
#include "header.h"

EXTERN void setAll();
EXTERN void clearBit(int n);
EXTERN int testBitIs1(int n);

int testIsBit0(int);
void setBit(int);
int getSeg();
int getIndex();
int getShift();
int number();

// Uses head to find the "bit array" (list)
void clearAll(){
        seg * p;
        p = head;

        while(p!=NULL){
                for(int i = 0; i < SIZE_OF_SEG; i++){
                        p->bits[i] = 0;
                        //printf("%d\n", p->bits[i]);
                }
                p = p->next;
    }
}

// return 1 when the integer n is not prime
int  testIsBit0(int n){

        int segm, pos, i, output;
        segm = (getSeg(n) + 1);
        i = getIndex(n);
        pos = getShift(n);

        seg * p;
        int j;
        p = head;

        for ( j = 0; j < segm; j++)
                p = p->next;

        unsigned int flag = 1;
    flag = flag << pos;

    output = (((p->bits[i] & flag) != 0) ? 0 : 1);
    return output;
}

// finds all the odd prime numbers (stores them in the segmented bit array (linked list) that starts at head).
void sieveOfE( int N ){
        setBit(1);
    // start with 3
        int k = 3;
    int i, j;

    while ( k <= N ) {
    /* ----------------------------------------
        Starting from k, find next
        prime number number i

        A prime number is detected by:

                    isPrime[i] == true
        ---------------------------------------- */

        for ( i = k; i <= N; i++ )
            if( testIsBit0(i) == 1){ break;}// Found !

        /* --------------------------------------
            Set:  isPrime[2*i] = false,
            isPrime[3*i] = false,
            ....
            (upto isPrime[N])
        -------------------------------------- */

        for (j = 2 * i; j <= N; j = j + i) {
            if (j % 2 != 0)
                setBit(j);
        }
        k = i + 2;
        }
}

// counts the total number of primes
int  countPrimes( int N ) {
    int primeCount = ((N >= 2)? 1  : 0);

    // i = i + 2 b/c everything is odd
    for(int i = 1; i <= N; i = i + 2) {
        if( testIsBit0(i))
            primeCount++;
    }
        return primeCount;
}

//  prints a count of the number of primes found and prints out a list of primes if there are ≤ 100 primes.
void printPrimes( int N ){
    if(N > 2)
        printf("prime: 2\n");

        for(int i = 1; i <= N; i = i + 2) {
        if( testIsBit0(i))
            printf("prime: %d\n", i);
    }
}

// setBit in pos n to 0
void setBit(int n) {
        int segm, pos, i;
        segm = getSeg(n) + 1;
        i = getIndex(n);
        pos = getShift(n);

        seg * p;
        int j;
        p = head;

        for ( j = 0; j < segm; j++)
                p = p->next;

    // shifts bit pos positions
        unsigned int flag = 1;
    flag = flag << pos;

    // set bit at pos position in A[i] to 0
    p->bits[i] = p->bits[i] | flag;
}

// the main program reads in a number of integers and calls factor() to print out the prime factors for each input.
void factor(int inp){
    clearAll();
    sieveOfE(inp);

    // deals w even numbers
    while(inp % 2 == 0){
        printf(" 2 ");
        inp = inp / 2;
    }

    // deals w odd numbers
    for(int i = 3; i<= inp; i = i + 2) {
            if( testIsBit0(i)){
                while(inp%i==0){
                    printf(" %d ", i);
                    inp = inp / i;
                }
            }
        }
        printf("\n");
}

int getIndex(int N){
        return (((N - 1) / 2) / 32)  % 256;
}

int getSeg(int N){
        return ((N - 1) / 2) / BITS_PER_SEG;;
}

int getShift(int N){
        return ((N - 1) / 2)  % 32;
}

int number(int segm, int index, int shift){
        return ((BITS_PER_SEG * segm) + (32 * index) + shift);
}
