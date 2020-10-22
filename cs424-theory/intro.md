# Course Outline

1. Finite Automaton
2. Push-down automaton
3. Turing Machine
4. Computability
7. Complexity 

## General computation Problem

input &rarr; ? &rarr; output

## String Decision Problem


## Strings

Pick a finite set of symbols, &Sigma;,
called our alphabet. For example:  

&Sigma; = {a,b}

A *string* x is a finite sequence of symbols

Let &Sigma;<sup>k</sup> = { all strings of length k}

&epsilon; is the empty string (also &lambda; sometimes)

&Sigma;<sup>*</sup> denotes all strings

A *language is a subset of &Sigma;<sup>*</sup>

## Deterministic finite automaton

* Only looks at input once
* Finite amount of memory

### First Example

L<sub>1</sub> = { x &sub; &Sigma;<sup>*</sup>: #<sub>b</sub>(x) is odd }

### Definition

* Q = a finite set
* &Sigma; = a finite set
* &delta; is a function from Q &cross; &Sigma; to Q
* q<sub>0</sub> &isin; Q
* F &subseteq; Q


Give a DFA M and an input string X = x1x1x3...xn

## Nondeterministic Finite Automaton

An NFA accepts input x iff there is some computation path that
1. Starts at the initial state
2. Ends at a a final state
3. Reads symbolss of x

NFA's are ata least as expressive as DFAs.  
Any DFA that defines a Language can be written into an NFA  
Later we'll be able to go the other way around.

* Show A &deg; B and A* using NFA
* Convert NFA back to DFA

### Claim

Given an NFA N, we can produce a DFA M accepting exactly the same strings (L(M) = L(N))

### Idea

Construct M that keeps track of the subset of states that N could be in after reading input seen so far

States of M = subsets of states of N

`#` states of M &leq; 2

## Definition of NFA

Q x &Sigma;<sub>&epsilon;</sub> &rarr; P(Q)

* P(Q) is the powerset of Q


## Regex

```
L1 = L((a*ba*ba*)*a*ba*) // matches any string with odd number of b's
```

| Regex &alpha; | Language L(&alpha;) |
|:---:|:---:|
| &epsilon; | {&epsilon;} |
| &empty; | { } |
| a,b... | {a},{b},... |
| &alpha; &cup; &beta; | L(&alpha;) &cup; L(&beta;) |
| &alpha;&beta; | L(&alpha;) &dot; L(&beta;) |
| &alpha;* | L(&alpha;)* |

### Claim

Given a regex &alpha;, we can construct an NFA N such that L(&alpha;) = L(N)

### Proof

By induction on length of &alpha;
Base cases:
* &epsilon; &rarr; : Either null string jump or stay on current state, final
* a &rarr;
* &empty; &rarr;: Stay on start

Combine these simple NFAs for any longer regexes

### Summary
* DFA to NFA: n to n
* NFA to DFA: n to 2<sup>n</sup>
* regex to NFA: n to O(n)

## Claim

Given an NFA with n states, we can make a regex with size 4<sup>n</sup>

### NFA to GNFA

NFA has
* Arrows into its start state
* Multiple final states
* Add outer start state with &epsilon; arrow into the NFA start state
* Send all final states to new final state with &epsilon; arrows.
* Add &empty; arrows if needed

Step 2:
* If N has &geq; 3 states.
* Pick p &notin; { q<sub>start</sub>, q<sub>accept</sub> }
* concatenate steps in a path to delete intermediate states.

## How do you show languages are not regular?

Pumping Lemma:
* page 78

* 3 equivalent models
* "perfect" characterization of regular language (Myhill-Nerode Theorem)


Given a DFA, how do we check that it is minimum size?
1. Check each state is reachable from q<sub>0</sub>
2. Check each pair of states has a "distinguishing string"

# Lecture 3

Minimal DFA?
* reachable
* distinguish every pair

| pair | z |
|:---:|:---:|
 0, 1 | *bb*
0, 2 | *b*
0, 3 | &epsilon;
1, 2 | *b*
1, 3 | &epsilon;
2, 3 | &epsilon;