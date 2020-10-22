# Dynamic Programming

F<sub>1</sub>=1, F<sub>2</sub> = 2

F<sub>n</sub> = F<sub>n - 1</sub> + F<sub>n - 2</sub>

Inefficient approach: Recursion

## Dynamic Programming approach

```
public int fib(int n) {
    int a = 1;
    int b = 1;

    for(int i = 3; i < n; i++) {
        int c = a + b;
        a = b;
        b = c;
    }

    return a + b;
}
```

## Chain Matrix Multiplication

* A: m &times; n
* B: n &times; p
* Total number of operations in the naive way takes **n &times; m &times; p**

* Catalan numbers

Time save: O(4^n) to O(n^3)

## Memoization

For Fibonnacci, we can store previous results in a hash table. Useful for functional languages.

## Numways to travel through a grid

Diagonally
```
for(int d = 0 to n) {
    for (int x = 0 to d) {
        int y = d-x;
    }
}
```

```
for(int x = 0 to n) {
    for (y from 0 to n) {
        
    }
}
```

## Subset Sum

n<sub>1</sub> through n<sub>k</sub>

Find subset that sums to `S`

NP Complete

## Longest Common subsequence

Count: 2^n

How many substrings are there? O(n<sup>2</sup>) , n choose 2
Similar strategy to finding paths in a grid

* If last characters match, remove both and recurse on the rest
  * `L(i,j) = 1 + L(i - 1, j - 1)`
* If last characters dont match, remove one and recurse
  * `L(i,j) = Max(L(i, j-1), L(i-1, j))`
```
lcs("string1", "string2");
lcs("string1, "string");
lcs("string", "string2");
lcs("string", "string");
```

`L(i, j) = LCS of S[0,...,i-1] and T[0,...,j-1]`

Easy case: empty string has no subsequences

`L(i, j) = 1 + L(i - 1, j - 1)`

## Table

Rule: if there's no match, move up or left until we find another

Step down diagonally

---------------------------------

# Edit Distance

Example: How many char insertions, deletions, substitutions do you need?

SUNDAY -> SATURDAY

Define function `ED(i, j)`
* `ED(i, 0) = i`
* `ED(0, j) = j`

If we delete the ith character
* `ED(i, j)` <= `ED(i, j - 1) + 1`

If we substitue the ith character with the jth character
* Prefix `A[1 ... i - 1]`
* Prefix `B[1 ... j - 1]`

```
Cost = ED(i- 1,j-1) + 1 if(A[i] != B[j]) else 0
```

## Transpositions

transposeCost(i, j) = ED(i - 2, j - 2) + 1

## Longest increasing subsequence

* If j > n, 0 (base case)
* If A[i] > A[j], lis(i, j + 1)
* Otherwise, bigger of
  * lis(i, j + 1)
  * 1 + lis(j, j + 1)

# Maximum independent set

An independent set is a subset of non-adjacent vertices

Problem: finding the largest one

# P vs. NP

P: class of decision problems **solvable** in polynomial time:
* Is the minimum element of this array < k?

Does *not* include
* What is the edge distance between these two strings

Includes
* Modified: Is the edit distance between these two strings <= k?

NP: Verifiable in polynomial time
* Is there a subset of {2, 5, 8, 13, 21} that sums to 31?

Given a candidate solution (e.g. {2, 8, 21}), one can verify that it's valid in polynomial time

* NP contains P
* NP-complete = every problem in NP can be reduced to it
* NP hard: at least as hard as NP

Most people don't think NP hard problems can be solved in polynomial time

can be salvaged in special cases or by approximation

