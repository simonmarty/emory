# Chapter 2

Context free grammars: G<sub>1</sub>
1. A &rarr; OA1
2. A &rarr; B
3. B &rarr; #

A CFG is in Chomsky Normal Form if every rule is one of these types:
1. S &rarr; &epsilon;
2. A &rarr; BC  (B &notin; S, C &notin; S)
3. A &rarr; *a* (terminal)

**Theorem 1**: We can convert every CFG to Chomsky Normal Form

## Parsing Problem

Given w &in; &Sigma;* and grammar G, is w &in; L(G)?

If w = w<sub>1</sub>w<sub>2</sub>... &in; &Sigma;*
and G is in Chmsky form, we want to decide whether w &in; L(G)

Claim: Any derivation of w from S has 2n - 1 steps.

Idea: 
* n - 1: "A &rarr; BC" to get length
* n: "A &rarr; a" to get terminals

So: We can solve parsing problem in exponential time (try all derivations of 2n - 1 steps)
* In fact there is a O(n<sup>3</sup>) time, "CYK Algorithm" (&sect;7, p291)

Most computing languages are designed to have O(n)-time parsers (&sect;2.4)

## &sect; 2.2: Push-down Automaton

Goal: PDA &approx; CFG

### Ambiguous Grammar Example

E &rarr; E + E | E * E | (E) | 2

## Reverse

Given a PDA, produce the CFG that accepts the same language (L(G) = L(P))

Step 1: Put P into "nice" form

1. Single final state
2. We clear stack when entering final state
3. Every transition is a "push" or a "pop"

### Building G

For every pair of states p, q in P, introduce a variable A<sub>pq</sub>

For state p and state s &in; &Gamma;*, say (p,s) is a "configuration" of P.

Goal: For all strings w &in; &Sigma;*, we want:

A<sub>pq</sub> &rarr; *w &harr; P has a computation from (p, &epsilon;) to (q, &epsilon;) reading w

1. A<sub>pq</sub> &rarr; a A<sub>rs</sub> b
2. For every three states p,r,q, Add rule: A<sub>pq</sub> &rarr; A<sub>pr</sub>A<sub>rq</sub>
3. For every state p: Add rule A<sub>pp</sub> &rarr; &epsilon;

### CF Pumping Game for L:
1. C picks p &geq; 0
2. N picks s &in; L, |s| &geq; p
3. C picks u,v,x,y,z &in; &Sigma;* so uvxyz = s, |vy| &geq; 1, |vxy| &leq; p
4. N picks i &geq; 0 so uv<sup>i</sup>xy<sup>i</sup>z &notin; L

Theorem L context free &rarr; C has a winning strategy

Corollary: N has a winning strategy &rarr; L is not context free

## HW2 Problem 5 Hint

Given a grammar G, determine {A: A &rarr;* &epsilon;}

S := {A: "A&rarr;&epsilon;" &in; R}

while r has a rule A &rarr; &alpha; where A &notin; S and &alpha; &in; S*, S:=S&cup;{A}

return S

A &rarr; BC 3rd
B &rarr; &epsilon; 1st
C &rarr; BB 2nd

At end: If we start with same B &notin; S, and if B &rarr;\* w,
we claim w &notin; S\*

