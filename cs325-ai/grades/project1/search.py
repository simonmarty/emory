# THIS  CODE  WAS MY OWN WORK , IT WAS  WRITTEN  WITHOUT  CONSULTING  ANY
# SOURCES  OUTSIDE  OF  THOSE  APPROVED  BY THE  INSTRUCTOR Simon Marty

# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    visited = set()
    stack = [(problem.getStartState(), [])]

    while len(stack):
        pos, path = stack.pop()
        visited.add(pos)

        if problem.isGoalState(pos):
            return path

        for pos, direction, cost in problem.getSuccessors(pos):
            if pos not in visited:
                stack.append((pos, path + [direction]))


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """

    # Using the standard library here, just because I'm a bit more familiar with it
    from collections import deque

    visited = set()
    queue = deque()

    start = problem.getStartState()

    # Tuple is (position, path), where path is a list containing the moves taken to get
    # to the current state
    queue.append((start, []))
    visited.add(start)

    while queue:
        pos, path = queue.popleft()

        if problem.isGoalState(pos):
            return path

        # The line below is the second best thing about python (after lambdas, obviously)
        for pos, direction, cost in problem.getSuccessors(pos):
            if pos not in visited:
                visited.add(pos)
                queue.append((pos, path + [direction]))

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    import heapq

    # Using a dict here, since I want to store the best cost for each node
    visited = {}
    # Priority queue
    pq = []

    start = problem.getStartState()

    # Tuple is (cost, position, path), where path is a list containing the moves taken to get
    # to the current state
    # heapq will use the first element in a tuple for maintaining heap order in Python
    heapq.heappush(pq, (0, start, []))
    visited[start] = 0

    while pq:
        parent_cost, parent_pos, parent_path = heapq.heappop(pq)

        if problem.isGoalState(parent_pos):
            return parent_path

        for pos, direction, cost in problem.getSuccessors(parent_pos):
            new_cost = parent_cost + cost   # The cost to get to this node from the current one
            if pos not in visited.keys() or visited[pos] >= new_cost:
                visited[pos] = new_cost
                heapq.heappush(pq, (new_cost, pos, parent_path + [direction]))


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    import heapq

    visited = set()
    # Priority queue
    pq = []

    start = problem.getStartState()

    # Tuple is (cost, position, path), where path is a list containing the moves taken to get
    # to the current state
    # heapq will use the first element in a tuple for maintaining heap order in Python
    heapq.heappush(pq, (heuristic(start, problem), start, []))

    while pq:
        parent_cost, parent_pos, parent_path = heapq.heappop(pq)

        if parent_pos not in visited:
            visited.add(parent_pos)

            if problem.isGoalState(parent_pos):
                return parent_path

            for pos, direction, cost in problem.getSuccessors(parent_pos):
                child_path = parent_path + [direction]
                heapq.heappush(pq, (problem.getCostOfActions(child_path) + heuristic(pos, problem), pos, child_path))


# Abbreviations
bfs = breadthFirstSearch

dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
