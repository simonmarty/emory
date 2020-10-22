# Networking: Continued

## Residual Graph

For each edge with capacity x/y, we can map two residual edges. We can increase the flow in its direction by (y-x) or decrease the flow by x at most.

Why does this work?

## Incremental Algorithm

Find augmenting paths until there aren't any

## Max flow Min cut theorem

A **st-cut** is a partition {V<sub>L</sub>, V<sub>R</sub>} so that s is in V<sub>L</sub> and t is in V<sub>R</sub>

Min cut problem

## Ford Fulkerson Algorithm

FF constructs a **sequence** of flows

### Integrality
* Each iteration of FF finds an augmenting path
* If the capacities are integers, every flow it generates will be integers.

Finding an augmenting path = reachability in residual graph  
Number of iterations:  
* Flow increases by >= 1

O(value(flow)) iterations

## Edmonds-Karp Heuristic:
* Use BFS to find augmenting path

1. Initialize G to flow 0
2. While residual graph has augmenting path
   1. Augment flow using path *as best as possible*
   

## Integrality

0/1-flows useful in combinatorial applications

Ex: Find max number of edge-disjoint paths from s to t.

## Bipartite Matching

A **matching** is a subset of eges that dont share any common endpoints
A **maximum matching** is the biggest one, **perfect match** uses all vertices

## Integrality

FF yields an integral max flow, but not every max flow is integral

## Bipartite matching

### Regular case

Suppose we have *n* applicants and n companies satisfying:
* Each applicant applies to *r* places
* Each company receives *r* apps

Is it possible to schedule *r* full interview days? Yes

Fractional max flow: 1/r

### Example: Baseball games

Max flow: flow = wins

Left side: Remaining games
Right side: Corresponding Teams


## Linear Programming

A factory makes *gizmos* (x) and *gadgets* (y) and wants to maximize its profits

Gizmo = $43, Gadget = $34  
* Only 180 hours of work time (x = 2, y = 3)
* Only 440 tons of steel (x = 8, y = 5)

### Expressing a max flow problem in terms of linear programming

* 0 &leq; f(e) &leq; 

Maximize: sum of f<sub>sv</sub>

### Min cut as an LP

Variables: d<sub>uv</sub>, v<sub>v</sub>

Constraints:
* d<sub>uv</sub> &leq; c<sub>uv</sub>
* f<sub>av</sub> = f<sub>va</sub>

Maximize: sum of f<sub>sv</sub>

### Max Flow as an LP

