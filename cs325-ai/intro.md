# AI and Types of (Rational) Agents

## What is AI?

The science of making machines that:
* Think like people
* Act like people
* Think rationally
* Act rationally

## Natural Language

* Speech technologies
  * Automatic speech recognition
  * Text-to-speech synthesis
  * Dialog systems

## Desiging Rational Agents

* An agent is an entity that perceives and acts
* A rational agent selects actions that maximize its (expected) utility
* Characteristics of the percepts, environment, and action space dictate techniques for selecting rational actions

## Five basic types in order of increasing generality

* Table Driven agents
* Simple reflex agents
  * Act only on the basis of the current percept
  * Based on the *condition-action rules*
    * ```
        if condition
        then action
      ```
* Model-based reflex agents
* Goal-based agents
  * Problem solving agents
* Utility-based agents
  * Can distinguish between different goals
* Learning agents


## Planning Agents

* Planning agents:
  * Ask "what if"
  * Decisions based on (hypothesized) consequences of actions
  * Must have a model of how the world evolves in response to actions
  * Must formulate a goal (test)

* Optimal vs. complete planning
* Planning vs. replanning

## Performance Measure

An objective criterion for success of an agent's behavior

Rational Agent selects actions that are expected to maximize its performance measure, given percept sequence and agent's built-in knowledge.

## General Tree Search



Strategies are evaluated along the following dimensions
* Completeness: Does it always find a solution
* Optimality: Does it always find a least-cost solution
* TIme and space complexity

## DFS

## BFS

Informed Search and Heuristics

## BFS + DFS: Iterative Deepening (ID)

Combine DFS space advantage with BFS time/shallow-solution advantages

## Uniform Cost Search (UCS) Properties

What nodes does UCS expand?
* Processes all nodes with cost less than cheapest solution
* If that solution costs C* and arcs cost at least &epsilon;, then the effective depth is roughly C*/&epsilon;
* Takes time O(b<sup>c*/&epsilon;</sup>)
* Space: O(b<sup>C*/&epsilon;</sup>)
* Assuming the best solution has a finite cost and minimum arc cost is positive, yes
* Optimal (proof via A*)

## Greedy Search

* Strategy: expand a node that you think is closest to a goal state
* Best-first takes you straight to the (wrong) goal
* Worst-case: like a badly-guided DFS

## UCS + Greedy = A\*

* **Uniform-cost** orders by path cost, or *backward cost* g(n)
* **Greedy** orders by goal proximity, or *forward cost* h(n)
* **A\* Search** orders by the sum: f(n) = g(n) + h(n)

* A heuristic *h* is admissible if
  * 0 &leq; h(n) &leq; h*(n)
  * Where h*(n) is the true cost to a nearest goal

## Optimality of A* Tree Search: Blocking

Proof:
* Imagine B is on the fringe
* Some ancestor n of A is on the fringe
* Claim: n will be expanded before B

# Heuristics

## Tiles heuristic

* Compute number of start missing
* Can take a long time to compute
* h(start) = 8

## Manhattan heuristic

* Relaxation: easier 8-puzzle where any tile could slide any direction at any time ignoring other tiles
* Total Manhattan distance from correct location
* h(start) = 3 + 1 + 2 + ... = 18

## Dominance

If h<sub>2</sub>(n) &geq; h<sub>1</sub>(n) for all n (both admissible), then h<sub>2</sub> **dominates** h<sub>1</sub>

# Graph Search

## Consistency of Heuristics

Main idea: estimated heuristic costs &leq; actual costs
* Admissibility: heuristic cost &leq; actual cost to goal
* Consistency: heuristic arc cost &leq; actual cost for each arc

# A*: Summary

* A* uses both backward costs and estimates of forward costs
* A* is optimal with admissible/consistent heuristics
* Heuristic design is key: often use relaxed problems