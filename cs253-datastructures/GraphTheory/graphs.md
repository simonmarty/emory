# Graphs

## Edges of a graph

* Directed vs undirected.
* Allowing or disallowing loops and multiple adjacencies


## Path

A **path** contains no repeated vertices or edges  
A **walk** alternates between vertices and edges

## Degree

* Degree: (undireted) # of edges touching v
* Outdegree: (directed) # of edges leaving v
* Indegree: (directed) # of edges entering v

## Undirected edges

## Fullerenes

* Graphs with low maximum degree

Total possible number of edges in a regular graph: v choose 2 = &Theta;(v<sup>2</sup>)

In a fullerene: 3/2V = &Theta;(v)

## Complete graphs

Graphs that have nearly all possible edges

## Edge list

List of edges, typically not very good
Graph ADT method `edges()` outputs the edge list.

2*deg(v) + 1 = O(deg(v))

Linear get outgoing/incoming edges

## Adjacency LIst

Store list of all outgoing edges

## Adjacency Matrix

mat[i][j] == 1 means there is an edge

# Graph Traversals

Trees &rarr; Graph
* In-order &rarr; DFS

```
DFS(v):
    1. Mark v as discovered
    2. For each outgoing edge(v,w):
        - If w has not been visited, DFS(w)
```

DFS builds a tree
* Edges not in tree are back edges and cross edges
  * Cross: between branches
  * Back: cycles

Cross edges only exist in digraphs

* Preorder

* Postorder
* Breadth first

# Transitive Closure

DFS at each vertex

Worst case O(n + m) time

Total Runtime: n*O(n + m) = O(n^3)

Connectivity (undirected)

A subgraph is *connected* if every node is reachable from any other node

## DFS worst case

Connectivity

O(n) (worst case dfs) O(n + m)

Runtime: O(n + m) because we skip visited
See each vertex at most twice, see each edge one time


## Strong connectivity: two way

Can do DFS at every vertex, but that's O(n(n + m))

Backwards DFS
* Just use incoming edges

Forwards edges: directed, grandparent to grandchild

## Cycle Detection

Keep track of current set of ancestors

# Breadth First Search

* Visit every vertex at depth 0
* Visit ...             depth 1
* Undirected
  * Only cross edges
* Directed
  * Only cross, back edges

```
queue = [root]
while queue:

    l = queue.poll()
    visited[l]= true
    for neighbor in l.neighbors():
        queue.add(neighbor)
```

O(m' + n)

O(n') space


# Iterative DFS with stack

# Directed Acyclic Graph

* Has sources and sinks
  * Source: indegree 0
  * Sink: outdegree 0

Topological ordering: all arrows pointing right
Topological ordering iff directed acyclic graph
* Any cycle would contain a back edge

## Topological Order

Linear scan for each iteration
n*O(n) = O(n^2)

1. Compute indegrees
2. Push all sources into stack
3. While stack is nonempty
   1. Pop v
   2. Remove v and add to topological order
   3. If any outneighbors of v is now a source, push to stack


O(m + n)

* n stack pushes/pops
* m indegree updates


### Edge weights
* Shortest path: minimum weight sum

Assume positive edge weights (and 0)  

### Edge Relaxation

* Source
* Everything else: +&infin;

### Original Dijkstra's

```
D[v] = infinity, D[source] = 0
collection = vertices  
while collection is nonempty:
    remove u with min D[u]
    relax all outgoing edges (u,v)
return D[end]
```

Adaptable Heap

O(n^2) time

When m = O(n^2)
* Heap O(n^2logn)
* Unsorted: O(n^2)

When m << n^2/logn, use heap
When m >> use unsorted

### Ternary heap

More children: bubbling down slower
Shallower depth: bubbling up faster

## Bellman Ford

```
D[v] = infinity, D[source] = 0
Repeat n - 1 times:
    Relax every edge
If there's still a relaxable edge, out put "negative cycle"
```

When m = O(N^2)
* Heap: O(n^2 log n)
* Unsorted collection: O(n<sup>2,</sup>)

## Bellman-Ford

* D[v] = infinity, D[source] = 0
* Repeat n-1 times:
  * Relax every edge
* If there's still a relaxable edge, output "negative cycle"


## Kruskal's algorithm

1. Sort all edge weights
2. Repeatedly pick the smellest ege without creating a cycle
3. Clusters: can't link two nodes in the same cluster
4. If you link two nodes, their clusters get merged

```
makeCluster(x)
union(p, q)
find(p)
```

```
makeCluster each vertex

```
```
Total Runtime: 
Sorting: O(m log m)
= O(m log n)  since m = O(n^2)

Total runtime: O(m log n) + O(m + nlogn)
= O(m log n)
```
## Prim's algorithm

1. set S = {v}
2. Repeatedly "grow" the minimum spanning tree
3. 

Weight of minimum spanning tree: sum of all edges in tree

# TSP

