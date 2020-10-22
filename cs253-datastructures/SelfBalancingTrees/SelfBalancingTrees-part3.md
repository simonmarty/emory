# 2,4 Tree

A 2,4 tree has:
* k = 2,3,4 at every internal node
* All external nodes are at the same depth

Proof: Every internal node has 2-4 children  
Height 0: (1) root node
Height 1: 2 to 4 nodes
Height 2: 2^2 to 4^2 nodes

## Operations

Search: O(h) time (one pass downwards)  
Rebalancing: O(h) time (one pass upwards)

h = O(log n)

# Red Black Trees

* Root is black
* No two adjacent red nodes
* Any path from a node to null has the same number of black nodes

## Insert

```
If it's the root, color it black, return

If parent is already colored black, return  

recolor // Parent is red
```

Case 1: Parent's sibling is black --> Left or right rotate

Case 2: Parent's sibling is red --> color flip
## Recoloring

## Tree Rotations

## Deletion

Deletion looks similar to transfer and fusion operators in 2-4 trees

Case 1: sibling is black and has a red child

Trinode restructuring, recolor ("transfer")

Case 2: sibling is black and has both black children

Now, sibling can be recolored (y is a 2-node)

Deletion uses at most two rotations.