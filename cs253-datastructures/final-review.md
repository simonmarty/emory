# Final Review

## Priority Queues

Heaps don't have any slow implementations
* insert: O(log(n))
* peek: O(1)
* removeMin: O(log(n))
* isEmpty: O(1)

## Huffman Coding

Given frequencies

## Boyer-Moor

i += m - min(k, 1 + last)

When character doesn't appear, i += m

## Topological ordering

## Edge relaxation

Dijkstra
* Edge relaxation at edges leaving vertex with lowest priority

O(min(ElogV, V^2)) // the first is with a heap, the second is with an unsorted collection

Unsorted collection can perform better as the number of edges can easily be E^2

Bellman-Ford
* Relax all edges, any order

Priority queue operations:
* n insertions/removeMins
* m replaceKeys

