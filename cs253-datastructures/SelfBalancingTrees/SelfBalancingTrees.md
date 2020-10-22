# Self Balancing Trees

## Binary Search Tree

Can use it for search operations

* Complexity is O(h) where h is the height of the binary tree
* Worst case is O(n) where the binary tree is essentially a linked list
    - Each node has one child only

    
    

``` python
treeSearch(node N, key K):
    if(N is null):
        return N
    if(N.value = L):
        return N
    elif(N.value < N):
        treeSearch(N.right, K)
    else:
        treeSearch(N.left, K)
```

Assuming the tree is balanced, if h > 10000, n = 2<sup>10000</sup>, which is ridiculously large.
We're essentially safe to recurse on the tree without worrying about overflow.

A **balanced** binary search tree would have height h = O(log n), but how do we construct such a tree?  
The BST needs to stay balanced even with additional operations (additions and removals)

Solution: **Self-balancing** binary search trees

### Insertion

Search for absent element terminates at a null pointer.

## Deletion

If a node has at most one child, just move that one child up to the spot where the removed node was.

Otherwise

* find the rightmost node in the left subtree of the node to delete (the **predecessor**)

$mdFormatter$3$mdFormatter$

``` python
    currentNode = v.left
    while(currentNode.right != null):
        currentNode = currentNode.right
```

* Move that node to the position of the node to delete 
* then move the predecessor's child up its parent's previous position

## In Order Traversal

* Recurse on left subtree (stop condition: `node.left == null` )
* Print node
* Recurse on right subtree (stop condition: `node.right == null` )

## Tree Rotations

![Tree Rotation](https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.P4I-yu0k1v6Tac23JOBW_QHaI3%26pid%3DApi&f=1)

and Trinode restructuring

# AVL Tree

Node height: heigh of the subtree rooted at node **including external or null nodes**

**Height balance property**

* For every internal node, children's heights differ by at most 1.
* This is enough to guarantee O(log n) height
* Let *m(h)* denote the minimum number of internal nodes in a hight *h* AVL tree.

Consider a height *h* AVL tree. At the root, what are the heights of its children?

How do we maintain that height balance with a tree rotation?
- Store height in node

- After inserting, if there's an imbalance, it's in one of the ancestors. Pick closest.

## Height field

- If the children's heights are correct, height of a node is `max(left.height, right.height) + 1`
- If the height of a node doesn't chang.......

## Deletion

