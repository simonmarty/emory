/*
THIS  CODE  WAS MY OWN WORK , IT WAS  WRITTEN  WITHOUT  CONSULTING  ANY
SOURCES  OUTSIDE  OF  THOSE  APPROVED  BY THE  INSTRUCTOR. _Your_Name_Here_
*/

#define EXTERN

#include <stdio.h>
#include <stdlib.h>
#include "header.h"

EXTERN void setAll();
EXTERN void clearBit(int n);
EXTERN int testBitIs1(int n);

void sieveOfE(int N) {
   setAll();
   clearBit(0);
   clearBit(1);
   int i;
   int k = 2;   // Start with 2 to find all primes

   while(k <= N) {
      for(i = k; i <= N; i++) {  // Find the next prime number i
         if(testBitIs1(i))
            break;
      }

      for(int j = 2*i; j <= N; j += i) {
         clearBit(j);
      }

      k = i + 1;
   }
}

int countPrimes(int N) {
   int count = 0;
   for(int i = 2; i <= N; i++) {
      if(testBitIs1(i)) {
         count++;
      }
   }
   return count;
}

void printPrimes(int N) {
   int count = 0;
   for(int i = 2; i <= N; i++) {
      if(testBitIs1(i)) {
         printf("%d\n", i);
      }
   }
}

void setAll() {
  for(int i = 0; i < sizeof(prime)/4; i++) {
     prime[i] = 0xffffffff;
  }
}

void clearBit(int n) {
   int block = n / 32;
   int locationInBlock = n % 32;
   prime[block] &= ~(1 << locationInBlock);
}

int testBitIs1(int n) {
   int block = n / 32;
   int locationInBlock = n % 32;
   int testBit = 1 << locationInBlock;
   return (prime[block] & testBit) > 0;
}