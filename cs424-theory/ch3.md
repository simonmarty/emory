# Chapter 3: Turing Machines

## Enumerators

Print out all strings of a language in arbitrary order

Turing machine E has a work tape and a printing tape

Q: Is "enumerable" a new class of languages

A: No. "enumerable" &equiv; "recognizable"

Warmup: Enumerate {a, b}*?

We would like standard order

&epsilon;, a, b, aa, ab...

**Claim 1** If L is enumerable, then L is recognizable

**Proof**

## Universal Turing Machine

Idea: Suppose M is a TM and `x` is an input for M

U = "On input <M, x>: on x

Simulate M, step by step:
* If M accepts, ACCEPT
* If M rejects, REJECT
* Else keep going

L(U){<M, x>}

### A<sub>DFA</sub>

We know how to simulate computation of B and w so that A<sub>DFA</sub> is decidable

### A<sub>NFA</sub>

Convert NFA to DFA

### A<sub>REX</sub>

Regex to NFA

### E<sub>DFA</sub>

Check if state F is reachable from start

### EQ<sub>DFA</sub>

Decidable Construct product DFA P

Let P accept &harr; exactly one of A, B accepts

### A<sub>CFG</sub>

Convert G to Chomsky Normal Form, try all derivations of appropriate length

### E<sub>CFG</sub>

------------------------
### Proof (Easy direction)

Suppose L is decidable  
Let M be a decider of L  
L = L(M), so L is recognizable  
Let M' be M with q<sub>accept</sub>, q<sub>reject</sub> swapped, then  
L(M') = co-L, so L is co-recognizable

### Harder direction

Suppose L and compL are recognizable  
There exist TM's M1 and M2 s.t.  
L(M1) = L, L(M2) = compL  

```
D = on input w:
    Simulate both M1(w) and M2(w) in parallel
    If M1 accepts:
        accept
    If M2 accepts:
        reject
```
D is a decider since it always halts for L(D) = L