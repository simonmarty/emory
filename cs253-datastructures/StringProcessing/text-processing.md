# Text Compression

Given a long piece of text, want to compress the text:
* char primitive in Java: 2 bytes = 16 bits

1. Not every character used
2. Repetitions

Example:
* Space = 0
* A = 1
* B = 2
* etc
* 5 bits

## Prefix codes as binary tree

## Huffman Coding
* A = 0.10
* B = 0.33
* C = 0.27
* D = 0.16
* E = 0.04

* Make new node w/ val = 0.14
  * Two children, A and E
* Repeat with next two smallest
* Path to node is encoding

# Greedy algorithms

At each step, take the best choice at the time
* Huffman coding: choose 2 trees with lowest frequencies

In general, not optimal

Ex: Change with 1, 5, 10

For c < 10
* #1 < 5
* #5 < 2

How to show Greedy is optimal
* Greedy choice: Optimal solution always includes the greedy choice
* Optimal substructure: The optimal solution contains optimal solutions for subproblems

## Activity scheduling

Greedy choice
* Consider an optimal solution
* If it doesn't contain shortest task, replace with shortest task
  
Optimal substructure:
* In the remaining T-t_shortest time, we should have an optimal solution

Huffman coding is optimal w.r.t:

## &Sigma;<sub>c in C</sub>f(c)d(c)

* c: the set of characters
* f(c): frequency of c
* d(c): depth of c

Consider any tree on {a, b, ...}

# Text Search

## Boyer Moore
1. Start matching from right to left
2. If no match, jump length of pattern
3. If match for character, next jump is to nearest appearance

```
i += m - Math.min(k, 1 + last.get(text[i]));
k = m - 1.
```
--------------------------

# Recap

## Huffman encoding

* Greedy
* Pick two smallest frequencies every time
* Optimizes &Sigma;f(c)d(c) for c &in; C
  * C is the set of characters
  * f(c) is the frequency of c
  * d(c) is the depth of c

## Brute force


## Boyer-Moore
* Start matching from right to left
* Big jumps
* Try to match last character
* Mismatch but letter appears elsewhere in pattern, align letter with corresponding letter in pattern

### `last(A)`

CABBED
* `last(A)` = 1
* `last(B)` = 3
* ...


* When character doesnt appear at all, `i += m`
* When chracter appears, but last is too far forward, `i += m - k`
* When character appears, but last is behind it, `i += m - (1 + latest)`

## Knuth-Morris-Pratt

* Fail function
* Left to right
* O(m + n) - Pattern + text