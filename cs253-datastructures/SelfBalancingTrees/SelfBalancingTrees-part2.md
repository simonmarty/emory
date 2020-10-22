# Self-Balancing Trees - Part 2

Operations that balance binary trees

* Keep insert, search, delete
* Rebalance after each operation
    - Many balancing schemes exist (AVL, splay, red-black, etc.)

### AVL tree - search rebalance 

No rebalancing for searches

## Binary tree implementation

Each node contains pointers to

* its left and right children
* its parent

Additional fields:

* Height (AVL trees)
* One bit (Red-Black Tree)

Rotation function syntax  
`rotate(Node n)` - rotates n with its parent.n is **the child**
<br></br>
`relink(Node parent, Node child, boolean makeLeftChild)` 

* X, Y children
* Grandparent child

-----------------------

## Splay Trees

Each time an operation is done, the target node (or something close by) becomes the new root.
Useful for repeated queries: The thing you want again is already at the top  
No explicit rebalancing condition  
It is possible to get linear height for trees.

Add a new node

* Rotate new node so it becomes the root
* When the node doesnt exist (**failed search**, deleted node), splay the parent.

### Splaying vs move-to-root

``` 
move-to-root():
    while(root != node):
        rotate(node)
```

Splaying: handle depths 2 at a time

* zig-zig
* zig-zag
* zig (for odd depths, at the end if your node is not yet root)

Move-to-root can have Omega(n^2) total complexity for n search/insert/remove operations.
Splay tree will have O(n log n) total complexity.

[Splay Tree Demo](http://www.link.cs.cmu.edu/splay/)

------------------

## Amortized Analysis - Dynamic Arrays

"If you insert into a full array, double the array size."
Worse case for n inserts is O(n

### Aggregate method

Rearrange carefully and add up the cost of each operation:

* n inserts, O(n) time
* If k is the largest integer such that 2^k <= n, then the resizing costs:
    - O(1) + O(2) + O(4) ... O(2^k) = O(2^(k + 1)) = O(n)

In total, the N insert options cost O(N) time, or O(1) per operation

### Potential Method

Define a "potential function" phi(T) on your data structure.

* For an operation, amortized cost = actual cost + Delta phi
    - change in potential
* A good potential function will "smooth" the costs:
    - Cheap operations will take longer
    - Expensive operations will take shorter

phi = 2n - N, where n is used space, N is the array length  

* Delta phi = 2 for insert: array stays the same
* Delta phi = -N for double: n stays the same, but N doubles

<br></br>

* Amortized cost for insert: 1 (actual) + 2 (change in potential)  
* Amortized cost for doubling with insert: N + 1 (actual) + 2 - N (change in potential)  

**Both cases**: amortized cost is 3, so total cost is <= 3n.
Which is O(n).

## Potential Method - Splay Trees

* Good choice of potential function is key
* Splay tree potential function:
    - Potential at node: log(size(node))
    - Potential of tree: sum of node potentials

`size(node)` : number of nodes in the subtree located at that node  
`rank = log(2, size(node))` 

**Claim**: If a rotation costs 1, doing:

* Zig on x takes <= 3(Delta r(x)) + 1 *amortized* time
* zig-zig or zig-zag on x <= 3(Delta r(x)) *amortized* time

If **Claim** is true, then the total amortized cost of splaying x is at most

`3(r(t)-r(x)) + 1 = O(log n)` 

Where t is the root  
rank(t) is constant  
Total amortized cost: ~O(m log n) for m operations  
O(n log n) is the max change  
Total true runtime: O((m + n) log n)

Average time per search: O(log n) for m > n

Can include insert, removal, etc. into analysis

----------------------
## Zig-Zig analysis

Amortized cost: 
```
2 + (Delta r(x) + Delta r(y) + Delta r(z))

<= 2 + r_after(x) + r_after(z) - 2r_before(x)
```

For n operations starting from an empty tree, average time is O(log n)